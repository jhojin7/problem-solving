#include <bits/stdc++.h>
using namespace std;
vector<bool> nums(10005,true); // true=prime
int main(){
    ios::sync_with_stdio(0);
    int M, N; 
    cin >> M;
    cin >> N;
    nums[0] = false;
    nums[1] = false;
    for (int n=2; n*n<=N; n++){
        // if not prime
        if (!nums[n]) continue;
        for (int m=n*n; m<=N; m+=n)
            nums[m] = false;
    }
    int anssum = 0;
    int ansfirst = -90909090;
    for (int n=M; n<=N; n++){
        if (nums[n] and ansfirst==-90909090) ansfirst = n;
        if (nums[n]) anssum += n;
    }
    if (anssum==0 and ansfirst==-90909090)
        cout << -1;
    else
        cout << anssum << '\n' << ansfirst;
}