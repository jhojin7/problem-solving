#include <bits/stdc++.h>
using namespace std;
int cnt1,cnt2;
int fib(int n){
    if (n==1 or n==2){
        cnt1++;
        return 1;
    }
    return fib(n-1)+fib(n-2);
}

int fibonacci(int n){
    int f[42] = {0,};
    f[1]=1; f[2]=1;
    for (int i=3;i<=n;i++){
        f[i] = f[i-1]+f[i-2];
        cnt2++;
    }
    return f[n];
}

int main(){
    ios::sync_with_stdio(0);
    int n;
    cin >> n;
    fib(n);
    fibonacci(n);
    cout << cnt1 << ' ' << cnt2;
    return 0;
}