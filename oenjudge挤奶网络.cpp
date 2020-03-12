#include<iostream>
#include<cstring>
 
/*
1.把每行字符串看作一个整体对行求next数组
2.将矩阵转置
3.进行操作1，注意这里的行是原来的列，列是原来的行，相当于求原来列的next数组
4.求出len－next[len]即最小不重复子串的长度作为子矩形的边长
*/
using namespace std;
#define MAX_ROW 10005
#define MAX_COL 80
 
char COW[MAX_ROW][MAX_COL];
char Transpose_COW[MAX_COL][MAX_ROW];
 
int Next_ROW[MAX_ROW];
int Next_COL[MAX_ROW];
 
int ROW, COL;
 
void Get_NextR()					//求行
{
	int j = -1, k = 0;
	Next_ROW[0] = -1;
	while (k < ROW)
	{
		if (j == -1 || !strcmp(COW[j], COW[k]))
		{
			j++;
			k++;
			Next_ROW[k] = j;
		}
		else
			j = Next_ROW[j];
	}
}
 
void Get_NextC()
{
	int j = -1, k = 0;
	Next_COL[0] = -1;
	while (k < COL)
	{
		if (j == -1 || !strcmp(Transpose_COW[j], Transpose_COW[k]))
		{
			j++;
			k++;
			Next_COL[k] = j;
		}
		else
			j = Next_COL[j];
	}
}
 
 
int main()
{
	while (cin >> ROW >> COL)
	{
		for (int i = 0; i < ROW; i++)
			cin >> COW[i];
		Get_NextR();
		for (int i = 0; i < ROW; i++)
			for (int j = 0; j < COL; j++)
				Transpose_COW[j][i] = COW[i][j];
		Get_NextC();
		
		int MIN_CoverNet = (ROW - Next_ROW[ROW])*(COL - Next_COL[COL]);
 
		cout << MIN_CoverNet << endl;
	}
	return 0;
}