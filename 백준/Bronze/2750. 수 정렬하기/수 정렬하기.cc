#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int N;
    cin >> N;
    multiset <int> nums;
    for (int i=0;i<N;i++){
        int x;
        cin >> x; 
        nums.insert(x);
    }
    for (auto x:nums)
        cout << x << '\n';
    return 0;
}