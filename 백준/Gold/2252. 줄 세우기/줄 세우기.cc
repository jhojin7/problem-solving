#include <bits/stdc++.h>
using namespace std;

int stu[32001];
vector<int> dest[100001];
int indegree[100001];

int main(){
    ios::sync_with_stdio(0);
    int N, M;
    cin >> N >> M;

    int x,y; 
    for (int i=0;i<M;i++){
        cin >> x >> y;
        dest[x].push_back(y);
        indegree[y]++;
    }

    queue<int> queue;
    for (int i=1; i<=N; i++){
        if (indegree[i]==0) queue.push(i);
    }
    while (!queue.empty()){
        int u = queue.front();
        queue.pop();
        cout << u << ' ';
        for (int v: dest[u]){
            indegree[v]--;
            if (indegree[v]==0) queue.push(v);
        }
    }
    return 0;
}