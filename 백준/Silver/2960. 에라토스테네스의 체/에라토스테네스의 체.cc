#include <bits/stdc++.h>
using namespace std;

vector <bool> primes(1002,true);
int main(){
    ios::sync_with_stdio(0);
    int N,K,cnt=0;
    cin >> N >> K;
    primes[1] = false;

    for (int i=2;i<=N;i++){
        // cout << i;
        if (!primes[i]) continue;
        for (int j=i;j<=N;j+=i){
            if (!primes[j]) continue;
            primes[j] = false;
            cnt++;
            // cout << j << '-' << cnt << ' ';
            if (cnt == K){
                cout << j;
                return 0;
            } 
        }
        // cout << '\n';
    }
    // cout << cnt;
    return 0;
}