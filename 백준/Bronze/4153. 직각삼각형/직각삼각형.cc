#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int a,b,c,d;
    while (1){
        cin >> a >> b>> c;
        if (a==0 and b==0 and c==0) break;
        if (a>b){
            d = b;
            b = a;
            a = d;
        }
        if (b>c){
            d = c;
            c = b;
            b = d;
        }
        if (a*a+b*b==c*c) cout << "right\n";
        else cout << "wrong\n";
    } 

    return 0;
}