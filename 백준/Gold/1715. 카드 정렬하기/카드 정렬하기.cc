#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    priority_queue <int,vector<int>,greater<int>> pq;
    int N,x;
    cin >> N;
    for (int i=0;i<N;i++){
        cin >> x;
        pq.push(x);
    }

    int tot = 0;
    while (pq.size() != 1){
        int a = pq.top();
        pq.pop();
        int b = pq.top();
        pq.pop();
        tot += a+b;
        pq.push(a+b);
        // cout << tot << '\n';
    }
    cout << tot << '\n';
    return 0;
}