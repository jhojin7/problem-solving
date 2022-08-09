#include <bits/stdc++.h>
using namespace std;
int arr[51];
int main(){
    ios::sync_with_stdio(0);
    int N,x;
    int minarr=99999999;
    cin >> N;
    for (int i=0;i<N;i++){
        cin >> x; 
        arr[i] = x;
        x<minarr ? minarr=x : minarr=minarr;
    }
    int maxarr = *max_element(begin(arr),end(arr));
    cout << maxarr*minarr;
}