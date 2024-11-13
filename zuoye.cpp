#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main(){
    int n;
    cin >> n;
    for(int i = 0;i < n;i++){
        string x;
        int k;
        cin >> x >> k;
        if(x == "0") cout << -1 << endl;
        else{
            for (int j=0;j < k;j++) cout << 9;
            int d = x.length();
            for (int j=0;j < d-1;j++) cout << 0;
            cout << endl;
        }
    }
}