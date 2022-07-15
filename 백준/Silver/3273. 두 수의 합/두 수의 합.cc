#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int n,x;
    cin >> n;
    set <int> arr;
    for (int i=0;i<n;i++){
        int tmp;
        cin >> tmp;
        arr.insert(tmp);
    }
    cin >> x;

    set <pair<int,int>> paired;
    int ans = 0;
    for (auto i:arr){
        int j = x-i;
        if (arr.find(j) != arr.end() && i!=j){
            pair<int,int> pairr;
            i<j ? pairr=make_pair(i,j) : pairr=make_pair(j,i);
            paired.insert(pairr);
        }
    }

    cout << paired.size();
    return 0;
}