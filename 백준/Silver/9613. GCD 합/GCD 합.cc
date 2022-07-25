#include <bits/stdc++.h>
using namespace std;

int arr[100];
int main(){
    ios::sync_with_stdio(0);
    int N,t,x;
    cin >> N;
    while (N--){
        cin >> t;
        for (int i=0;i<t;i++){
            cin >> x;
            arr[i] = x;
        }
        long long int s = 0;
        for (int i=0;i<t-1;i++){
            for (int j=i+1;j<t;j++){
                s += gcd(arr[i],arr[j]);
            }
        }
        cout << s << '\n';
    }
}