#!/usr/bin/env python3
import sys

# YOUR CODE GOES HERE
from input import legal
from utils import Graph, Point, Line, Vertices, Edges

graph = Graph()

def main():
    # YOUR MAIN CODE GOES HERE

    # sample code to read from stdin.
    # make sure to remove all spurious print statements as required
    # by the assignment

    i = 0
    while True:
        i += 1
        line = sys.stdin.readline()
        line = line[: len(line) - 1]
        # print("read a line:", line
        if line == "":
            break
        # print("read a line:", line)
        try:
            # print("line", i, "=", line)
            legal_bol, legal_msg = legal(line)
            if not legal_bol:
                raise Exception(legal_msg)
            if legal_msg[0] == "add":
                graph.add(legal_msg[1], legal_msg[2])
            elif legal_msg[0] == "mod":
                graph.modify(legal_msg[1], legal_msg[2])
            elif legal_msg[0] == "rm":
                graph.remove(legal_msg[1])
            elif legal_msg[0] == "gg":
                print(graph.gg(), flush=True)
            else:
                raise Exception("Error: runtime error")
        except Exception as e:
            print(e, file=sys.stderr)


            

    # print("Finished reading input")
    # return exit code 0 on successful termination
    sys.exit(0)


if __name__ == "__main__":
    main()
