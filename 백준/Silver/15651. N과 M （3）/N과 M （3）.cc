#include <bits/stdc++.h>
using namespace std;

void f(int m, int n, vector<int> arr){
    if (n==0){
        for (auto x:arr) cout << x << ' ';
        cout << '\n';
        return;
    }
    for (int i=1;i<=m;i++){
        arr.push_back(i);
        f(m,n-1,arr);
        arr.pop_back();
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);
    int m,n;
    cin >> m >> n;
    vector<int> arr;
    f(m,n,arr);
}