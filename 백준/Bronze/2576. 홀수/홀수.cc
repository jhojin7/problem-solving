#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int num,sum=0, minval=111;
    for (int i=0;i<7;i++){
        cin >> num;
        if (num%2 ==1){
            sum += num;
            if (num < minval) minval = num;
        } 
    }
    if(minval == 111) cout << -1; 
    else cout << sum << '\n' << minval << '\n';
    return 0;
}