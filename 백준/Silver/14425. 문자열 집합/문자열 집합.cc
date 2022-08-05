#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int N,M;
    cin >> N >> M;
    set<string> strs;
    string st;
    for (int i=0;i<N;i++){
        cin >> st;
        strs.insert(st);
    }
    int cnt=0;
    for (int i=0;i<M;i++){
        cin >> st;
        if (strs.find(st)!=strs.end())
            cnt++;
    }
    cout << cnt;
    return 0;
}