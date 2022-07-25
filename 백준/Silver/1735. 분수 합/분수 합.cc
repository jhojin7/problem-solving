#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);

    int a,b,c,d;
    cin >> a >> b;
    cin >> c >> d;

    int A = a*d + b*c;
    int B = b*d;
    for (int i=min(A,B); i>=2; i--){
        if (A%i==0 and B%i==0){
            A/=i; B/=i;
            break;
        }
    }
    cout << A << ' ' << B;
    return 0;
}