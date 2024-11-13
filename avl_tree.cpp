#include <iostream>
using namespace std;

typedef struct avlnode{
    int element;
    int height;
    struct avlnode *left;
    struct avlnode *right;
} avlnode;

int max(int a,int b){
    if (a > b) return a;
    else return b;
}

int height(avlnode *node){//返回高度，如果比无孩节点还低，则为-1
    if(node == NULL)
        return -1;
    else
        return node->height;
}

bool insert(avlnode *node,int number){
    if(node->left == NULL && node->right == NULL){
        if(node->element == number)//如果number == node的值，那么直接结束
            return true;
        avlnode *new_node = (avlnode*)malloc(sizeof(avlnode));//创造新节点
        if(new_node == NULL){
            cout << "This node not be craety." << endl;
            return false;
        }
        new_node->left = new_node->right = NULL;//new_node初始化
        new_node->height = number;new_node->height = 0;
        if(number < node->element){//判断左还是右
            node->left = new_node;
            return true;
        }
        else{
            node->right = new_node;
            return true;
        }
    }
    node->height = max(height(node->left),height(node->right)) + 1;//node高度加一
    return true;
}

int main(){
    return 0;
}