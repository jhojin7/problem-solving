#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);

    int N;
    cin >> N;
    int ans=0;
    while (N--){
        stack <char> stack;
        string str;
        cin >> str;
        for (auto c:str){
            if (!stack.empty() && stack.top() == c){
                stack.pop();
                continue;
            }
            stack.push(c);
        }
        if (stack.empty()) ans++;
    }
    cout << ans;
    return 0;
}