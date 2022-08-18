#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);
    int n; cin >> n;
    long long ans = 0;
    for (int i=1;i<=n;i++){
        if (n%i==0) ans += i;
    }
    cout << (ans*5)-24;
    return 0;
}