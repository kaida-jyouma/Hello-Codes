#include <iostream>
#include <vector>
using namespace std;
int gcd(int x, int y = 1){
    std::vector<int> xdiv;
    std::vector<int> ydiv;
    for (auto i=1;i<=x;i++) if (x % i == 0) xdiv.push_back(i);
    for (auto j=1;j<=y;j++) if (y % j == 0) ydiv.push_back(j);
    int retgcd = 0;
    auto find = [](std::vector<int> vec, int x){int ct = 0;for (int i : vec) if (i == x) ct ++;if (ct > 0) return true;else return false;};
    for (int k : xdiv) if (find(ydiv, k)) retgcd = k;
    return retgcd;
}
int main(){
    std::cout << gcd(50, 75) << std::endl;
}
