#include <bits/stdc++.h>
using namespace std;
int chars[40];
map<char,int> mp;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);

    string ss;
    int maxch = 0;
    while (cin >> ss){
        // cin >> ss;
        if (ss=="\n") break;
        for (auto c:ss){
            mp[c]++;
            maxch = max(mp[c],maxch);
        }
    }
    for (char c='a'; c<='z'; c++){
        if (mp[c]==maxch) 
            cout << c;
    }
    return 0;
}