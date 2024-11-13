#include <iostream>
using namespace std;

typedef struct stack{
    int content;
    struct stack *next;
} stack;

stack *make_stack(){
    stack *p = (stack*)malloc(sizeof(stack));
    p->content = 0;p->next = NULL;
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

int main(){//):41   }125   ]93
    char ch[1001];
    stack *p = make_stack();
    cout << "in $ end";
    while (ch[0]!='$')
    {   
        cin >> ch;
        for(int i=0;ch[i]!=NULL;i++){
            switch (ch[i]) {
                case '(': 
                    in_stack(p, 41);
                    break;
                case '{': 
                    in_stack(p, 125);
                    break;
                case '[': 
                    in_stack(p, 93);
                    break;
                }
            if(ch[i]==read_top_stack(p)){
                out_stack(p);
            }
        }
    }
    if(p->next==NULL){
        cout << "yes.";
    }
    else{
        cout << "no";
    }
    cin.get();
    cin.get();
    return 0;
}