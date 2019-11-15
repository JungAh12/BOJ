#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int user;

	scanf("%d", &user);

	for (int i = 1; i <= 9; i++) {
		printf("%d * %d = %d\n",user,i,user*i);
	}
	return 0;
}