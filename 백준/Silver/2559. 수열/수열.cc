#include <bits/stdc++.h>
using namespace std;
int arr[100003];
int main(){
    ios::sync_with_stdio(0);
    int N, K;
    cin >> N >> K;
    for (int i=1;i<=N;i++){
        cin >> arr[i];
        arr[i] += arr[i-1];
    }
    int maxsum = -99999999;
    for (int i=K;i<=N;i++)
        maxsum = max(arr[i]-arr[i-K],maxsum);
    cout << maxsum;
    return 0;
}