#include <iostream>
#include <vector>
using namespace std;



vector<vector<int>> fibonacci(int n, vector<vector<int>>& oz) {
	if (oz[n][0] != 0 || oz[n][1] != 0) {	//n번째의 [0]횟수와 [1]횟수가 처음이 아니면
		return oz;
	}
	if (n == 0) {							//n번째가 0이면
		oz[n][n]++;							//[0][0]의 횟수 추가
		return oz;
	}
	if (n == 1) {							//n번째가 1이면
		oz[n][n]++;							//[1][1]의 횟수 추가
		return oz;
	}
	else {
		//reculsive
		fibonacci(n - 1, oz);
		fibonacci(n - 2, oz);

		//아랫단계 0, 1 횟수 count 결과를 더해줌
		oz[n][0] += oz[n - 1][0];			
		oz[n][1] += oz[n - 1][1];
		oz[n][0] += oz[n - 2][0];
		oz[n][1] += oz[n - 2][1];
		return oz;
	}
}

int main() {

	int T,n;											//테스트 케이스, 구하고자하는 서수
	vector<vector<int>> result;
	vector<vector<int>> oz;
	cin >> T;
	result.assign(T, vector<int>(2, 0));
	for (int i = 0; i < T; i++) {
		cin >> n;
		oz.assign(n + 1, vector<int>(2, 0));			//0부터 n까지의 0,1 count 저장할 vector 생성
		fibonacci(n, oz);								//호출
		
		//[테스트케이스][0 또는 1] 횟수 저장
		result[i][0] = oz[n][0];
		result[i][1] = oz[n][1];
		oz.clear();
	}
	for (int i = 0; i < T; i++) {
		cout << result[i][0] << " " << result[i][1] << endl;	//n번째의 0 횟수와 1횟수 출력
	}
	return 0;
}