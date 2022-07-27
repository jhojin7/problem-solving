#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    while (1){
        string str;
        cin >> str; 
        if (str=="0") break;

        bool no = false;
        auto left = str.begin(); 
        auto right = str.rbegin();
        while (left!=str.end() and right!=str.rend()){
            // if (left==right) break;
            // cout << *left << ' ' << *right << '\n';
            if (*left != *right){
                cout << "no\n";
                no = true;
                break;
            }
            left++; 
            right++;
        }
        if (!no) cout << "yes\n";
    }
    return 0;
}