#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int x,y,w,h;
    cin >> x >> y >> w >> h;
    int arr[] = {abs(x-0),abs(y-0),abs(x-w),abs(y-h)};
    cout << *min_element(begin(arr),end(arr));
    return 0;
}