from typing import Union

from utils import Point, Line, Vertices, Edges, Graph


def legal(input: str) -> tuple([bool, Union[str, list]]):

    input = list(input.strip())
    input = [x for x in input if x != ""]
    if len(input) == 0:
        return False, "Error: not input"
    if len(input) >= 4 and input[0] == "a" and input[1] == "d" and input[2] == "d" and input[3] == " ":
        return _add_legal("".join(input[3:]))
    elif len(input) >= 4 and input[0] == "m" and input[1] == "o" and input[2] == "d" and input[3] == " ":
        return _mod_legal("".join(input[3:]))
    elif len(input) >= 3 and input[0] == "r" and input[1] == "m" and input[2] == " ":
        return _rm_legal("".join(input[2:]))
    elif len(input) == 2 and input[0] == "g" and input[1] == "g":
        return True, ["gg"]
    else:
        return False, "Error: Illegal command. Please use add, mod, rm, or gg"
    

def _add_legal(input: str) -> tuple([bool, Union[str, list]]):

    input = input.strip()
    st_legal, st_legal_msg = _st_legal(input)
    if not st_legal:
        return False, st_legal_msg
    seq_legal, seq_legal_msg = _seq_legal(input[len(st_legal_msg)+2:])
    if not seq_legal:
        return False, seq_legal_msg
    if len(seq_legal_msg) < 2:
        return False, "Error: add must contain at least 2 points"
    return True, ["add", st_legal_msg, seq_legal_msg]


def _mod_legal(input: str) -> tuple([bool, Union[str, list]]):

    input = input.strip()
    st_legal, st_legal_msg = _st_legal(input)
    if not st_legal:
        return False, st_legal_msg
    seq_legal, seq_legal_msg = _seq_legal(input[len(st_legal_msg)+2:])
    if not seq_legal:
        return False, seq_legal_msg
    if len(seq_legal_msg) < 2:
        return False, "Error: mod must contain at least 2 points"
    return True, ["mod", st_legal_msg, seq_legal_msg]

def _rm_legal(input: str) -> tuple([bool, Union[str, list]]):

    input = input.strip()
    st_legal, st_legal_msg = _st_legal(input)
    if not st_legal:
        return False, st_legal_msg
    if len(input[len(st_legal_msg)+2:].replace(" ", "")) != 0:
        return False, "Error: rm shouldn't contain anything after street name"
    return True, ["rm", st_legal_msg]


# def _st_legal(input: str) -> tuple([bool, str]):

#     input = list(input.strip())
#     input = [x for x in input if x != ""]

#     if len(input) <= 2 or input[0] != "\"":
#         return False, "Error: Must input street name after add command"

#     st_end_idx = None
#     for i in range(1, len(input)):
#         if input[i] == "\"":
#             st_end_idx = i
#             break
#     if st_end_idx == None:
#         return False, "Error: Street name must be in quotes"
#     if st_end_idx == 1:
#         return False, "Error: Street name must not be empty"
#     st_name = "".join(input[1: st_end_idx])

#     return True, st_name

def _st_legal(input: str) -> tuple([bool, str]):

    input = input.strip()

    if len(input) <= 2 or input[0] != "\"":
        return False, "Error: Must input street name after add command"
    
    input_end_idx = input.rfind("\"")
    if input_end_idx == -1:
        return False, "Error: Street name must be in quotes"
    
    st_name = input[1: input_end_idx]
    if st_name == "":
        return False, "Error: Street name must not be empty"
    
    return True, st_name
    


# def _seq_legal(input: str) -> tuple([bool, list[Point]|str]):

#     input = "".join(input).replace(" ", "").split("(")
#     print(input)
#     input = [x for x in input if x != ""]
#     if len(input) == 0:
#         return False, "Error: No points inputted"
#     for i in range(len(input)):
#         if input[i][len(input[i]) - 1] != ")":
#             return False, "Error: Points must be in the form (x,y)"
#         input[i] = input[i][:len(input[i]) - 1]
#         input[i] = input[i].split(",")
#         if len(input[i]) != 2:
#             return False, "Error: Points must be in the form (x,y)"
#         x_legal, x = _int_legal(input[i][0])
#         y_legal, y = _int_legal(input[i][1])
#         if not x_legal or not y_legal:
#             return False, "Error: Points' coordinates must be integers"
#         input[i] = Point(x=x, y=y)
#     return True, input

def _seq_legal(input: str) -> tuple([bool, Union[str, list]]):

    input = "".join(input).replace(" ", "")
    res = []
    while input != "":
        if input[0] != "(":
            return False, "Error: Points must be in the form (x,y)"
        input = input[1:]
        idx_comma = input.find(",")
        if idx_comma == -1:
            return False, "Error: Points must be in the form (x,y)"
        x_legal, x = _int_legal(input[:idx_comma])
        if not x_legal:
            return False, "Error: Points' coordinates must be integers"
        input = input[idx_comma+1:]
        idx_rbracket = input.find(")")
        if idx_rbracket == -1:
            return False, "Error: Points must be in the form (x,y)"
        y_legal, y = _int_legal(input[:idx_rbracket])
        if not y_legal:
            return False, "Error: Points' coordinates must be integers"
        input = input[idx_rbracket+1:].strip()
        res.append(Point(x=x, y=y))

    for i in range(len(res)-1):
        if res[i] == res[i+1]:
            return False, "Error: Consequential Points must be distinct"
    return True, res

        

def _int_legal(input: str) -> tuple([bool, Union[str, int]]):
    
    try:
        int(input)
        return True, int(input)
    except:
        return False, "Error: Points' coordinates must be integers"
