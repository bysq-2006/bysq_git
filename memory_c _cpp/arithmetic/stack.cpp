#include <iostream>
using namespace std;

typedef struct stack{
    int content;
    struct stack *next;
} stack;

stack *make_stack(){
    stack *p = (stack*)malloc(sizeof(stack));
    p->content = NULL;p->next = NULL;
    return p;
}

void in_stack(stack *list,int num){
    stack *p = (stack*)malloc(sizeof(stack));
    p->content = num;
    p->next = list->next;
    list->next=p;
    return;
}

int out_stack(stack *list){
    if(list->next==NULL){
        cout << "This stack is empty.";
        return -114514;
    }
    stack *ptr = list->next;
    list->next = list->next->next;
    int temporar = ptr->content;
    free(ptr);
    return temporar;
}

void make_empty(stack *list){
    stack *ptr,*start;
    start = list;
    ptr = list = list->next;
    do{
        list=list->next;
        free(ptr);
        ptr=list;
    }while(list->next!=NULL);
    free(list);
    start->next=NULL;
}

int read_top_stack(stack *list){
    if(list->next==NULL){
        // cout << "This stack is empty.";
        return -114514;
    }
    return list->next->content;
}

int main(){
    stack *a = make_stack();
    for(int i=0;i<=10;i++){
        in_stack(a,i);
    }
    make_empty(a);
    cout << out_stack(a);
    return 0;
}