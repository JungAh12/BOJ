#include <stdio.h>
#include <stdlib.h>



int main()
{

	int *a;
	int i, j, k;
	int t;
	int n;
	int a1;
	scanf("%d %d", &n, &a1);
	a = (int*)calloc(sizeof(int), n);

	for (i = 0; i < n; i++)
	{
		scanf("%d", &a[i]);
	}



	for (i = 0; i < n; i++)
	{
		if (a1 > a[i])
			printf("%d ", a[i]);
	}
	return 0;
}
