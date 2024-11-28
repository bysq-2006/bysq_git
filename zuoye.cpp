#include <iostream>
using namespace std;

// 定义结构体，用于存储最大值和最小值
struct MAX_MIN {
    int max; // 用于存储最大值
    int min; // 用于存储最小值
};

// 函数：返回两个整数中的最大值
int max_1(int a, int b) {
    return a > b ? a : b;
}

// 函数：返回两个整数中的最小值
int min_1(int a, int b) {
    return a < b ? a : b;
}

// 函数：获取两个整数的最大值和最小值，并以结构体形式返回
struct MAX_MIN get_max_min(int a, int b) {
    int max = max_1(a, b);
    int min = min_1(a, b);
    struct MAX_MIN s = {max, min}; // 注意这里修正了成员变量的赋值顺序
    return s;
}

// 主函数
int main() {
    struct MAX_MIN s = get_max_min(3, 5);
    cout << "最大值是: " << s.max << endl;
    cout << "最小值是: " << s.min << endl;
    return 0;
}