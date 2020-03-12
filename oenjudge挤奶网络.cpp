#include<iostream>
#include<cstring>
 
/*
1.��ÿ���ַ�������һ�����������next����
2.������ת��
3.���в���1��ע�����������ԭ�����У�����ԭ�����У��൱����ԭ���е�next����
4.���len��next[len]����С���ظ��Ӵ��ĳ�����Ϊ�Ӿ��εı߳�
*/
using namespace std;
#define MAX_ROW 10005
#define MAX_COL 80
 
char COW[MAX_ROW][MAX_COL];
char Transpose_COW[MAX_COL][MAX_ROW];
 
int Next_ROW[MAX_ROW];
int Next_COL[MAX_ROW];
 
int ROW, COL;
 
void Get_NextR()					//����
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