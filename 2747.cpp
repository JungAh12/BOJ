#include <iostream>
#include <vector>
using namespace std;

vector<int> oz;

vector<int> fibonacci(int n, vector<int>&oz) {
	if (oz[n] != 0) {
		return oz;
	}
	if (n == 0) {
		oz[n] = 0;
		return oz;
	}
	if (n == 1) {
		oz[n] = 1;
		return oz;
	}
	else {
		fibonacci(n - 1, oz);
		fibonacci(n - 2, oz);
		oz[n] = oz[n - 1] + oz[n - 2];
		return oz;
	}
}

int main() {
	
	int n;
	cin >> n;
	oz.assign(n + 1, 0);
	fibonacci(n, oz);
	cout<<oz[n]<<endl;
	
	return 0;
}