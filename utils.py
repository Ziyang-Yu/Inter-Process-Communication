from typing import List, Optional, Union
import copy
# class Point(object):
#     """A point in a two dimensional space"""
#     def __init__(self, x, y):
#         self.x = round(float(x), 2)
#         self.y = round(float(y), 2)

#     def __repr__(self):
#         return '(' + pp(self.x) + ', ' + pp(self.y) + ')'
    
#     def __eq__(self, __value: object) -> bool:
#         if isinstance(__value, Point):
#             return self.x == __value.x and self.y == __value.y
#         return False
    
#     def __iter__(self):
#         return iter([self.x, self.y])

class Point(tuple):
    """A point in a two dimensional space"""

    def __new__(cls, x, y, intersect=False):
        return super(Point, cls).__new__(cls, tuple([round(float(x), 5), round(float(y), 5)]))

    def __init__(self, x, y, intersect=False):
        
        self.x = round(float(x), 5)
        self.y = round(float(y), 5)
        self.intersect = intersect

    def __repr__(self):
        return '(' + pp(self.x) + ', ' + pp(self.y) + ')'
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Point):
            return self.x == __value.x and self.y == __value.y
        return False
    
    # def __ne__(self, __value: object) -> bool:
    #     if isinstance(__value, Point):
    #         return self.x != __value.x or self.y != __value.y
    #     return True
    
    def __hash__(self):
        return hash((self.x, self.y))

class Line(tuple):
    """A line between two points"""

    def __new__(cls, src: Union[int, Point], dst:Union[int, Point]):
        return super(Line, cls).__new__(cls, tuple([src, dst]))

    def __init__(self, src:Union[int, Point], dst:Union[int, Point]):

        self.src = src
        self.dst = dst
        if not isinstance(self.src, Point):
            self.src = round(self.src)
        if not isinstance(self.dst, Point):
            self.dst = round(self.dst)
            

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Line):
            return (self.src == __value.src and self.dst == __value.dst) or (self.src == __value.dst and self.dst == __value.src)
        return False
    
    # def __ne__(self, __value: object) -> bool:
    #     if isinstance(__value, Line):
    #         return (self.src != __value.src or self.dst != __value.dst) and (self.src != __value.dst or self.dst != __value.src)
    #     return True

    def __str__(self):
        return '<'+ str(self.src) + ',' + str(self.dst) + '>'
    
    def __hash__(self): # TODO: HASH
        return hash(self.src) + hash(self.dst)


class Vertices(object):
    """A list of vertices"""
    def __init__(self, vertices: List[Point]):
        self.vertices = vertices

    def __repr__(self): # TODO
        return "V = {\n" + "\n".join([str(i+1) + ": " + str(self.vertices[i]) for i in range(len(self.vertices))]) + "\n}"
    
    def num(self):
        return len(self.vertices)   
    

class Edges(object):
    """A list of edges"""
    def __init__(self, edges: List[Line]):
        self.edges = edges

    def __repr__(self): # TODO
        return "E {" + ",".join([str(self.edges[i]) for i in range(len(self.edges))]) + "}"
    

class Graph(object):
    """A graph of streets"""
    def __init__(self):
        self.vertices = {}

    def add(self, street_name: str, vertices: List[Point]):
        if street_name in self.vertices:
            raise Exception("Error: Street name already exists")
        self.vertices[street_name] = vertices

    def get(self, street_name: str) -> List[Vertices]:
        if street_name not in self.vertices:
            raise Exception("Error: Street name does not exist")
        return self.vertices[street_name]
    
    def modify(self, street_name: str, vertices: List[Point]):
        if street_name not in self.vertices:
            raise Exception("Error: Street name does not exist")
        self.remove(street_name)
        self.add(street_name, vertices)

    def remove(self, street_name: str):
        if street_name in self.vertices:
            # raise Exception("Error: Street name does not exist")
            del self.vertices[street_name]

    def reset_vertices(self):
        for st in self.vertices:
            for v in self.vertices[st]:
                v.intersect = False

    def copy(self):
        g = Graph()
        for st in self.vertices:
            st_vertices = self.vertices[st]
            st_vertices_copy = [Point(v.x, v.y) for v in st_vertices]
            g.add(st, st_vertices_copy)
        return g

    def gg(self):
        v, e = solution(self)


        return str(v) + "\n" + str(e)


def pp(x) -> str:
    """Returns a pretty-print string representation of a number.
       A float number is represented by an integer, if it is whole,
       and up to two decimal places if it isn't
    """
    if isinstance(x, float):
        return "{0:.2f}".format(x)
    if isinstance(x, int):
        return "{0:.2f}".format(str(x))
    return str(x)


def intersect(l1: Line, l2: Line) -> Optional[Point]:
    """Returns a point at which two lines intersect"""

    # end to end
    if l1.src == l2.src or l1.src == l2.dst:
        l1.src.intersect = True
        return l1.src
    if l1.dst == l2.src or l1.dst == l2.dst:
        l1.dst.intersect = True
        return l1.dst

    # vertival and horizontal
    if l1.src.y == l1.dst.y and l2.src.y == l2.dst.y:
        return None
    if l1.src.x == l1.dst.x and l2.src.x == l2.dst.x:
        return None
    if l1.src.y == l1.dst.y and l2.src.x == l2.dst.x:
        if min(l1.src.x, l1.dst.x) <= l2.src.x and max(l1.src.x, l1.dst.x) >= l2.src.x and min(l2.src.y, l2.dst.y) <= l1.src.y and max(l2.src.y, l2.dst.y) >= l1.src.y:
            return Point(l2.src.x, l1.src.y, True)
        else:
            return None
    if l1.src.x == l1.dst.x and l2.src.y == l2.dst.y:
        if min(l2.src.x, l2.dst.x) <= l1.src.x and max(l2.src.x, l2.dst.x) >= l1.src.x and min(l1.src.y, l1.dst.y) <= l2.src.y and max(l1.src.y, l1.dst.y) >= l2.src.y:
            return Point(l1.src.x, l2.src.y, True)
        else:
            return None
    
    #Consider parallel lines
    if l1.dst.x != l1.src.x and l2.dst.x != l2.src.x and round((l1.dst.y - l1.src.y) / (l1.dst.x - l1.src.x), 5) == round((l2.dst.y - l2.src.y) / (l2.dst.x - l2.src.x), 5):
        return None
    

    x1, y1 = l1.src.x, l1.src.y
    x2, y2 = l1.dst.x, l1.dst.y

    x3, y3 = l2.src.x, l2.src.y
    x4, y4 = l2.dst.x, l2.dst.y

    xnum = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4))
    xden = ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    xcoor =  xnum / xden

    ynum = (x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)
    yden = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    ycoor = ynum / yden

    return Point(xcoor, ycoor, True)

def is_intersect(l1: Line, l2: Line) -> bool:
    intersect_pt = intersect(l1, l2)
    if intersect_pt is None:
        return False
    if intersect_pt.x <= max(l1.src.x, l1.dst.x) and intersect_pt.x >= min(l1.src.x, l1.dst.x) \
        and intersect_pt.y <= max(l1.src.y, l1.dst.y) and intersect_pt.y >= min(l1.src.y, l1.dst.y) \
        and intersect_pt.x <= max(l2.src.x, l2.dst.x) and intersect_pt.x >= min(l2.src.x, l2.dst.x) \
        and intersect_pt.y <= max(l2.src.y, l2.dst.y) and intersect_pt.y >= min(l2.src.y, l2.dst.y):
        return True
    return False

def point_on_edge(p: Point, e: Line) -> bool:
    if p == e.src or p == e.dst:
        return False
    len_e = ((e.src.x - e.dst.x)**2 + (e.src.y - e.dst.y)**2)**0.5
    len_p1 = ((e.src.x - p.x)**2 + (e.src.y - p.y)**2)**0.5
    len_p2 = ((e.dst.x - p.x)**2 + (e.dst.y - p.y)**2)**0.5
    if round(len_e, 5) == round(len_p1 + len_p2, 5):
        return True
    return False


# def add(name: str, vertices: Vertices, graph: Graph):
#     """Adds a street to the graph"""
#     graph.add(name, vertices)


# def remove(name: str, graph: Graph):
#     """Removes a street from the graph"""
#     graph.remove(name)


# def modify(name: str, vertices: Vertices, graph: Graph):
#     """Modifies a street in the graph"""
#     graph.modify(name, vertices)


# def generate(graph: Graph):
#     """Generates a graph from the input"""
#     v, e = solution(graph)
#     print(v+e)

def solution(graph: Graph) -> (Vertices, Edges):
    """Returns a solution to the graph"""

    st_names = list(graph.vertices.keys())
    graph_copy = graph.copy()

    for i in range(len(st_names)):
        for j in range(i+1, len(st_names)):
            st1 = graph_copy.vertices[st_names[i]]
            st2 = graph_copy.vertices[st_names[j]]
            while True:
                stop = True
                len_st1 = len(st1)
                len_st2 = len(st2)
                for k in range(len(st1)-1):
                    for l in range(len(st2)-1):

                        l1 = Line(st1[k], st1[k+1])
                        l2 = Line(st2[l], st2[l+1])
                        if is_intersect(l1, l2):
                            intersect_pt = intersect(l1, l2)
                            if point_on_edge(intersect_pt, l1):
                                st1.insert(k+1, intersect_pt)
                            elif intersect_pt == l1.src:
                                l1.src.intersect = True
                            else:
                                l1.dst.intersect = True
                            if point_on_edge(intersect_pt, l2):
                                st2.insert(l+1, intersect_pt)
                            elif intersect_pt == l2.src:
                                l2.src.intersect = True
                            else:
                                l2.dst.intersect = True
                if len_st1 != len(st1) or len_st2 != len(st2):
                    stop = False
                if stop:
                    break
                
                    

    vertices = set()
    edges = set()
    for i in range(len(st_names)):
        st = graph_copy.vertices[st_names[i]]
        for j in range(len(st)):
            if j == 0 and st[j].intersect:
                vertices.add(st[j])
                vertices.add(st[j+1])
                edges.add(Line(st[j], st[j+1]))
            if j < len(st)-1 and st[j].intersect:
                vertices.add(st[j])
                vertices.add(st[j+1])
                vertices.add(st[j-1])
                edges.add(Line(st[j], st[j+1]))
                edges.add(Line(st[j], st[j-1]))
            if j == len(st)-1 and st[j].intersect:
                vertices.add(st[j])
                vertices.add(st[j-1])
                edges.add(Line(st[j], st[j-1]))

    vertices = list(vertices)
    edges = list(edges)
    vertices_map = {tuple(vertices[i]): i+1 for i in range(len(vertices))}
    
    edges: List[Line]
    edges = [Line(vertices_map[tuple(e.src)], vertices_map[tuple(e.dst)]) for e in edges]

    # reset intersect
    # graph.reset_vertices()
    
    
    return f"V {Vertices(vertices).num()}", Edges(edges).__repr__()


# def solution(graph: Graph) -> (Vertices, Edges):
#     """Returns a solution to the graph"""
#     vertices = set()
#     edges = set()
#     st_names = list(graph.vertices.keys())

#     hash_map = {} # point to possible lines
#     for i in range(len(st_names)):
#         for j in range(i+1, len(st_names)):
#             st1 = graph.vertices[st_names[i]]
#             st2 = graph.vertices[st_names[j]]
#             for k in range(len(st1)-1):
#                 for l in range(len(st2)-1):
#                     print("len(st_names), len(st1), len(st2)", len(st_names), len(st1), len(st2))
#                     print("k, l, i, j", k, l, i, j)
#                     l1 = Line(st1[k], st1[k+1])
#                     l2 = Line(st2[l], st2[l+1])
#                     if is_intersect(l1, l2):
#                         vertices.add(intersect(l1, l2))
#                         vertices.add(st1[k])
#                         vertices.add(st1[k+1])
#                         vertices.add(st2[l])
#                         vertices.add(st2[l+1])
#                         if intersect(l1, l2) != st1[k]:
#                             edges.add(Line(intersect(l1, l2), st1[k]))
#                         if intersect(l1, l2) != st1[k+1]:
#                             edges.add(Line(intersect(l1, l2), st1[k+1]))
#                         if intersect(l1, l2) != st2[l]:
#                             edges.add(Line(intersect(l1, l2), st2[l]))
#                         if intersect(l1, l2) != st2[l+1]:
#                             edges.add(Line(intersect(l1, l2), st2[l+1]))
                        
    
#     print("len(edges)", len(edges))
#     for e in edges:
#         e: Line
#         if e.src == e.dst:
#             edges.remove(e)

#     vertices = list(vertices)
#     edges = list(edges)

#     while True:
#         e_pre = edges.copy()
#         print("len(edges), len(vertices)", len(edges), len(vertices))
#         for v in vertices:
#             for e in edges:
#                 e: Line
#                 if point_on_edge(v, e):
#                     edges.remove(e) if e in edges else None
#                     vertices.remove(e.src) if e.src in vertices else None
#                     vertices.remove(e.dst) if e.dst in vertices else None
#                     if v.intersect or e.src.intersect:
#                         edges.append(Line(e.src, v))
#                         vertices.append(e.src)
#                         vertices.append(v)
#                     if v.intersect or e.dst.intersect:
#                         edges.append(Line(e.dst, v))
#                         vertices.append(e.dst)
#                         vertices.append(v)
#                     print(v, e, point_on_edge(v, e))
#         print("len(e_pre), len(edges)", len(e_pre), len(edges))
#         if e_pre == edges:
#             break

#     vertices = list(set(vertices))
#     edges = list(set(edges))
#     vertices_map = {tuple(vertices[i]): i+1 for i in range(len(vertices))}
    
#     edges: List[Line]
#     edges = [Line(vertices_map[tuple(e.src)], vertices_map[tuple(e.dst)]) for e in edges]

#     # reset intersect
#     graph.reset_vertices()
    
    
#     return Vertices(vertices), Edges(edges)


# 




