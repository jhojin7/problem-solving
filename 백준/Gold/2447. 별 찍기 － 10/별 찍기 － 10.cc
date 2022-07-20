#include <bits/stdc++.h>
using namespace std;

const int N_MAX = 2187*3; //3^7
int N;
char arr[N_MAX][N_MAX];

void recurse(char (&arr)[N_MAX][N_MAX],int n, int a, int b){
    if (n == 3){
        for (int i=0;i<3;i++){
            for (int j=0;j<3;j++){
                int ii = a+i;
                int jj = b+j;
                if (i==1 && j==1) continue;
                arr[ii][jj] = '*';
            }
        }
        return;
    }
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            if (i==1 && j==1) continue;
            recurse(arr,n/3,a+n/3*i,b+n/3*j);
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin >> N;
    recurse(arr,N,0,0);

    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            if (arr[i][j] != '*')
                cout << ' ';
            else 
                cout << arr[i][j];
        }
        cout << "\n";
    }
    return 0;
}