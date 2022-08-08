#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);

    vector<pair<int,int>> arr;
    for (int i=0;i<3;i++){
        int x,y;
        cin >> x >> y;
        arr.push_back({x,y});
    }
    int x = arr[0].first^arr[1].first^arr[2].first;
    int y = arr[0].second^arr[1].second^arr[2].second;
    cout << x << ' ' << y;
    return 0;
}