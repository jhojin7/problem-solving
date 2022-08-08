#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int x,A,B,C;
    cin >> A >> B >> C;
    if (C-B==0){
        cout << -1;
        return 0;
    }
    x = A/(C-B)+1;
    if (x<0) cout << -1;
    else cout << x;
    return 0;
}