#include <bits/stdc++.h>
int main(){
    int t,a,b,c;
    std::cin >> t;
    for (int i=0;i<t;i++){
        std::cin >> a >> b;
        c = a+b;
        if (c >= 50){
            std::cout << 49;
        }
        else if (c<=2){
            std::cout << 3;
        }
        else {
            std::cout << c+1;
        }
        std::cout << "\n";
    }
}