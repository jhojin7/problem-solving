#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int N,x=1,y=6,ans=2;
    cin >> N;
    while (1){
        if (N==1){
            cout << 1;
            break;
        }
        if (x<N and N<=x+y){
            cout << ans;
            break;
        }
        ans +=1;
        x = x+y;
        y+=6;
    }
}