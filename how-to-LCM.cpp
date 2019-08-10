#include <iostream>
using namespace std;
auto lcm2(int x, int y = 1){
    int c = 1;
    while (true){
        if ((x * c) % y == 0){
            return x * c;
            break;
        }
        c++;
    }
}
int main(){
    std::cout << lcm2(1001, 21) << std::endl;
}
