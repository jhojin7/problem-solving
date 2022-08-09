#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int a,b;
    while (1){
        cin >> a>> b;
        if (a==0 and b==0) break;
        else if (b%a==0) cout << "factor\n";
        else if (a%b==0) cout << "multiple\n";
        else cout << "neither\n";
    }
    return 0;
}