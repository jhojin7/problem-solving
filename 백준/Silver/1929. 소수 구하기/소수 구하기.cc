#include <bits/stdc++.h>
using namespace std;
int M,N;
vector <bool> primes(1000002,true);
int main(){
    ios::sync_with_stdio(0);
    cin >> M >> N;
    // isprime
    primes[1] = false;
    for (int i=2;i*i<=N;i++){
        if (!primes[i]) continue;
        for (int j=i*i;j<=N;j+=i)
            primes[j] = false;
    }
    for (int n=M;n<=N;n++){
        if (primes[n]) cout << n << '\n';
    }
    return 0;
}