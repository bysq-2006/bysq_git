#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <conio.h>

typedef struct duo_xian_shi {
    struct duo_xian_shi *next;
    int left;
    int right;
} duo_xian_shi;

void jinwei(duo_xian_shi *list3, int left, int right) {
    while(1){
        if(right == list3->right){
            list3->left+=left;
            break;
        }
        else if(right > list3->right){
            duo_xian_shi *neww = (duo_xian_shi*)malloc(sizeof(duo_xian_shi));
            neww->next=list3->next;
            neww->left=list3->left;
            neww->right=list3->right;
            list3->next=neww;
            list3->left=left;
            list3->right=right;
            break;
        }
        else{
            list3=list3->next;
        }
    };
}

void multiplication(duo_xian_shi *list1,duo_xian_shi *list2,duo_xian_shi *list3){
    int left,right;
     duo_xian_shi *ptr_list2 = list2;
    while(list1!=NULL){
        list2 = ptr_list2;
        while(list2!=NULL){
            left = (list1->left) * (list2->left);
            right = list1->right + list2->right;
            jinwei(list3,left,right);
            list2 = list2->next;
        }
        list1 = list1->next;
    }
}

void printduo_xian_shi(duo_xian_shi *list){
    while(list->next!=NULL){
        printf("%dX^%d",list->left,list->right);
        printf("+");
        list=list->next;
    }
    printf("%dX^%d",list->left,list->right);
}

void add_position(duo_xian_shi *list,int n,int left,int right){//在第n个后面插入一位元素
    duo_xian_shi *p;
    p = (duo_xian_shi*)malloc(sizeof(duo_xian_shi));
    for(int i=0;i<n;i++){
        list = list->next;
    }
    p->left=left;
    p->right=right;
    p->next = list->next;
    list->next = p;
}

int main() {
    duo_xian_shi adt1,adt2;
    adt1.next=NULL;adt2.next=NULL;
    adt1.left=99999;adt1.right=2;adt2.left=666;adt2.right=0;
    add_position(&adt1,0,999,3);
    // add_position(&adt2,0,9,2);
    duo_xian_shi sum;
    sum.next=NULL;sum.left=0;sum.right=0;
    multiplication(&adt1,&adt2,&sum);
    printduo_xian_shi(&sum);
    _getch();
    return 0;
}