#include<stdio.h>
#include<stdlib.h>
#include<queue>
#include <iostream>
int root[50009]; 
int count[50009]={0};
int ans;
int find(int x)
{
	if(root[x]==x)
	{
		return x;
	}
	else{
		int t=find(root[x]);
		return t;
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
		ans--;
	}
}
main()
{
	int n,m;
	int ji=1;
	scanf("%d",&n);
	scanf("%d",&m);
	while(n!=0&&m!=0)
	{
	ans=n;
	for(int i=1;i<=n;i++)
	{
		root[i]=i;
	}
	int a,b;
	for(int i=1;i<=m;i++)
	{
		scanf("%d",&a);
		scanf("%d",&b);
		Union(a,b);
	}
	printf("Case %d: %d\n",ji,ans);
	scanf("%d",&n);
	scanf("%d",&m);
	ji++;
	}
	return 0;
}