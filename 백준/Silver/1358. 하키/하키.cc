#include <bits/stdc++.h>

int W,H,X,Y,P,R;
bool isInside(int x, int y){
    // rectangle
    if (X<=x and x<=X+W
        and Y<=y and y<=Y+H)
        return true;

    // left circle
    R = H/2; //radius
    auto d_sq = (x-X)*(x-X) + (y-(Y+R))*(y-(Y+R)); 
    if (d_sq<=R*R) return true;
    // right circle
    auto d2_sq = (x-(X+W))*(x-(X+W)) + (y-(Y+R))*(y-(Y+R)); 
    if (d2_sq<=R*R) return true;

    return false;
}

using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin >> W>>H>>X>>Y>>P;
    int x,y;
    int cnt=0;
    while (P--){
        cin >> x >> y;
        cnt += isInside(x,y);
    }
    cout << cnt;
    return 0;
}