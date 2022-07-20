#include <bits/stdc++.h>
using namespace std;
using Counter = map<int,int>;
Counter cnter;

int main(){
    ios::sync_with_stdio(0);
    int N,f,tmp;
    cin >> N;
    for (int i=0;i<N;i++){
        cin >> tmp; 
        cnter[tmp] +=1;
    }
    cin >> f; 
    cout << cnter[f];
    return 0;
}