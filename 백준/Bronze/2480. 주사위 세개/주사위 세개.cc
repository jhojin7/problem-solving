#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);

    string str = "";
    int arr[3];
    int cnt[10] = {0};
    int base=0,eyes = 0;

    getline(cin, str);
    istringstream iss(str);
    // cout << str << '\n';
    for (int &e : arr){
        iss >> e;
        cnt[e] += 1;
        if (cnt[e] ==3 && base < 10000){
            base = 10000;
            eyes = e;
        }
        else if (cnt[e] ==2 && base < 1000) {
            base = 1000;
            eyes = e;
        }
    } 
    // for (int e : arr) 
    //     cout << cnt[e] << ' ';

    if (base == 10000)
        cout << base+eyes*1000;
    else if (base == 1000)
        cout << base+eyes*100;
    else{
        eyes = *max_element(begin(arr),end(arr));
        cout << eyes*100; 
    }
}