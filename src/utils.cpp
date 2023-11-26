#include <iostream>
#include <string> // for string class
#include <vector>
#include <sstream>
#include <typeinfo>
#include <set>

#include "data/graph.h"
#include "data/node.h"

using namespace std;


void trim(string &input) 
{
    input.erase(0, input.find_first_not_of(" "));
    input.erase(input.find_last_not_of(" ") + 1);
}

std::vector<std::string> getStringArray(string &input)
{
    std::vector<std::string> stringArray;
    string temp;
    int i = 0;
    while (i < int(input.length()))
    {
        if (input[i] == ' ')
        {
            stringArray.push_back(temp);
            temp = "";
        }
        else
        {
            temp += input[i];
        }
        i++;
    }
    stringArray.push_back(temp);
    return stringArray;
}

std::vector<std::string> split(string s, char del)
{
    stringstream ss(s);
    string word;
    std::vector<std::string> res = std::vector<std::string>();
    while (!ss.eof()) {
        getline(ss, word, del);
        res.push_back(word);
    }
    return res;
}

std::vector<std::vector<int>> getEdges(string& input)
{
    std::vector<std::vector<int>> edges;
    input.erase(0, 1);
    input.erase(input.size() - 1, 1);

    smatch match;
    regex r("-?[0-9]+,-?[0-9]+");
    // cout << input << endl;
    while (std::regex_search(input, match, r) == true) {
            std::vector<std::string> edge = split(match.str(0), ',');
            edges.push_back({std::stoi(edge[0]), std::stoi(edge[1])});
            input = input.substr(match.position(0)+match.str(0).length(), input.length()-(match.position(0)+match.str(0).length()));

        }
    return edges;
}


bool operator==(const Node node1, const Node node2)
{
    return node1.val == node2.val;
}

bool operator<(const Node node1, const Node node2)
{
    return node1.val < node2.val;
}

bool operator>(const Node &node1, const Node &node2)
{
    return node1.val > node2.val;
}

bool in(std::set<Node*> nodes, Node* node)
{
    for (Node* node1 : nodes){
        if (*node1 == *node){
            return true;
        }
    }
    return false;
}

string bfs(Graph &g, int start, int end)
{
    if (start > g.V || end > g.V || start <= 0 || end <= 0){
        throw std::string("Invalid input");
    }
    if (start == end){
        return std::to_string(start);
    }
    std::set<Node*> nodes;
    Node *node = new Node(start, NULL);
    nodes.insert(node);
    while (true){

        vector<Node*> temp_nodes_vector;

        for (Node *node : nodes) {

            std::vector<int> neighbours = g.getNeighbours(node->val);
            
            for (int j = 0; j < int(neighbours.size()); j++){

                Node *newNode = new Node(neighbours[j], node);
                
                if(in(nodes, newNode)){
                    continue;
                }

                temp_nodes_vector.push_back(new Node(neighbours[j], node));
            }
        }

        for (int i = 0; i < int(temp_nodes_vector.size()); i++){
            nodes.insert(temp_nodes_vector[i]);
            if (temp_nodes_vector[i]->val == end){
                goto breakloop;
            }
        }
        if (temp_nodes_vector.size() == 0){
            goto breakloop;
        }
    }
    breakloop: std::vector<Node*> nodes_vector;


    nodes_vector.reserve (nodes.size ());
    std::copy (nodes.begin(), nodes.end(), std::back_inserter (nodes_vector));
    for (int i = 0; i < int(nodes_vector.size()); i++){
        if (nodes_vector[i]->val == end){
            Node *node = nodes_vector[i];
            string path = to_string(node->val);
            while (node->prev != NULL){

                Node *node_pre = node->prev;
                path = to_string(node_pre->val) + "-" + path;
                node = node_pre;
            }
            return path;
        }
    }
    throw std::string("No path found.");
}

