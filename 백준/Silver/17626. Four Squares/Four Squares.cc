#include <bits/stdc++.h>
std::string stdinp = R"(15663)";
std::istringstream ccccccccccccccccin(stdinp);
using namespace std;

vector<bool> cnt(5, false); // 1-idxed
void findSquares(int n)
{
    for (int i = sqrt(n); i >= 1; i--)
    {
        if (i * i == n)
            cnt[1] = true;
        for (int j = i; j >= 1; j--)
        {
            if (j * j + i * i == n)
                cnt[2] = true;
            for (int k = j; k >= 1; k--)
            {
                if (k * k + j * j + i * i == n)
                    cnt[3] = true;
                for (int l = k; l >= 1; l--)
                {
                    if (l * l + k * k + j * j + i * i == n)
                    {
                        cnt[4] = true;
                    }
                }
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin >> n;
    findSquares(n);
    if (cnt[1])
        cout << 1;
    else if (cnt[2])
        cout << 2;
    else if (cnt[3])
        cout << 3;
    else if (cnt[4])
        cout << 4;
    return 0;
}