#include <iostream>
#include <cmath>
using namespace std;

typedef struct two_tree
{
    int x;
    int y;
} two_tree;

//默认一百位,type: two_tree
two_tree* make_start(int n = 100){
    two_tree *p = (two_tree *)malloc(sizeof(two_tree) * n);
    for (int i = 0; i < n; i++){
        p[i].x = 0;
        p[i].y = 0;
    }
    return p; // 返回指针
}

// 移动到左子节点
int move_left(int n) {
    return 2 * n + 1;
}

// 移动到右子节点
int move_right(int n) {
    return 2 * n + 2;
}

// 移动到父节点
int move_father(int n) {
    if (n < 1) {
        return 0; // 处理边界情况
    }
    return (n - 1) / 2; // 直接计算父节点
}

int main(){
    cout << move_father(11);
    return 0;
}