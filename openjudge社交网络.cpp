#include<stdio.h>
#include <iostream>
using namespace std;
int k[307];
char c[307][307];
int n;
void bfs(int t)
{
	if(k[t]==0)
	{
		k[t]=1;
		for(int i=0;i<n;i++)
		{
			if(i!=t)
			{
				if(c[t][i]=='1')
				{
					bfs(i);
				}
			}
		}
	}
	else{
		return;
	}
}
main()
{
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%s",c[i]);
	}
	for(int i=0;i<n;i++)
	{
		for(int s=0;s<n;s++)
		{
			k[s]=0;
		}
		bfs(i);
		for(int q=0;q<n;q++)
		{
			if(k[q]==1)
			{
				c[i][q]='1';
			}
		}
	}
	for(int u=0;u<n;u++)
	{
		printf("%s\n",c[u]);
	}
} 