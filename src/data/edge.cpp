# include "edge.h"

// Add edge to graph
void Edges::AddEdge(int &src, int &dest){
    this->edges[src].push_back(dest);
    this->edges[dest].push_back(src);
}

void Edges::AddEdges(std::vector<std::vector<int>> &edges){
    for(int i = 0; i < int(edges.size()); i++){
        AddEdge(edges[i][0], edges[i][1]);
    }
}

// Get neighbours of a node
std::vector<int> Edges::GetNeighbours(int &src){
        // cout << "edges[src]" << (this->edges)[src].size() << "src" << src << endl;
        return this->edges[src];
}

// Get number of nodes
bool Edges::IsEdge(int &src, int &dest){
    for(int i = 0; i < int(edges[src].size()); i++){
        if(edges[src][i] == dest){
            return true;
        }
    }
    return false;
}

