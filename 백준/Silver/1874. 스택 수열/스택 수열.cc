#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int N; 
    cin>>N;
    int ToPush = 1;
    stack <int> S;
    string ans;
    while (N--){
        int x;
        cin >> x;
        if(x>=ToPush){
            while(x!=ToPush) {
                S.push(ToPush++);
                ans.append("+\n");
            }
            S.push(ToPush++);
            ans.append("+\n");
            if (S.top() == x){
                S.pop();
                ans.append("-\n");
            }
        }
        else if (S.top() == x){
            S.pop();
            ans.append("-\n");
        }
        else {
            ans = "NO\n";
            break;
        }
    }
    cout << ans;
    return 0;
}