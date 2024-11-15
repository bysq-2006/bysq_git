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

avlnode* rotate_one_left(avlnode* node){//左旋转，返回node的右孩（新节点）
    avlnode* right_node = node->right;
    node->right = right_node->left;
    right_node->left = node;
    node->height = max(height(node->left),height(node->right)) + 1;
    right_node->height = max(height(right_node->left),height(right_node->right)) + 1;
    return right_node;
}

avlnode* rotate_one_right(avlnode* node){//右旋转，返回node的左孩（新节点）
    avlnode* left_node = node->left;
    node->left = left_node->right;
    left_node->right = node;
    node->height = max(height(node->left),height(node->right)) + 1;
    left_node->height = max(height(left_node->left),height(left_node->right)) + 1;
    return left_node;
}

avlnode* rotate_two_left(avlnode* node){//右双旋转，返回node的左孩的右孩（新节点）
    node->left = rotate_one_left(node->left);
    return rotate_one_right(node);
}

avlnode* rotate_two_right(avlnode* node){//右双旋转，返回node的左孩的左孩（新节点）
    node->right = rotate_one_right(node->right);
    return rotate_one_left(node);
}
//如果旋转了，父节点的高都会变，不过（node高度加一）那个地方的代码会改变所有相关父节点的高
 
avlnode* insert(avlnode *node,int number){//使用方法：node = insert(node,number);
    if(node->left == NULL && node->right == NULL){
        avlnode *node = (avlnode*)malloc(sizeof(avlnode));//创造新节点 和 如果number == node的值，那么直接结束
        if(node == NULL || node->element == number){
            cout << "This node not be craety." << endl;
            return;
        }
        node->left = node->right = NULL;//new_node初始化
        node->element = number;node->height = 0;
    }
    else if(number < node->element){// 左
        node->left = insert(node->left,number);
        if(height(node->left) - height(node->right) == 2){
            if(number < node->left->element){
                node = rotate_one_right(node);//将这个节点进行右单旋转然后返回原来节点的左孩
            }
            else{
                node = rotate_two_left(node);
            }
        }
    }
    else if(number > node->element){// 右
        node->right = insert(node->right,number);
        if(height(node->right) - height(node->left) == 2){
            if(number > node->right->element){
                node = rotate_one_left(node);//将这个节点进行左单旋转然后返回原来节点的右孩
            }
            else{
                node = rotate_two_right(node);
            }
        }
    }
    node->height = max(height(node->left),height(node->right)) + 1;//node高度加一
    return node;
}

int main(){
    return 0;
}