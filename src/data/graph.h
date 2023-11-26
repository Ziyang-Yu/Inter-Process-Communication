# ifndef graph_h
# define graph_h

# include <iostream>
# include <string> 
# include <bits/stdc++.h>
# include "edge.h"

using namespace std;

class Graph
{
    public:
        int V;
        Edges E;

        // Graph();
        void set(int &V, std::vector<std::vector<int>> &edges);
        void reset();
        std::vector<int> getNeighbours(int &node);
    
};

# endif