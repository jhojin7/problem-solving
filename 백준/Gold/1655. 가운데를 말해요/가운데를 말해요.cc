#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;
typedef tree<
    int, null_type,
    less_equal<int>, //less_equal!!!!
    rb_tree_tag,tree_order_statistics_node_update
> ordered_set;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);

    int N,x;
    ordered_set S;
    cin >> N;
    
    while (N--){
        cin >> x;
        S.insert(x);
        // cout << x << ' ' << S.size() << ' ';
        int idx;
        if (S.size()%2 == 0)
            idx = S.size()/2-1;
        else
            idx = S.size()/2;
        cout << *S.find_by_order(idx) << '\n';
    }
    return 0;
}