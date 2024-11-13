#include <stdio.h>
#include <conio.h>
//只能计算偶数长度的序列
int max3(int a, int b, int c){
    if(a>=b && a>=c)
        return a;
    else if(b>=a && b>=c)
        return b;
    else
        return c;
}

int numzimax(int num[],int a,int n){
    int start =0,end = 0;
    if(a > n) {
        return 0; // 如果a大于n，返回0
    }
    if(n - a == 0){
        return num[a]; // 如果a和n相等，返回num[a]
    }
    if(n - a == 1){
        return max3(num[a], num[n], (num[a] + num[n])); // 如果a和n相差1，返回三个值中的最大值
        start = a;
        end = n;
    }
    int center = (a + n) / 2;
    int left = numzimax(num,a,center);
    int right = numzimax(num,center+1,n);
    int centermax_left = 0,centermax_right = 0;
    int acentermax_left = 0,acentermax_right = 0;
    for(int i = center;i>=a;i--){
        acentermax_left += num[i];
        if(acentermax_left>centermax_left){
            start = i;
            centermax_left = acentermax_left;
        }
    }
    for(int i = center+1;i<n;i++){
        acentermax_right += num[i];
        if(acentermax_right>centermax_right){
            end = i;
            centermax_right = acentermax_right;
        }
    }
    //英文的意思是:注:请以最后一行为标准
    printf("(Note: Please use the last standard of conduct)start:%d,end:%d\n",start,end);
    int centermax = centermax_left + centermax_right;
    return max3(left,right,centermax);
}



int main() {
    int num[8] ={4,-3,5,-2,-1,2,6,-2};
    printf("%d",numzimax(num,0,7));
    _getch();
    return 0;
}
