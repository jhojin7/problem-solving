#include <bits/stdc++.h>
using namespace std;

bool isok(int n){
    int cnt =0;
    vector<int> arr;
    while (n>0){
        arr.push_back(n%10);
        n = n/10;
    }
    auto it = arr.begin();
    while ((it+2)!=end(arr)){
        if (*it==6 and *next(it)==6 and *next(next(it))==6){
            return true;
        }
        it++;
    }
    return false;
}

int main(){
    ios::sync_with_stdio(0);
    int N;
    cin >> N;
    int movie = 666;
    while (N>0){
        if (isok(movie)) N--;
        if (N==0) break;
        movie++;
    }
    cout << movie;
    return 0;
}