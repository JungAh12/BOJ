#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int user;

	scanf("%d", &user);

	for (int i = 1; i <= user; i++) {
		printf("%d\n",i);
	}
	return 0;
}