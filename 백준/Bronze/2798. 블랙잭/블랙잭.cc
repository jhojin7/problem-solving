#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int N, M, x;
    vector<int> arr;

    cin >> N >> M;
    for (int i=0;i<N;i++){
        cin >> x;
        arr.push_back(x);
    }

    int mindiff = 99999999;
    int ans;
    for (auto a:arr){
        for (auto b:arr){
            for (auto c:arr){
                if (a!=b and b!=c and c!=a){
                    int diff = M-(a+b+c);
                    if (diff >= 0 and mindiff >= diff){
                        mindiff = diff;
                        ans = a+b+c;
                    }
                }
            }
        }
    }
    cout << ans;
    return 0;
}