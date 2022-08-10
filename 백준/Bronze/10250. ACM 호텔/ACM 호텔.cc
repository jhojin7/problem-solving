#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int t;
    cin >> t;
    while (t--){
        int H,W,N;
        cin >> H >> W >> N;
        int cnt = 0;
        for (int xx=1; xx<=W; xx++){
            for (int yy=1; yy<=H; yy++){
                cnt++;
                if (cnt==N){
                    printf("%d%02d\n",yy,xx);
                    break;
                }
            }
        }
    }
    return 0;
}