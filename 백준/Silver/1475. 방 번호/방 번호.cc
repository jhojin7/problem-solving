#include <bits/stdc++.h>
int main(){
    using namespace std;
    ios::sync_with_stdio(0);
    string str;
    map <char,int> cnter;

    cin >> str;
    for (auto c:str){
        if (cnter.find(c) == end(cnter))
            cnter[c] = 0;
        cnter[c] += 1;
    }

    cnter['6'] = cnter['6']+cnter['9'];
    cnter.erase('9');

    int maxcnt=-999;
    for (auto &x:cnter){
        if (x.first == '6'){
            if (x.second%2==0) x.second/=2;
            else x.second = x.second /2 +1;
        }
        if (x.second >= maxcnt) maxcnt = x.second;
    }
    cout << maxcnt;
    return 0;
}