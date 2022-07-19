#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int tc; 
    cin >> tc;
    while (tc--){
        string str;
        list <char> pw;
        cin >> str; 
        list<char>::iterator cursor = pw.begin();
        for (auto c:str){
            if (c == '-'){
                if (pw.empty()) 
                    continue;
                if (cursor != pw.begin()){
                    cursor --;
                    cursor = pw.erase(cursor);
                }
            }
            else if (c == '<'){
                if (cursor != pw.begin())
                    cursor--;
            }
            else if (c == '>'){
                if (cursor != pw.end())
                    cursor++;
            }
            else{
                pw.insert(cursor,c);
            }
        }
        for (auto c:pw) cout << c;
        cout << '\n';
    }
    return 0;
}