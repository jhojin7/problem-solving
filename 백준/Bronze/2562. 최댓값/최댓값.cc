#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int n,maxnum,maxidx;
    maxnum=0; maxidx=0;
    for (int i=0;i<9;i++){
        cin >> n;
        if (n > maxnum){
            maxnum = n;
            maxidx = i+1;
        }
    }
    cout << maxnum << '\n' << maxidx << '\n';
    return 0;
}