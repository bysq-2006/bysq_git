#include <iostream>
using namespace std;

typedef struct {//定义堆结构体
    int maxSize;
    int nowSize;
    int* arrayPtr;
} heap;

heap* make_heap(int maxSize = NULL){// 用法 heap* a = make_heap(<数字>);
    if(maxSize == NULL){
        cout << "ERROR: maxSize is empty!!!" << endl;
        return NULL;
    }
    heap* Heap = (heap*)malloc(sizeof(heap));//初始化
    Heap->maxSize = maxSize;
    Heap->nowSize = 0;
    Heap->arrayPtr = (int*)malloc(sizeof(int) * maxSize);//数组及初始化
    for(int i = 0;i < maxSize;i++){
        Heap->arrayPtr[i] = 0;
    }
    return Heap;
}



int main(){
    heap* a = make_heap(66);
    return 0;
}