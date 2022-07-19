#include <bits/stdc++.h>
using namespace std;

bool ispair(char l,char r){
    // cout << l << ' ' << r << '\n';
    if (l=='(' && r==')') return true;
    else if (l=='[' && r==']') return true;
    else return false;
}

bool isparen(char c){
    if (c=='(') return true;
    else if (c==')') return true;
    else if (c=='[') return true;
    else if (c==']') return true;
    else return false;
}

int main(){
    ios::sync_with_stdio(0);
    string ans;
    while (1){
        string str;
        getline(cin,str);
        if (str == ".") break;
        
        stack <char> stack;
        for (auto c:str){
            if (c=='.') break;
            if (!isparen(c)) continue;
            if (!stack.empty() && ispair(stack.top(),c)){
                stack.pop();
                continue;
            }
            stack.push(c);
        }
        // if (stack.empty()) cout << "yes\n";
        // else cout << "no\n";
        if (stack.empty()) ans.append("yes\n");
        else ans.append("no\n");
    }
    cout << ans;
    return 0;
}