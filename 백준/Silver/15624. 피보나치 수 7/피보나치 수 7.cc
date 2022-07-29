#include <bits/stdc++.h>
using namespace std;
using llint = long long int;
llint dp[1000000];
llint m = 1000000007;

int main(){
    ios::sync_with_stdio(0);
    int N;
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 1;
    cin >> N;
    for (int i=2;i<=N+1;i++)
        dp[i] = dp[i-1]%m + dp[i-2]%m;
    cout << dp[N]%m;
    return 0;
}