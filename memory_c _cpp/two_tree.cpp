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

// int move_father(int n) {    被ai爆杀,cao
//     if (n < 1){
//         return 0;
//     }; // 处理边界情况
//     int ptr1 = 0, ptr0 = 0;
//     for (int i = 0; true; i++) {
//         if ((int)pow(2, i) < n && n < (int)pow(2, i + 1)) {
//             ptr1 = (int)pow(2, i) - 1;
//             ptr0 = (int)pow(2, i - 1) - 1;
//             break;
//         }
//     }
//     for (int i = 0; ptr0 != n && ptr1 != n; i++) {
//         ptr0++;
//         ptr1 += 2;
//     }
//     return ptr0;
// }

int main(){
    cout << move_father(11);
    return 0;
}