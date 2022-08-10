#include <bits/stdc++.h>
using namespace std;

vector<bool> primes (10003,true);
int main(){
    ios::sync_with_stdio(0);

    // calc primes
    primes[1] = false;
    for (int i=2;i*i<=10000;i++){
        if (!primes[i]) continue;
        for (int j=i*i; j<=10000; j+=i)
            primes[j] = false;
    }

    // testcase
    int t;
    cin >> t;
    while (t--){
        int mini=0,minj=0;
        int mindiff = 99999999;
        int n;
        cin >> n;
        for (int i=2;i<=n;i++){
            int j = n-i;
            if (0<j and j<n and primes[i] and primes[j]){
                int diff = abs(j-i);
                if (diff < mindiff){
                    mindiff = diff;
                    mini = i;
                    minj = j;
                }
            }
        }
        cout << mini << ' ' << minj << '\n';
    }
    return 0;
}