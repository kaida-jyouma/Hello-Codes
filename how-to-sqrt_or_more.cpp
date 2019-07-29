#include <iostream>
#include <string>
#include <cmath>
using namespace std;
float rt(int x){
	float num = x;
	float prm = 0;
	for (int i=0;i<8;i++){
		float ct = std::pow(10, -(i));
		while (std::pow(prm, 36) < num){
			prm += ct;
		}
		prm -= ct;
	}
	return prm;
}
int main(){
	std::cout << rt(40483056135) << std::endl;
}
