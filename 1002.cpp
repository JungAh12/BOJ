#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

class pos {
public:
	int x;
	int y;
};

int posRyu(int r1, int r2, pos J, pos B) {
	int result = -1;
	double d = sqrt((pow((J.x - B.x),2) )+ (pow((J.y - B.y),2)));	//J와 B의 거리
	if ((r2 - r1 == d) && (r1 == r2)) {
		result = -1;
	}
	else if ((r1 + r2 == d) || (abs(r2 - r1) == d)) {
		result = 1;
	}
	else if ((r1 + r2) > d && abs(r2 - r1) < d) {
		result = 2;
	}
	else if ((r1 + r2) < d || abs(r2 - r1) > d || (d == 0 && r1 != r2)) {
		result = 0;
	}

	return result;
}

int main() {

	pos J = pos();	//조규현좌표
	pos B = pos();	//백승환좌표
	vector<int> result;
	int JR, BR, T;

	cin >> T;

	for (int i = 0; i < T; ++i) {
		cin >> J.x >> J.y >> JR >> B.x >> B.y >> BR;	//x1,y1,r1,x2,y2,r2
		result.push_back(posRyu(JR, BR, J, B));
	}
	for (int i = 0; i < T; ++i) {
		cout << result[i] << endl;
	}

	return 0;
}

