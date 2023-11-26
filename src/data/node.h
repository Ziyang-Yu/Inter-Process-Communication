# ifndef node_h
# define node_h

# include <iostream>
# include <string> 
# include <bits/stdc++.h>
# include "node.h"

using namespace std;

class Node
{
    public:
        Node *prev;
        int val;

        // Graph();
        Node();
        Node(int &val, Node *prev);
    
};

# endif