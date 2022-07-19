#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int N;
    cin >> N;
    while (N--){
        stack <char> S;
        string parens;
        cin >> parens;
        for(auto c:parens){
            if (!S.empty() && S.top()=='(' && c==')'){
                S.pop();
                continue;
            }
            S.push(c);
        }
        if (!S.empty()) cout << "NO\n";
        else cout << "YES\n";
    }
}