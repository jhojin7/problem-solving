#include <bits/stdc++.h>
using namespace std;

int arr[2000005];
int main(){
    ios::sync_with_stdio(0);

    int N,x; 
    cin >> N;
    while(N--){
        cin >> x;
        arr[x+1000000]+=1;
    }
    for (int i=2000005;i>=0;i--){
        for (int j=0;j<arr[i];j++)
            cout << i-1000000 << '\n';
    }
    return 0;
}