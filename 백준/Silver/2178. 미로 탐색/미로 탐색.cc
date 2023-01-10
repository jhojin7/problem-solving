#include <bits/stdc++.h>
using namespace std;

// int grid[101][101];
string grid[101];
bool vis[101][101];
using Pair = pair<pair<int,int>,int>;
#define x first
#define y second
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(){
    ios::sync_with_stdio(0);cin.tie(0);
    // freopen("input.txt", "r", stdin);
    int N,M; cin>>N>>M;
    for (int i=0; i<N; i++){
        cin >> grid[i];
    }

    queue<Pair> Q;
    Q.push({{0,0},1});
    // stack<Pair> S;
    // S.push({{0,0},1});
    vis[0][0] = 1;
    // while (!S.empty()){
    while (!Q.empty()){
        Pair cur = Q.front(); Q.pop();
        // Pair cur = S.top(); S.pop();
        int cnt = cur.second;

        if (cur.first.x==N-1 and cur.first.y==M-1){
            cout << cnt;
            return 0;
        }
        // cout << cur.first.x << cur.first.y << cnt << endl;

        for (int i=0; i<4; i++){
            int nx = cur.first.x + dx[i];
            int ny = cur.first.y + dy[i];
            if (0>nx || nx>=N || 0>ny || ny>=M) 
                continue;
            if (vis[nx][ny])
                continue;
            if (grid[nx][ny]!='1')
                continue;
            Q.push({{nx,ny},cnt+1});
            vis[nx][ny] = 1;
        }
    }
    return 0;
}