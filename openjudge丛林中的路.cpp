#include<stdio.h>
#include<stdlib.h>
#include<queue>
#include <iostream>
int root[300]; 
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
using namespace std;
struct edge{
	int begin;
	int end;
	int weight;
}; 
struct cmp1//����ȽϽṹ
{
      bool operator ()(struct edge&a,struct edge&b)
    {
          return a.weight>b.weight;//��Сֵ����
 	}
};
main()
{
	int n;
	scanf("%d",&n);
	while(n!=0)
	{
		for(int i=0;i<30;i++)
	{
		root[i]=i;
	}
	priority_queue<struct edge,vector<struct edge>,cmp1>q;
	char be;/*��ʼ*/
	char en;/*�յ�*/
	int we;/*Ȩֵ*/
	int du; 
	edge r;
	for(int i=0;i<n-1;i++)
	{
		cin>>be>>du;
		for(int j=0;j<du;j++)
		{
			cin>>en>>we;
			r.begin=be;
			r.end=en;
			r.weight=we;
			q.push(r);	
		}
	} /*����Ϊ��ͼ����*/
	int sum=0;
	while(q.empty()!=1)
	{
		if(find(q.top().begin-'A')!=find(q.top().end-'A'))
		{
			sum=sum+q.top().weight;
			Union(q.top().begin-'A',q.top().end-'A');
		}
		q.pop();
	}
	printf("%d\n",sum);
	scanf("%d",&n);
	}
	return 0;
}