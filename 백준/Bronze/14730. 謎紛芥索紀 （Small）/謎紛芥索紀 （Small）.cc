#include <bits/stdc++.h>
using namespace std;
using ll = long long int;

ll M = pow(10,9)+7;
int main(){
    ios::sync_with_stdio(0);
    int N, x=1;
    ll c,k,ans=0;
    cin >> N;
    while (N--){
        cin >> c >> k;
        ll tmp = ((c*k)*pow(x,k-1));
        ans += fmod(tmp,M);
    }
    cout << ans;
    return 0;
}