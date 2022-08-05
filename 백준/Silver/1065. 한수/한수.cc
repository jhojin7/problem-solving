#include <bits/stdc++.h>
using namespace std;

bool isHansu(int n){
    vector<int> arr;
    int x = n;
    int prev, diff;
    while (x!=0){
        // cout << x << ' ' << x%10 << '\n';
        // cout << x%10 << '\n';
        arr.push_back(x%10);
        if (x/10==0)
            break;
        x = x/10;
    }
    // cout << n <<'\n';
    diff = arr[1]-arr[0];
    for (int i=0;i<arr.size()-1;i++){
        // cout << arr[i+1] << ' ' << arr[i] << '\n';
        if (diff!=arr[i+1]-arr[i]) 
            return false;
    }
    return true;
}


int main(){
    ios::sync_with_stdio(0);
    int N,cnt=0;
    cin >> N;
    for (int x=1;x<=N;x++){
        if (x<=99){
            cnt++;
        }
        else if (isHansu(x)==true){
            cnt++;
        }
    }
    cout << cnt; 
    return 0;
}