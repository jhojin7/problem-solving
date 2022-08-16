#include <bits/stdc++.h>
using namespace std;

vector<int> adj[1001];
int indegree[1001];

int main(){
    ios::sync_with_stdio(0);
    int N, M;
    int m,x;
    cin >> N >> M;
    for (int i=0;i<M;i++){
        cin >> m;
        vector<int> tmp;
        for (int j=0;j<m;j++){
            cin >> x;
            tmp.push_back(x);
        }
        for (int j=0;j<m-1;j++){
            adj[tmp[j]].push_back(tmp[j+1]);
            indegree[tmp[j+1]]++;
        }
    }

    vector<int> ans;
    queue<int> q;
    for (int i=1;i<=N;i++)
        if (indegree[i]==0) 
            q.push(i); 
    while (!q.empty()){
        int u = q.front();
        q.pop();
        ans.push_back(u);

        for (auto v:adj[u]){
            indegree[v]--;
            if (indegree[v]==0) 
                q.push(v);
        }
    }
    if (ans.size()!=N) cout << 0;
    else {
        for (auto u:ans) cout << u << '\n';
    }
    return 0;
}