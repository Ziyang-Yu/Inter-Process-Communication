# include <iostream>
# include <string> 
# include <bits/stdc++.h>
# include "node.h"

using namespace std;

Node::Node(int &val, Node *prev): prev(prev), val(val){
}
Node::Node(): prev(NULL), val(0){
}