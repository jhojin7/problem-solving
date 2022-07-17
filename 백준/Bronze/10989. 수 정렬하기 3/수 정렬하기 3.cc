#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int N;
    cin >> N;
    int nums[10002]={0};

    for (int i=0;i<N;i++){
        int x;
        cin >> x; 
        nums[x] +=1;
    }
    for (int i=1;i<=10000;i++){
        for (int j=0;j<nums[i];j++)
            cout << i << '\n';
    }
    return 0;
}