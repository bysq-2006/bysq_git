#include <iostream>
#include <cmath>
using namespace std;
//

// 14

//

void swap(int* a, int* b){//交换两个数
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(int* nums,int size,int i){//如果为叶子节点，不需要堆化，否则，如果左右子节点大于父节点，则交换，并递归堆化
    int largest = i;
    int left = 2*i + 1;
    int right = 2*i + 2;
    if(left < size && nums[left] > nums[largest]){
        largest = left;
    }
    if(right < size && nums[right] > nums[largest]){
        largest = right;
    }
    if(largest!= i){
        swap(&nums[i],&nums[largest]);
        heapify(nums,size,largest);
    }
}

void build_heap(int* nums,int size){//建堆,从最后一个非叶子节点开始，往上堆化，size/2 - 1之后为叶子节点，不需要堆化
    for(int i = size/2 - 1;i >= 0;i--){
        heapify(nums,size,i);
    }
}

int left_child(int i){//左孩子
    return 2*i + 1;
}

int right_child(int i){//右孩子
    return 2*i + 2;
}

void heapsort(int* nums,int size){//堆排序
    while(size){
        swap(&nums[0],&nums[size - 1]);
        int i = 0;
        size--;
        while(left_child(i) < size - 1 || right_child(i) < size - 1){
            int l = left_child(i);
            int r = right_child(i);
            if(nums[l] >= nums[r]){
                if(nums[i] <= nums[l]){
                    swap(&nums[i],&nums[l]);
                    i = l;
                }
            }
            else{
                if(nums[i] <= nums[r]){
                    swap(&nums[i],&nums[r]);
                    i = r;
                }
            }
        }
    }
}

void shellsort(int* nums,int size){//希尔排序
    // int count = 0;
    for(int long_ = size/2;long_ > 0;long_ /= 2){
        for(int a = 0;a < long_;a++){
            for(int i = long_ + a;i < size;i += long_){
                int temnum = nums[i],j;
                for(j = i - long_;j >= 0;j -= long_){
                    // count++;
                    if(nums[j] > temnum) nums[j + long_] = nums[j];
                    else break;
                }
                nums[j + long_] = temnum;
            }
        }
    }
    // cout << count << endl;
}

void insertsort(int* nums, int size){//作者的算法是判断交换数字的地方，我是交换数字nums[j + 1] = nums[j]不判断，但是在nums[j + 1] = temnum有判断
    // int count = 0;
    for(int i = 1;i < size;i++){
        int temnum = nums[i],j;
        for(j = i - 1;j >= 0;j--){
            // count++;
            if(nums[j] > temnum) nums[j + 1] = nums[j];
            else break;
        }
        nums[j + 1] = temnum;
    }
    // cout << count << endl;
}

void partitionsort(int* nums,int start = 0,int end = 0){
    if(end - start == 1){
        if(nums[start] > nums[end]) swap(nums[start],nums[end]);
    }
    else if(end == start) return;
    else{
        int a = start + (end - start) / 2;
        partitionsort(nums,start,a);
        partitionsort(nums,a + 1,end);
        int size = end - start + 1;
        int* tempint = (int*)malloc(sizeof(int) * (size));
        int left = start,right = a + 1,i = 0;
        while(i < size){
            if(nums[left] > nums[right]){
                tempint[i] = nums[right];
                right++;
            }
            else{
                tempint[i] = nums[left];
                left++;
            }
            i++;
        }
    }
}

int main(){
    int nums[9] = {7,8,1,9,6,54,1,0,2};
    int size = sizeof(nums) / sizeof(nums[0]);
    partitionsort(nums,0,size - 1);
    for(int i=0; i<size; i++){
        cout << nums[i] << " ";
    }
    return 0;
}