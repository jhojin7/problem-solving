#include <bits/stdc++.h>
using namespace std;

const char ioi[3] ={'I','O','I'};
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    // ///////////////////////////////////////////////////////

    int N,a,b,ans=0;
    set<int> s;
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> a>>b;
        if (b==1 and s.find(a)==s.end()) s.insert(a);
        else if (b==0 and s.find(a)!=s.end()){
            s.extract(a);
        }
        else ans++;
    }
    ans = ans + s.size();
    cout << ans;
    // ///////////////////////////////////////////////////////
	return 0;
}