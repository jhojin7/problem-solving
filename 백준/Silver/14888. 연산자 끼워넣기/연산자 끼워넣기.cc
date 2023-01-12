#include <bits/stdc++.h>
using namespace std;
#define fastio ios::sync_with_stdio(0); cin.tie(0)

int num[11];
int ops[4];
int N,a,b,c,d;
int ans=0, maxans = -999999999, minans = 999999999;

auto dfs(int ans, int idx){
    if (idx==N){
        maxans = max(maxans, ans);
        minans = min(minans, ans);
        return;
    }
    for (int i=0; i<4; i++){
        if (ops[i]<=0) continue;
        ops[i]--;
        if      (i==0) dfs(ans+num[idx], idx+1);
        else if (i==1) dfs(ans-num[idx], idx+1);
        else if (i==2) dfs(ans*num[idx], idx+1);
        else if (i==3) dfs(ans/num[idx], idx+1);
        ops[i]++;
    }
}

int main(){
    fastio;
    cin >> N;
    for (int i=0; i<N; i++)
        cin >> num[i];
    for (int i=0; i<4; i++)
        cin >> ops[i];
    ans = num[0];
    dfs(ans,1);
    cout << maxans << '\n' << minans;
    return 0;
}