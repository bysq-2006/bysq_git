#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <conio.h>

struct lian_biao {
    int content;
    struct lian_biao *next;
};

typedef struct lian_biao lian_biao;

int ifempty(lian_biao *list){//判断是否为空表返回零或一
    return list->next==NULL;
}

int find_lian_biao_size(lian_biao *list){//不包括表头，从第0个开始数
    if(ifempty(list)){
        printf("The lianbiao is empty.");
        return -1;
    }
    list = list->next;
    int i=0;
    while(list->next != NULL){
        list = list->next;
        i++;
    }
    return i;
}

lian_biao* makelist(){//制造一个表头
    lian_biao *p;
    p=(lian_biao*)malloc(sizeof(lian_biao));
    if(p==NULL){
        printf("Memory allocation failure.");
        return NULL;
    }
    p->next=NULL;
    return p;
}

void ifempty_print(lian_biao *list){//判断是否为空表直接打印信息
    if(list->next==NULL){
        printf("this is an empty table.");
    }
    else {
        printf("this is not empty table.");
    }
}

void add_start(lian_biao *list,int content){//在表头添加一个数据也就是第0位
    lian_biao *p;
    p = (lian_biao*)malloc(sizeof(lian_biao));
    p->content = content;
    p->next = list->next;
    list->next = p;
}

void add_end(lian_biao *list,int content){
    lian_biao *p;
    p = (lian_biao*)malloc(sizeof(lian_biao));
    p->content = content;
    p->next = NULL; // 初始化next指针
    while(list->next!=NULL){
        list=(list->next);
    }
    list->next=p;
}

void add_position(lian_biao *list,int n,int content){//在第n个后面插入一位元素
    if(find_lian_biao_size(list) < n){
        printf("n > lianbiao_size.");
        return;
    }
    lian_biao *p;
    p = (lian_biao*)malloc(sizeof(lian_biao));
    list = list->next;
    for(int i=0;i<n;i++){
        list = list->next;
    }
    p->content = content;
    p->next = list->next;
    list->next = p;
}

void all_print(lian_biao *list){
    list = list->next; // 先移动到第一个节点
    while(list->next!=NULL){
        printf("%d\n",list->content);
        list=(list->next);
    }
    printf("%d\n",list->content);
}

int find(lian_biao *list,int content){
    if(ifempty(list)){
        printf("List is empty.\n");
        return -1;
    }
    int i=-1;
    while(list->next!=NULL){
        if(list->content == content){
            return i;
        }
        list=(list->next);
        i++;
    }
    if(list->content == content){
        return i;
    }
    printf("not content.\n");
    return -1;
}

void delete_lianbiao(lian_biao *list, int n) {//删除第n个后面一个元素
    if(find_lian_biao_size(list) < n){
        printf("n > lianbiao_size.");
        return;
    }
    lian_biao *p = list;
    for (int i = 0; i < n && p->next != NULL; i++) {
        p = p->next;
    }
    if (p->next == NULL) {
        printf("Node %d does not exist.\n", n);
        return;
    }
    lian_biao *temp = p->next;
    p->next = p->next->next;
    free(temp);
}

void replace(lian_biao *list,int n,int num){
    if(find_lian_biao_size(list) < n){
        printf("n > lianbiao_size.");
        return;
    }
    list = list->next;
    for(int i = 0;i<n;i++){
        list = list->next;
    }
    list->content=num;
}

int main() {
    lian_biao *list = makelist();
    for(int i = 0;i<10;i++){
        add_end(list,i);
    }
    delete_lianbiao(list,find(list,4));
    all_print(list);
    _getch();
    return 0;
}
