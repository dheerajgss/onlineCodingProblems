#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	while(t)
	{
		int n, temp, count;
		scanf("%d",&n);
		temp = (n-1)/4;
		if(temp % 2 == 0)
		{
			count = n % 4;
			switch(count)
			{
				case 1: printf("thumb\n");
						break;
				case 2: printf("index finger\n");
						break;
				case 3: printf("middle finger\n");
						break;
				case 0: printf("ring finger\n");
						break;
			}
		}
		else if(temp % 2 == 1)
		{
			count = n % 4;
			switch(count)
			{
				case 1: printf("little finger\n");
						break;
				case 2: printf("ring finger\n");
						break;
				case 3: printf("middle finger\n");
						break;
				case 0: printf("index finger\n");
						break;
			}
		}
		t--;
	}
}
