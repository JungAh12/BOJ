#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int x, y;

	scanf("%d %d", &x, &y);
	
	printf("%d\n%d\n%d\n%d\n%d\n",(x+y),(x-y),(x*y),(x/y),(x%y));

	return 0;
}