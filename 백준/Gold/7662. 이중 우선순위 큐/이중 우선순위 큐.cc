#include <bits/stdc++.h>
int main(){
    using namespace std;
    ios::sync_with_stdio(0);
    int T,N;
    cin >> T;
    for (int t=0;t<T;t++){
        cin >> N;
        typedef pair<int,int> tup;
        priority_queue <tup> maxpq;
        priority_queue <tup,vector<tup>,greater<tup>> minpq;
        set <tup> visited;

        for (int i=0;i<N;i++){
            char op; int x;
            cin >> op;
            if (op == 'I'){
                cin >> x;
                minpq.push(make_pair(x,i));
                maxpq.push(make_pair(x,i));
            }
            else if (op == 'D'){
                int minmax;
                cin >> minmax; 
                if (minmax == 1){
                    while (!maxpq.empty() && visited.find(maxpq.top())!=end(visited))
                        maxpq.pop();
                    if (maxpq.empty()) continue;
                    auto popped = maxpq.top();
                    if (visited.find(popped) != end(visited)){
                        maxpq.pop();
                        continue;
                    }
                    maxpq.pop();
                    visited.insert(popped);
                } 
                else if (minmax == -1){
                    while (!minpq.empty() && visited.find(minpq.top())!=end(visited))
                        minpq.pop();
                    if (minpq.empty()) continue;
                    auto popped = minpq.top();
                    if (visited.find(popped) != end(visited)){
                        minpq.pop();
                        continue;
                    }
                    minpq.pop();
                    visited.insert(popped);
                } 
            }
        }
        while (!minpq.empty() && visited.find(minpq.top())!=end(visited))
            minpq.pop();
        while (!maxpq.empty() && visited.find(maxpq.top())!=end(visited))
            maxpq.pop();
        if (minpq.empty()) {
            cout << "EMPTY\n";
            continue;
        }
        if (maxpq.empty()) {
            cout << "EMPTY\n";
            continue;
        }
        cout << maxpq.top().first << ' ' << minpq.top().first <<'\n';
    }
    return 0;
}