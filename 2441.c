#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int user;

	scanf("%d", &user);

	for (int i = 0; i < user; i++) {
		for (int j = 0; j < user; j++){
			if (j < i)
				printf(" ");
	else		
				printf("*");
	}
		printf("\n");
	}
	return 0;
}