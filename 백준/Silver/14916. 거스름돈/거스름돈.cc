#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);
    int n; cin >> n;
    int mm=99999999;
    for (int i=0;i<=20000; i++){
        for (int j=0;j<=50000; j++){
            if (5*i+2*j > n) break;
            if (5*i+2*j==n){
                mm = min(mm,i+j);
            }
        }
    }
    if (mm==99999999) cout << -1;
    else cout << mm;
    return 0;
}