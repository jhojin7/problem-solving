#include <bits/stdc++.h>
using namespace std;

const int MAXINT = 2187+3; 
int paper[MAXINT][MAXINT];
int N;
map <int,int> cnt;
using Counter = map<int,int>;

Counter recurse(int n, int x,int y){
    // stop recursion
    if (n == 3){
        Counter cnt_local;
        for (int i=0;i<3;i++){
            for (int j=0;j<3;j++){
                cnt_local[paper[x+i][y+j]]+=1;
            }
        }
        return cnt_local;
    }
    // do recursion
    Counter cnt;
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            Counter cnt_local = recurse(n/3,x+n/3*i,y+n/3*j);
            // add counts
            if (!cnt_local[0]and !cnt_local[1]) cnt[-1]+=1;
            else if (!cnt_local[-1]and !cnt_local[1]) cnt[0]+=1;
            else if (!cnt_local[-1]and !cnt_local[0]) cnt[1]+=1;
            else{
                cnt[-1]+=cnt_local[-1];
                cnt[0]+=cnt_local[0];
                cnt[1]+=cnt_local[1];
            }
        }
    }
    return cnt;
}
int main(){
    ios::sync_with_stdio(0);
    cin >> N;

    for (int i=0;i<N;i++)
        for (int j=0;j<N;j++)
            cin >> paper[i][j];

    Counter cnt = recurse(N,0,0);
    if (!cnt[0]and !cnt[1]) cnt[-1]=1;
    else if (!cnt[-1]and !cnt[1]) cnt[0]=1;
    else if (!cnt[-1]and !cnt[0]) cnt[1]=1;

    cout << cnt[-1] << '\n';
    cout << cnt[0] << '\n';
    cout << cnt[1] << '\n';
    return 0;
}