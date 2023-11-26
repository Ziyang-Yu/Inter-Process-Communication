# include <algorithm>
# include <iostream>
# include <unistd.h>
# include <cmath>
# include <vector>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>


# define _buffer_size 1024
using namespace std;

bool is_number(const std::string& s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}


int rand_s(int* arg_s){

    std::ifstream urandom("/dev/urandom");

    if (urandom.fail()) {
        throw std::string("Cannot open /dev/urandom");
    }
    unsigned int s = 1;
    urandom.read((char *)&s, sizeof(int));
    // cout << "s before: " << s << endl;
    // cout << "arg_s: " << *arg_s << endl;
    s = s % (*arg_s-1) + 2;
    // cout << "s after: " << s << endl;
    return s;
}

int rand_n(int* arg_n){

    std::ifstream urandom("/dev/urandom");

    if (urandom.fail()) {
        throw std::string("Cannot open /dev/urandom");
    }

    unsigned int n = 1;
    urandom.read((char *)&n, sizeof(int));
    n = n % (*arg_n) + 1;
    return n;
}

int rand_l(int* arg_l){

    std::ifstream urandom("/dev/urandom");

    if (urandom.fail()) {
        throw std::string("Cannot open /dev/urandom");
    }
    
    unsigned int l = 1;
    urandom.read((char *)&l, sizeof(int));

    l = l % (*arg_l- 4) + 5;
    return l;
}

int rand_c(int* arg_c){

    std::ifstream urandom("/dev/urandom");

    if (urandom.fail()) {
        throw std::string("Cannot open /dev/urandom");
    }

    unsigned int c = 1;
    urandom.read((char *)&c, sizeof(int));

    c = c % (*arg_c*2+1) - *arg_c;

    return c;
}


int crossProduct(pair<pair<int, int>, pair<int, int>>* v1, pair<pair<int, int>, pair<int, int>>* v2){ 

    int x1 = v1->second.first - v1->first.first;
    int y1 = v1->second.second - v1->first.second;
    int x2 = v2->second.first - v2->first.first;
    int y2 = v2->second.second - v2->first.second;
    
    return x1*y2 - x2*y1;
}

bool on_segment(pair<pair<int, int>, pair<int, int>>* seg, pair<int, int>* p){

    int x1 = seg->first.first;
    int y1 = seg->first.second;
    int x2 = seg->second.first;
    int y2 = seg->second.second;
    int x = p->first;
    int y = p->second;

    if (x == x1 and y == y1) return true;
    if (x == x2 and y == y2) return true;
    if (abs(sqrt( ((x-x1)^2) + ((y-y1)^2)) + sqrt( ((x-x2)^2) + ((y-y2)^2)) - sqrt( ((x1-x2)^2) + ((y1-y2)^2))) < 0.001) return true;
    return false;
}

bool seg_overlap(pair<pair<int, int>, pair<int, int>>* seg1, pair<pair<int, int>, pair<int, int>>* seg2){

    // pair<int, int> p1 = seg1->first;
    // pair<int, int> q1 = seg1->second;
    pair<int, int> p2 = seg2->first;
    pair<int, int> q2 = seg2->second;

    if (crossProduct(seg1, seg2) != 0) return false;

    if (on_segment(seg1, &p2) or on_segment(seg1, &q2)) return true;

    return false;

}

pair<int, int> next_pt(std::vector<std::vector<pair<int, int>>>* streets, bool new_street, int* arg_c){

    for (int i=0; i<25; i++){

        if (new_street){
            int x = rand_c(arg_c);
            int y = rand_c(arg_c);
            return make_pair(x, y);
        }
        else{
            int pre_x = streets->back().back().first;
            int pre_y = streets->back().back().second;
            int x = rand_c(arg_c);
            int y = rand_c(arg_c);

            pair<int, int> p1 = make_pair(pre_x, pre_y);
            pair<int, int> p2 = make_pair(x, y);

            pair<pair<int, int>, pair<int, int>> seg_new = make_pair(p1, p2);

            for (int j=0; (unsigned)(j)<streets->size(); j++){
                for (int k=0; (unsigned)(k)<streets->at(j).size()-1; k++){
                    pair<pair<int, int>, pair<int, int>> seg_pre = make_pair(streets->at(j).at(k), streets->at(j).at(k+1));
                    if (seg_overlap(&seg_new, &seg_pre)) goto label;
                }
            }
            return p2;

        }

        label: ;

    }

    throw std::string("cannot generate a valid point after 25 attempts");

}



int main(int m_argc, char **argv){

            try{

                int sdef = 10;
                int ndef = 5;
                int ldef = 5;
                int cdef = 20;

                int* arg_s = &sdef;
                int* arg_n = &ndef;
                int* arg_l = &ldef;
                int* arg_c = &cdef;

                char * temp;

                int p[2];

                // cout << "m_argc: " << m_argc << endl;
                

                std::string current_exec_name = argv[0]; // Name of the current exec program
                std::vector<std::string> all_args;

                if (m_argc > 1) {
                    all_args.assign(argv + 1, argv + m_argc);
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
                    else if ((i >= 10) &&  (is_number(all_args[i])) && (is_number(all_args[i+1]))){

                        p[0] = atoi(argv[i]);
                        p[1] = atoi(argv[i+1]);
                    }
                    else {
                        throw std::string("Invalid argument");
                    }
                }


        // int p[2];

        // p[0] = atoi(argv[5]);
        // p[1] = atoi(argv[6]);



                while(1){

                        try {
                            for (int i=0; i < 100; i++){
                                cout << "rm \"st" << i  << "\""<< endl;
                            }
                            // write(p[1], std::string("rm \n").c_str(), std::string("rm \n").size());


                            int num_st = rand_s(arg_s);
                            std::vector<std::vector<pair<int, int>>> streets;

                            for(int i=0; i<num_st; i++){
                                int num_segs = rand_n(arg_n);
                                pair<int, int> new_pt = next_pt(&streets, true, arg_c);
                                streets.push_back({new_pt});
                                for(int j=0; j<num_segs; j++){
                                    pair<int, int> pt = next_pt(&streets, false, arg_c);
                                    streets.back().push_back(pt);
                                }

                                std::string input = "add \"st" + std::to_string(i) + "\"";
                                for (int k=0; (unsigned)(k)<streets.back().size(); k++){
                                    input += " (" + std::to_string(streets.back().at(k).first) + "," + std::to_string(streets.back().at(k).second) + ") ";
                                }

                                // input += "\n";
                                cout << input << endl;
                                // write(p[1], input.c_str(), input.size());
                            }
                            cout << "gg" << endl;
                            
                            // write(p[1], std::string("gg \n").c_str(), std::string("gg \n").size());
                            sleep(rand_l(arg_l));
                }
                catch (std::string e) {
                    std::cerr << "Error: " <<  e << endl;
                    }

        }
            }
                catch (string msg){
            std::cerr << "Error: " << msg << endl;
        }




}