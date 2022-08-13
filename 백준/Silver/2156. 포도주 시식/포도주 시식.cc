#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int N;
    cin >> N;
    vector<int> arr(N+1,0);
    vector<int> dp(N+1,0);
    for (int i=1;i<=N;i++) cin >> arr[i];
    dp[1] = arr[1];
    // dp[2] = max(dp[1],arr[1]+arr[2]);
    dp[2] = dp[1]+arr[2];
    for (int i=3;i<=N;i++){
        // dp[i] = max(dp[i-1],arr[i]+dp[i-2]);
        dp[i] = max(dp[i-3]+arr[i]+arr[i-1],dp[i-2]+arr[i]);
        dp[i] = max(dp[i],dp[i-1]);
        // cout << dp[i]<<'\n';
    }
    cout << dp[N];
    return 0;
}