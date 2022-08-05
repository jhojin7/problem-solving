#include <bits/stdc++.h>
using namespace std;

vector<bool> nums(10004,false);

void d(int x){
    int s = x;
    while (x!=0){
        s += x%10;
        x = x/10;
    }
    // cout << s << ' ';
    nums[s] = true;
}

int main(){
    ios::sync_with_stdio(0);
    for (int i=1;i<=10000;i++) d(i);
    for (int i=1;i<=10000;i++){
        if (!nums[i]) cout << i << '\n';
    }
    return 0;
}