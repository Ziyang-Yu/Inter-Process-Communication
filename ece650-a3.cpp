#include <iostream>
#include <unistd.h>
#include <algorithm>
#include <iostream>
#include <unistd.h>
#include <cmath>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <cerrno>
#include <clocale>
#include <cstring>
#include <string.h>
#include <typeinfo>

using namespace std;

// char* getCmdOption(char ** begin, char ** end, const std::string & option)
// {
//     char ** itr = std::find(begin, end, option);
//     if (itr != end && ++itr != end)
//     {
//         return *itr;
//     }
//     return 0;
// }

// bool cmdOptionExists(char** begin, char** end, const std::string& option)
// {
//     return std::find(begin, end, option) != end;
// }

bool is_number(const std::string& s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}


int main (int argc, char *argv[]) {


    try {
    int sdef = 10;
    int ndef = 5;
    int ldef = 5;
    int cdef = 20;

    int* arg_s = &sdef;
    int* arg_n = &ndef;
    int* arg_l = &ldef;
    int* arg_c = &cdef;

    char * temp;
    

    std::string current_exec_name = argv[0]; // Name of the current exec program
    std::vector<std::string> all_args;

    if (argc > 1) {
        all_args.assign(argv + 1, argv + argc);
    }

    for (int i=0; i < all_args.size(); i += 2){

        if ((all_args[i] == "-s") && (i+1 < all_args.size()) && (is_number(all_args[i+1])) && (stoi(all_args[i+1]) >= 2)){
                    *arg_s = stoi(all_args[i+1]);
        }
        else if ( (all_args[i] == "-n") && (i+1 < all_args.size()) && (is_number(all_args[i+1])) && (stoi(all_args[i+1]) >= 1) ){
                    *arg_n = stoi(all_args[i+1]);
        }
        else if ((all_args[i] == "-l") && (i+1 < all_args.size()) && (is_number(all_args[i+1])) && (stoi(all_args[i+1]) >= 5)){
                    *arg_l = stoi(all_args[i+1]);
        }
        else if ((all_args[i] == "-c") && (i+1 < all_args.size()) && (is_number(all_args[i+1])) && (stoi(all_args[i+1]) >= 1)){
                    *arg_c = stoi(all_args[i+1]);
        }
        else {
            throw std::string("Invalid argument");
        }
    }




    int p0[2], p1[2];
    //p0: gen --- a1
    //p1: a1 --- a2
    //write: 1, read: 0
    // std::cout << "pipe" << std::endl;
    // stdin: 0, stdout: 1, stderr: 2
    if (pipe(p0) == -1) return 1;
    if (pipe(p1) == -1) return 1;
    // if (pipe(p2) == -1) return 1;

    pid_t pid = fork();
    if (pid == -1) return 1;

    if (pid == 0) {
        // process
        pid_t pid = fork();
        if (pid == -1) return 1;

        if (pid == 0){
            dup2(p0[1], STDOUT_FILENO);
            execl("./rgen", "./rgen", "-s", std::to_string(*arg_s).c_str(), "-n", std::to_string(*arg_n).c_str(), "-l", std::to_string(*arg_l).c_str(), "-c", std::to_string(*arg_c).c_str(), NULL);
            }
        else{
            dup2(p0[0], STDIN_FILENO);
            dup2(p1[1], STDOUT_FILENO);
            execl("/usr/bin/python3", "python3", "../../../ece650-a1.py", "--fdsp_0", std::to_string(p0[0]).c_str(), "--fdsp_1", std::to_string(p0[1]).c_str(), "--fdsp_2", std::to_string(p1[0]).c_str(), "--fdsp_3", std::to_string(p1[1]).c_str(), NULL);
        }
    }else{
        pid_t pid = fork();
        if (pid == -1) return 1;
        if (pid == 0) {
            while (1){
            //     char c;
                std::string input = "";
                std::getline(std::cin, input);
            //     for (std::string input; std::getline(std::cin, input);) {
            //         write(p1[1], input.c_str(), input.size());
            //     }
                if (input.size() != 0)
                {   
                    // cout << "input: " << input << endl; 
                    input += "\n";
                    write(p1[1], input.c_str(), input.size());
                }
            }
        }
        else{
            dup2(p1[0], STDIN_FILENO);
            execl("./ece650-a2", "./ece650-a2", std::to_string(p1[0]).c_str(), std::to_string(p1[1]).c_str());
        }
        
        }

    }
    catch (string e) {
        std::cerr << "Error: " << e << endl;
    }

    return 0;

}
