#include <bits/stdc++.h>
using namespace std;

using llint = long long int;
llint factorial(llint N){
    if (N==0) return 1;
    if (N==1) return 1;
    if (N==2) return 2;
    return factorial(N-1)*N;
}

int main(){
    int N;
    cin >> N;
    cout << factorial(N);
}