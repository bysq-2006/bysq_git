#include <iostream>
using namespace std;

int fa(int* a){
    *a = 666;
    return *a;
}

int main(){
    int a = NULL;
    int* p = &a;
    cout << fa(p);
    return 0;
}