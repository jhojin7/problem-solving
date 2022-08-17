#include <bits/stdc++.h>
using namespace std;
using llint = long long int;
llint arr[1000001];
llint cnt[1001];

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);
    int N, M;
    cin >> N >> M;
    for (int i=1;i<=N;i++){
        cin >> arr[i];
        arr[i] += arr[i-1];
        // (prefix[j]-prefix[i])%M==0
        // prefix[j]%M == prefix[i]%M
        arr[i] %= M;
        cnt[arr[i]]+=1;
    }

    llint ans = cnt[0]; // prefix[x]%M==0
    for (int x=0;x<M;x++)
        ans += cnt[x]*(cnt[x]-1)/2;
    cout << ans;
}