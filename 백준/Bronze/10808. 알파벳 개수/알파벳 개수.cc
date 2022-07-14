#include <bits/stdc++.h>
int cnt[26];
int main(){
    using namespace std;
    ios::sync_with_stdio(0);
    string str;
    cin >> str;
    for (char c:str) cnt[c-'a']++;
    for (int i:cnt) cout << i << " ";
}