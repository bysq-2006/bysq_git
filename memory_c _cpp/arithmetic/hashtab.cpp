#include <iostream>
#include <math.h>
using namespace std;

typedef struct hash_list_node{//横着的那个
    int element;
    struct hash_list_node* next;
} hash_list_node;

typedef struct hashtab{//竖着的那个
    int tabesize;
    struct hash_list_node** hash_list_ptr;
} hashtab;

hashtab* make_hashtab(int tabesize = 17){//创造一个hash表，返回指针
    hashtab* tab = (hashtab*)malloc(sizeof(hashtab));
    if(tab == NULL){
        cout << "ERROR: This tab is NULL!!!" << endl;
        return NULL;
    }
    tab->tabesize = tabesize;
    tab->hash_list_ptr = NULL;
    tab->hash_list_ptr = (hash_list_node**)malloc(sizeof(hash_list_node*) * tab->tabesize);//创建了一个指向指针数组的指针
    if(tab->hash_list_ptr == NULL){
        cout << "ERROR: This tab is NULL!!!" << endl;
        return NULL;
    }
    for(int i = 0;i < tab->tabesize;i++){
        tab->hash_list_ptr[i] = NULL;
    }
    return tab;
}

int hash_zhuanghua(char* ch,int size){//char[] => int转换器
    int sum = 0;
    for(int i = 0;i < size;i++){
        sum += ch[i];
    }
    return sum;
}

void insert(hashtab* tab,int number){//number接受int 用之前先在hash里面转换一下
    int n = number % tab->tabesize;
    hash_list_node* head = tab->hash_list_ptr[n];
    hash_list_node* ptr = head;
    while(ptr != NULL){
        if(number == ptr->element)
            return;
        ptr = ptr->next;    
    }
    hash_list_node* new_node = (hash_list_node*)malloc(sizeof(hash_list_node));
    new_node->element = number;
    new_node->next = head;
    tab->hash_list_ptr[n] = new_node;
}

void print_list(hashtab* tab){
    for(int i = 0;i < tab->tabesize;i++){
        cout << tab->hash_list_ptr[i] << ": ";
        hash_list_node* ptr = tab->hash_list_ptr[i];
        while(ptr != NULL){
            cout << ptr->element << ',';
            ptr = ptr->next;    
        };
        cout << endl;
    }
}

int main(){
    hashtab* tab0 = make_hashtab();
    insert(tab0,hash_zhuanghua("hi liujiushan",14));
    print_list(tab0);
    return 0;
}