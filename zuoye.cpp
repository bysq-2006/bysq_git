#include <iostream>
using namespace std;

bool isPalindrome(int x) {
    if(x < 0) return false;
    else{
        int xs =x ,x_ = x,size = 0;
        while(xs > 0){
            xs /= 10;
            size++;
        }
        cout << x/(size - 1);
        while(x > 0){
            
        }
    }
}

int main(){
    isPalindrome(1234567899);
    return 0;
}