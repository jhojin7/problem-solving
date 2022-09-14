#include <bits/stdc++.h>
using namespace std;

using adderRet = pair<int,int>;

adderRet half_adder(char a, char b, int carry){
    int s = 0;
    int c = 0;
    s = (a-'0') + (b-'0') + carry;
    if (s>=10){
        c = s/10;
        s = s%10;
    }
    return {c,s};
}

string full_adder(string &A, string&B){
    int s = 0;
    int carry = 0;
    string ret_string;

    auto ia = A.rbegin();
    auto ib = B.rbegin();
    adderRet x;
    while (ia!=A.rend() and ib!=B.rend()){
        x = half_adder(*ia,*ib,carry);
        carry = x.first;
        ret_string.insert(ret_string.begin(),x.second+'0');
        ia++; ib++;
    }
    while (ia!=A.rend()){
        x = half_adder(*ia,'0',carry);
        carry = x.first;
        ret_string.insert(ret_string.begin(),x.second+'0');
        ia++;
    }
    while (ib!=B.rend()){
        x = half_adder('0',*ib,carry);
        carry = x.first;
        ret_string.insert(ret_string.begin(),x.second+'0');
        ib++;
    }
    if (carry>0){
        ret_string.insert(ret_string.begin(),carry+'0');
        return ret_string;
    } 
    else return ret_string;
}

int main(){
    ios::sync_with_stdio(0);
    string A = "";
    string B = "";
    cin >> A >> B;
    cout << full_adder(A,B);

    return 0;
}