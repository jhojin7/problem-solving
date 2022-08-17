#include <bits/stdc++.h>
using namespace std;
string s;
int dp[200002][26];

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);

    cin >> s;
    dp[0][s[0]-'a']+=1;
    for (int i=1;i<(int)s.length();i++){
        for (int j=0;j<26;j++)
            dp[i][j] = dp[i-1][j];
        // cout << s[i]-'a' << ' ';
        int ch = s[i]-'a';
        dp[i][ch]+=1;
    }

    int q,l,r;
    char c;
    cin >> q;
    while(q--){
        cin >> c >> l >> r;
        int lll = dp[l][c-'a'];
        int rrr = dp[r][c-'a'];
        int ans = rrr-lll;
        if (c==s[l]) ans+=1;
        // cout << lll << rrr << ans << '\n';
        cout << ans << '\n';
    }
}