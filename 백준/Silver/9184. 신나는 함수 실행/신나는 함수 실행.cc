#include <bits/stdc++.h>
using namespace std;

using trio = tuple<int,int,int>;
map<trio,int> dp;

int www(int a, int b, int c){
    trio abc = {a,b,c};
    if (dp.find(abc)!=dp.end()) return dp[abc];
    if (a<=0 or b<=0 or c<=0){
        dp[abc] = 1;
        return 1;
    } 
    else if (a>20 or b>20 or c>20) {
        dp[abc] = www(20,20,20);
        // return dp[abc];
    }
    else if (a<b and b<c){
        dp[abc] = www(a,b,c-1)+www(a,b-1,c-1)-www(a,b-1,c);
        // return dp[abc];
    }
    else{
        dp[abc] = www(a-1,b,c)+www(a-1,b-1,c)+www(a-1,b,c-1)-www(a-1, b-1, c-1);
        // return dp[abc];
    }
    return dp[abc];
}

int main(){
    ios::sync_with_stdio(0);
    int a,b,c;
    while (1){
        cin >> a >> b >> c;
        if (a==-1 and b==-1 and c==-1) break;
        www(a,b,c);
        cout << "w(" << a << ", " << b << ", " << c << ") = ";
        cout << dp[{a,b,c}] << "\n";
    }
    return 0;
}