#include <bits/stdc++.h>
using namespace std;

int N,M,arr[100];
bool visited[100];

void nm(int k){
    if (k==M){
        for (int i=0;i<M;i++)
            cout << arr[i] << ' ';
        cout << '\n';
        return;
    }
    for (int i=1;i<=N;i++){
        if (!visited[i]){
            arr[k] = i;
            visited[i] = true;
            nm(k+1);
            visited[i] = false;
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin >> N >> M;
    nm(0);
    return 0;
}