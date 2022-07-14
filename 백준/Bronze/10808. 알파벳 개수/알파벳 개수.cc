#include <bits/stdc++.h>

int main(){
    using namespace std;
    string str;
    int cnt[26] = {0};
    cin >> str;
    for (auto c:str){
        cnt[c-'a'] = cnt[c-'a']+1;
    }

    for (auto i:cnt){
        cout << i << " ";
    }
    cout << "\n";
    return 0;
}