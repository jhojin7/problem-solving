#include <bits/stdc++.h>
using namespace std;
set<int> nums;
int main(){
    ios::sync_with_stdio(0);
    int x;
    for (int i=0;i<10;i++){
        cin >> x;
        nums.insert(x%42);
    }
    cout << nums.size();
    return 0;
}