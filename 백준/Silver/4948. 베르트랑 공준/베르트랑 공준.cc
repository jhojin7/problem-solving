#include <bits/stdc++.h>
using namespace std;
vector<bool> primes(123456*2+10,true);
void sieve(int a, int b){
    // n ~ 2n
    primes[1] = false;
    for (int i=2; i*i<=b; i++){
        if (!primes[i]) continue;
        for (int j=i*i; j<=b; j+=i){
            primes[j] = false;
        }
    }
}

int cnt_sieve(int a, int b){
    int cnt = 0;
    for (int i=a;i<=b;i++)
        if (primes[i]) cnt++;
    return cnt;
}

int main(){
    ios::sync_with_stdio(0);
    sieve(1,123456*2+10);
    while (true){
        int n; 
        cin >> n;
        if (n == 0) break;
        cout << cnt_sieve(n+1,2*n) << '\n';
    }
}