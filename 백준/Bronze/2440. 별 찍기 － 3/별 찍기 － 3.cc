#include <bits/stdc++.h>
int main(){
    using namespace std;
    int N = 5;
    cin >> N;
    for (int i=0;i<N;i++){
        for (int j=N-i-1;j>=0;j--){
            cout << '*';
        }
        cout << '\n';
    }
}