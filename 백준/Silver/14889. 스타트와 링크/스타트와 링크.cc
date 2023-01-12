#include <bits/stdc++.h>
using namespace std;
#define fastio ios::sync_with_stdio(0); cin.tie(0)

int S[21][21];
bool vis[21];
int N, ans=999999999;

void dfs(int cnt, int i){
    if (cnt==N/2){
        int team1=0, team2=0;
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                if (vis[i] and vis[j])
                    team1+=S[i][j];
                else if (!vis[i] and !vis[j])///////
                    team2+=S[i][j];
            }
        }
        if (ans>abs(team1-team2))
            ans = abs(team1-team2);
        return;
    }

    for (int j=i; j<N; j++){
        vis[j] = 1;
        dfs(cnt+1, j+1);
        vis[j] = 0;
    }
}

int main(){
    fastio;
    cin >> N;
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            cin >> S[i][j];
        }
    }
    dfs(0,0);
    cout << ans;
    return 0;
}