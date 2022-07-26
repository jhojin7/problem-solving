#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int maxS = 0, maxidx=0;
    for (int i=0; i<5; i++){
        vector <int> nums;
        int x;
        for (int i=0;i<4;i++){
            cin >> x;
            nums.push_back(x);
        }
        int S = accumulate(nums.begin(),nums.end(),0);
        if (S > maxS){
            maxS = S;
            maxidx = i;
        }
    }
    cout << maxidx+1 << ' ' << maxS << '\n';
    return 0;
}