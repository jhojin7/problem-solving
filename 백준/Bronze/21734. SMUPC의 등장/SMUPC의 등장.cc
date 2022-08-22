#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);
    string s;
    cin >> s;
    for (auto c:s){
        int tmp = c;
        int s = 0;
        while (tmp>0){
            s+=tmp%10;
            tmp/=10;
        }
        // cout << tmp << s << '\n';
        for (int i=0;i<s;i++) cout << c;
        cout << '\n';
    }
}