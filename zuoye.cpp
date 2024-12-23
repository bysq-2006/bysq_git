#include <iostream>
using namespace std;

void moveZeroes(int* nums, int numsSize) {//原理是让所有为零的元素排成一条队伍然后让这个队伍一直往后跑
    int size0 = 0;
    for(int i = 0;i < numsSize;i++){
        if(nums[i] == 0){//哪里如果检测到元素是零的话就让元素0进入队伍,表现为队伍长度加一
            size0++;
        }
        else{//如果检测到元素不为零的,就让该元素与队伍的最后一名互换表现为整个队伍向右进一步
            if(size0 == 0) continue;
            nums[i - size0] = nums[i];
            nums[i] = 0;
        }
    }
}

int main(){
    int nums[] = {0,1,0,3,12};
    int numsSize = sizeof(nums)/sizeof(nums[0]);
    moveZeroes(nums,numsSize);
    for(int i = 0;i < numsSize;i++){
        cout<<nums[i]<<" ";
    }
    return 0;
}