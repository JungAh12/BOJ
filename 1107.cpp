//리모컨 1107
/*
button = 0 to 9, +, -
plus = channel +1
minus = channel -1
if channel == 0 and minus == true :
   non change
channel is infinite

goal channel = N
now channel = 100
*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define NUMBER 10
#define MIN(a,b) a>b ? b:a;
int main() {

	int N;
	int btn_num;
	string wrong;
	int remoteControl[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

	ios::sync_with_stdio(false); // 입력 시 속도 향상
	cin >> N;
	cin >> btn_num;
	cin.ignore();
	getline(cin, wrong);
	for (int i = 0; i < wrong.size(); ++i) {
		if (wrong[i] == ' ') continue;
		remoteControl[wrong[i] - '0'] = -1;
	}

	//이동할 수 있는 방법
	// +, -로만 이동
	int count = abs(N - 100);

	//번호로만이동
	for (int i = 0; i < 999999; i++) {
		string numstr = to_string(i);
		bool flag = false;
		for (int j = 0; j < numstr.size(); j++) {
			if (remoteControl[numstr[j] - '0'] == -1) flag = true;
			if (flag) break;
		}
		if (flag) continue;
		else {
			if (i == N) {
				count = MIN(count, numstr.size());
			}
			else {
				//혼합 이동

				count = MIN(count, abs(N - i) + numstr.size());
			}
		}
	}

	cout << count;
	
	return 0;
}