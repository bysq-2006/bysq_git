#include <iostream>
using namespace std;

int trap(int* height, int heightSize) {
}

int main(){
    int n = 12;
    int a[n] = {0,1,0,2,1,0,1,3,2,1,2,1};
    int b[6] = {4,2,0,3,2,5};
    cout << trap(a,n) << endl;
    cout << trap(b,6);
    return 0;
}