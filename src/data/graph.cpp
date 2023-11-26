# include "graph.h"


void Graph::set(int &V, std::vector<std::vector<int>> &edges){
    for (int i = 0; i < int(edges.size()); i++){
        if (edges[i].size() != 2){
            throw std::string("Invalid input");
        }
        if (edges[i][0] > V || edges[i][1] > V || edges[i][0] <= 0 || edges[i][1] <= 0){
            throw std::string("Invalid input");
        }
        if (edges[i][0] == edges[i][1]){
            throw std::string("Invalid input");
        }
        for (int j = 0; j < i; j++){
            if (i != j && edges[i][0] == edges[j][0] && edges[i][1] == edges[j][1]){
                throw std::string("Invalid input");
            }
            if (i != j && edges[i][0] == edges[j][1] && edges[i][1] == edges[j][0]){
                throw std::string("Invalid input");
            }
        }
    }
    // cout << "address of G: " << this << endl;

    this->V = V;
    this->E.AddEdges(edges);
    // this->E.AddEdges(edges);
}

void Graph::reset(){
    this->V = 0;
    this->E.edges.clear();
}

std::vector<int> Graph::getNeighbours(int &node){
    return this->E.GetNeighbours(node);
}