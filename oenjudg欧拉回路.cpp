
#include<stdlib.h>
#include<queue>
#include <iostream>
int root[1005]; 
int du[1005];
int find(int x)
{
	if(root[x]==x)
	{
		return x;
	}
	else{
		root[x]=find(root[x]);
		return root[x];
	}
}
void Union(int x,int y)
{
	int rx,ry;
	rx=find(x);
	ry=find(y);
	if(rx!=ry)
	{
		root[ry]=rx;
	}
}
main()
{
	int n;
	scanf("%d",&n);
	while(n!=0)
	{
	int m;
	scanf("%d",&m);
	for(int i=1;i<=n;i++)
	{
		root[i]=i;
		du[i]=0;
	}
	int c,f;
	for(int i=1;i<=m;i++)
	{
		scanf("%d",&c);
		scanf("%d",&f);
		du[c]++;
		du[f]++;
		Union(c,f);
	}
	int ROOT=find(1);
	int sum=1;
	for(int i=1;i<=n;i++)
	{
		if(find(i)!=ROOT||du[i]%2!=0)
		{
			sum=0;
		}
	}
	printf("%d\n",sum);
	scanf("%d",&n);
	}
	return 0;
}