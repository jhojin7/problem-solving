#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    queue <int> cards;
    int N;
    cin >> N;
    for (int i=1;i<=N;i++) cards.push(i);

    while (cards.size() != 1){
        cards.pop();
        cards.push(cards.front());
        cards.pop();
    }
    cout << cards.back();
    return 0;
}