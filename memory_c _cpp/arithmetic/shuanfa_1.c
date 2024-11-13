#include <stdio.h>
// 编写一个程序解决选择问题令K等于N除以二画出表格显示你的程序对于N维不同值的运行时间,排序从大到小
int swap(int *a,int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
int main() {
    int n[999]={0};
    int k,j=1,time=0;
    while (j!=0)
    {
        j=0;
        for(int i =0;i< 999;i++) { 
            if(n[i] < n[i+1]){
                j++;time++;
                swap(&n[i],&n[i+1]);
            }
        }
    }
    printf("请输入需要的几个数字：");
    scanf("%d",&k);
    printf("排序次数：%d\n",time);
    return 0;
}
