#include <stdio.h>
#include <conio.h>
//对分查找

int binary_search(int num[], int start, int end, int x){
    if (start > end) {
    return -1; // 如果开始位置大于结束位置，说明找不到目标
    }
    int center = (start + end) / 2;
    if(num[center] < x){
        return binary_search(num,center+1,end,x);
    }
    else if(num[center] > x){
        return binary_search(num,start,center-1,x);
    }
    if(num[center] == x){
        return center;
    }
}

int main() {
    //左到右顺序为从小到大
    int num[100] = {
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
        51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
        71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
        91, 92, 93, 94, 95, 96, 97, 98, 99, 100
    };
    int i,n = 99;//n为(数组长度-1),因为是从零开始的
    // scanf("%d", &i);
    i = 11;
    int a = binary_search(num, 0, n, i);
    printf("%d", a);
    _getch();
    return 0;
}
