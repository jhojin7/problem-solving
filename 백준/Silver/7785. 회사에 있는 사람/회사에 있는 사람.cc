#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    string name, log;
    int N;
    cin >> N;
    set <string> company;
    for (int i=0; i<N; i++){
        cin >> name;
        cin >> log;
        if (log == "enter")
            company.insert(name);
        else if (log == "leave")
            company.erase(name);
    }
    for (auto it = company.rbegin(); it!=company.rend(); it++){
        cout << *it << '\n';
    }
    return 0;
}