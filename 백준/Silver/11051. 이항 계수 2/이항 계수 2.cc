#include <bits/stdc++.h>
using namespace std;

int dp[1003][1003];
int main(){
    ios::sync_with_stdio(0);
    int n,k;
    cin >> n >> k;
    dp[0][0] = 1;
    for (int i=1;i<=n+1;i++){
        dp[i][0] = 1;
        for (int j=1; j<=k; j++){
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1])%10007;
        }
    }
    cout << dp[n][k];
    return 0;
}