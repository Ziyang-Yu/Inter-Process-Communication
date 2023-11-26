#ifndef UTILS_H
#define UTILS_H

#include <string>
#include <vector>
#include "data/graph.h"
using namespace std;

// std::vector<std::string> getStringArray;
string& trim(string &s);
std::vector<std::string> getStringArray(string &input);
std::vector<std::string> split(string s, char del);
std::vector<std::vector<int>> getEdges(string& input);
string bfs(Graph &g, int start, int end);

#endif