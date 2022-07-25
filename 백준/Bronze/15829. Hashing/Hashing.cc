#include <bits/stdc++.h>
using namespace std;

using LLong = long long int;
int r = 31;
int M = 1234567891;

LLong power(int a, int b, int m){
    LLong ret = 1;
    for (int i=0;i<b;i++){
        ret *= a%m;
        ret %= m;
    }
    return ret;
}

LLong H(string &S){
    LLong ans = 0;
    for (int i=0;i<(int)S.size();i++){
        LLong tmp = (S[i]-'a'+1)*(power(r,i,M));
        ans += tmp;
    }
    return ans%M; 
}

int main(){
    ios::sync_with_stdio(0);
    int L;
    string str;
    cin >> L;
    cin >> str;
    cout << H(str);
    return 0;
}