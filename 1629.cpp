/*
처음에 행렬제곱이랑 똑같다고 생각해서

matrix multiply → scalar multiply로 바꿨는데

바로 return할 수 있는 조건들을 따지다 보니 굳이 matrix 경우처럼 식이 길어질 필요가 없었음.

- 곱하고자 하는 수가 홀수이면 A가 한번 더 곱해진다는 것을 주의해서 풀어야했음.
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
using namespace std;

long long int recul(long long int A, long long int B, long long int C) {
	if (A == C)
		return 0;
	if (B == 0)
		return 1;
	if (B == 1)
		return A % C;
	
	long long int D = recul(A, B / 2, C);

	if (B % 2 == 1) //홀수면
		return (((D * D) % C) * A) % C;
			//마지막에 A하나 더 곱해야함.
	else
		return (D*D)%C;
}
int main() {

	long long int A, B, C;

	scanf("%lld %lld %lld", &A,&B,&C);

	long long int D;
	D = recul(A, B, C);

	cout << D;

	return 0;
}
