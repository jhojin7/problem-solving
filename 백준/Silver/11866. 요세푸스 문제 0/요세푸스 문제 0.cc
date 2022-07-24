#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int N,K; 
    cin >> N >> K;
    list <int> arr,ans;
    for (int i=1;i<=N;i++) arr.push_back(i);
    // for (auto x:arr) cout << x << ' ';
    // cout << '\n';
    list<int>::iterator it = arr.begin();

    while (arr.size() != 0){
        for (int i=0;i<K-1;i++){
            if (it == arr.end()) it = arr.begin();
            it++;
        }
        if (it == arr.end()) it = arr.begin();
        // cout << *it << '\n';
        ans.push_back(*it);
        it = arr.erase(it);
        // for (auto x:arr) cout << x << ' '; cout << '\n';
    }
    cout << "<" << ans.front();
    ans.pop_front();
    for (auto x:ans) cout << ", " << x ; 
    cout << ">";
    return 0;
}