# ifndef edge_h
# define edge_h

# include <iostream>
# include <string> 
# include <bits/stdc++.h>
#include <unordered_map>

using namespace std;


class Edges {
    
    public:
        unordered_map<int, std::vector<int>> edges;

        // Add edge to graph
        void AddEdge(int &src, int &dest);

        void AddEdges(std::vector<std::vector<int>> &edges);

        // Get neighbours of a node
        std::vector<int> GetNeighbours(int &src);

        // Get number of nodes
        bool IsEdge(int &src, int &dest);

};

# endif