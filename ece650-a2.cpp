# include <iostream>
# include <string> 
# include <bits/stdc++.h>

# include "src/data/graph.h"
# include "src/data/edge.h"
# include "src/utils.h"

using namespace std;



int main(int argc, char** argv)
{   

    
    string input;
    std::vector<std::string> inputarray;
    int V;
    std::vector<std::vector<int>> E;
    Graph G;
    while(!std::cin.eof()) {
        try{
        // handle input
            getline(cin,input);
            trim(input);
            inputarray = getStringArray(input);
            if (inputarray.size() == 1) {
                continue;
            }
            else if (inputarray.size() == 2 && inputarray[0] == "V"){
                cout << input << endl;
                G.reset();
                V = 0;
                E.clear();
                V = std::stoi(inputarray[1]);
                if (V <= 1){
                    G.reset();
                    V = 0;
                    E.clear();
                    throw std::string("Invalid input");
                }
            }
            else if (inputarray.size() == 2 && inputarray[0] == "E"){
                cout << input << endl;
                if (E.size() != 0){
                    throw std::string("Invalid input");
                }
                if (V == 0){
                    E.clear();
                    throw std::string("Invalid input");
                }
                E = getEdges(inputarray[1]);
                try{
                    G.set(V, E);
                }
                catch (std::string e) {
                    E.clear();
                    throw e;
        }

            }
            else if (inputarray.size() == 3 && inputarray[0] == "s"){
                if (V == 0){
                    throw std::string("Invalid input");
                }
                if (E.size() == 0){
                    throw std::string("Invalid input");
                }
                int src = std::stoi(inputarray[1]);
                int dest = std::stoi(inputarray[2]);
                cout << bfs(G, src, dest) << endl;
            }
            else{
                throw std::string("Invalid input");
            }
        }
        catch (string e) {
            std::cerr << "Error: " << e << endl;
        }
    }
    return 0;

}