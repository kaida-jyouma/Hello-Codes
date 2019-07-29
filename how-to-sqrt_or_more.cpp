#include <iostream>
#include <string>
#include <cmath>
using namespace std;
float rt(int x, int y = 2){
	float num = x;
	float prm = 0;
	for (int i=0;i<8;i++){
		float ct = std::pow(10, -(i));
		while (std::pow(prm, y) < num){
			prm += ct;
		}
		prm -= ct;
	}
	return prm;
}
int main(){
	std::cout << rt(2) << std::endl;
}
