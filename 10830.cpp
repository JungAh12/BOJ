/*
* - 파이썬으로 하면 시간초과나서 못풀음
* - pypy3도 시간초과남
* - 1000%1000 = 0 나와야하는거 생각해야함
* - ^을 *로 표현할 수 있다는 것을 생각해야 분할로 풀기 가능
* - define 쓰기 귀찮아서 scanf_s썼더니 계속 컴파일 에러
*/

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int n;
long long int m;
vector<vector<int>> mul(vector<vector<int>>& A) {
	vector<vector<int>> arr(n, vector<int>(n));

	for (int i = 0; i < n; i++) {
		for (int k = 0; k < n; k++) {
			arr[i][k] = A[i][k] % 1000;
		}
	}
	return arr;
}

vector<vector<int>> mul(vector<vector<int>> &A, vector<vector<int>> &C) {
	vector<vector<int>> arr(n,vector<int>(n));

	int sub = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				sub += A[i][k] * C[k][j];
			}
			arr[i][j] = sub % 1000;
			sub = 0;
		}
	}
	return arr;
}

vector<vector<int>> recul(vector<vector<int>> &A, long long int num) {
	vector<vector<int>> C;
	if (num == 1) 
		return mul(A);

	C = recul(A, num / 2);
	C = mul(C, C);

	if (num % 2) 
		C = mul(C, A);

	return C;
}
int main() {

	vector<vector<int>> A;
	
	int num;
	scanf("%d %lld", &n, &m);
	for (int i = 0; i < n; i++) {
		vector<int> inA;
		for (int j = 0; j < n; j++) {
			scanf("%d", &num);
			inA.push_back(num);
		}
		A.push_back(inA);
	}

	vector<vector<int>> C;

	C = recul(A, m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << C[i][j] << ' ';
		}
		cout << '\n';
	}

	return 0;
}
