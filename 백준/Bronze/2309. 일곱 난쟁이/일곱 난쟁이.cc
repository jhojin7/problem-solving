#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    int heights[9] = {0};
    int sum = 0;
    for (int &h:heights){
        cin >> h;
        sum += h;
    }
    sort(begin(heights),end(heights));

    int no1=-1,no2=-1;
    for (int i=0;i<9;i++){
        for (int j=0;j<9;j++){
            if(i!=j && sum - heights[i] - heights[j] == 100){
                no1 = i;no2=j;
            }
        }
    }

    for (int i=0;i<9;i++)
        if (i!=no1 && i!=no2)
            cout << heights[i] << '\n';

    return 0;
}