#include <bits/stdc++.h>
using namespace std;
int d(int x){
    int s = x;
    while (x>0){
        s+=x%10;
        x=x/10;
    }
    return s;
}

int main(){
    ios::sync_with_stdio(0);
    int N;
    cin >> N;
    int ans = 9999999;
    for (int x=1;x<N;x++){
        int dx = d(x);
        // cout << x << ' ' << dx << '\n';
        if (dx==N) ans = min(ans,x);
    }
    if (ans == 9999999) cout << 0;
    else cout << ans;
    return 0;
}