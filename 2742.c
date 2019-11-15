#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int user;

	scanf("%d", &user);

    while(user!=0){
		printf("%d\n",user);
        user--;
	}
	return 0;
}