#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int a,b,c;
    cin >> a >> b>> c;
    int arr[3] = {a,b,c};
    sort(arr,arr+3);
    for (int i:arr) cout << i << ' ';
    return 0;
}