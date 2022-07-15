#include <bits/stdc++.h>
using namespace std;
list<char> text;
int main()
{
    ios::sync_with_stdio(0);
    string init;
    cin >> init;
    for (auto c : init)
        text.push_back(c);
    auto cursor = end(text);
    int N; char op;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> op;
        if (op == 'P'){
            char ch;
            cin >> ch;
            text.insert(cursor,ch);
        }
        else if (op == 'L'){
            if (cursor != begin(text))
                cursor --;
        }
        else if (op == 'D'){
            if (cursor != end(text))
                cursor ++;
        }
        else if (op == 'B'){
            if (cursor != begin(text)){
                cursor--;
                cursor = text.erase(cursor);
            }
        }

    }
    for (auto c : text) cout << c;
}