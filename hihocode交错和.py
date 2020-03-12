#include<iostream>
using namespace std;

#define ll long long int //��Ҫ��long long �����д��
const int mod = 1000000007;//��������ֵ������ȡģ
struct node{
    ll s, n;//s: ����λ����� n�����������ĸ���
};
node dp[21][20][400];//[����][���ĸ�����Ϊ��ͷ][��������λ�����]
int bits[21];//���һ�����ĸ�λ���͵��ߴ����0��20
ll base[21];//ÿһ��λ�Ļ�׼ ����ʮλ��=base[2]=10

//len��λ����, dig���׸�����, begin_zero��ʾ�����λ����ǰλ�Ƿ�ȫ��Ϊ0�� limit��ʾ��һλö���Ƿ������ƣ�bit[len-2]��9���� sum��Ҫ������ֺ� 
node dfs(int len, int dig, bool begin_zero, bool limit, int sum){
    node t;//��ų���Ϊ len�Ľ��
    t.s = 0, t.n = 0;
    //�����߽�ֵ 
    if (len <= 0 || len >= 20 || dig < 0 || dig > 9 || sum < -200 || sum >= 200)
        return t;
    //�������е�DP����������仯���� 
    if (!limit && dp[len][dig + (begin_zero ? 0 : 10)][sum + 200].n != -1)
        return dp[len][dig + (begin_zero ? 0 : 10)][sum + 200];
    //����ֻ��һλ���Ͳ���Ҫö����һλ�ˣ�ֱ�����۷��ؼ��� 
    if (len == 1){
        if (dig != sum)
            return t;
        t.n = 1, t.s = sum;
        return t;
    }
    //��ʼö����һλ������ 
    int end = limit ? bits[len - 2] : 9;//��һλ���ֵ����ֵ
    int newsum = dig - sum;
    node tmp;
    for (int j = 0; j < end + 1; j++)
    {
        if (begin_zero){//ǰ�涼��0���������ľ��ɵ�ǰλ���� j�Ƿ�Ϊ0
            tmp = dfs(len - 1, j, j == 0, limit && (j == end), sum);
        }
        else{//ǰ�治��ȫΪ0
            tmp = dfs(len - 1, j, false, limit && (j == end), newsum);
        }
        //��tmp��ֵ�ۼӵ�t��
        t.n += tmp.n;//���������ĸ���
        //�������������ĳ���Ϊ len ��data[len]�������ĺͣ� tmp �ǳ���Ϊ i-1��data[len-1]�������ĺ�
        //ÿһ���� data[len] = dig * base[len] + data[len-1]  �ҹ���n��
        //t.s = t.s + tmp.n * (dig * base[len]) + tmp.s ���� %mod �͵õ�����Ľ��
        t.s = ((t.s + tmp.s) % mod + ((tmp.n * dig) % mod * base[len]) % mod) % mod;
    }
        //������Ϊlen������dig��ͷ�ģ���λ��Ϊsum �����н����������ɣ��Ž�����д洢
    if (!limit) 
        dp[len][dig + (begin_zero ? 0 : 10)][sum + 200] = t;
        //dig + (begin_zero ? 0 : 10) ������������״̬����1. ǰ����Ϊ0��2. ǰ��������������
    return t;
}

int solve(ll n, int s){
    if (n <= 0)
        return 0;
    int l = 0;
    for (int i = 0; i < 21; i++)
        bits[i] = 0;
    //��n��ÿһλ�ӵ͵��߷ŵ� bits[0]��bits[l] ��
    while (n){
        bits[l++] = n % 10;
        n /= 10;
    }
    //��l+1��ʼ����n�ĳ��ȴ�1�����ҵ�l+1λ����Ϊ0
    return  dfs(l + 1, 0, true, true, s).s;
}

int main(){
    ll l, r, s;
    node t;
    t.n = -1;
    t.s = 0;
    for (int i = 0; i < 21; i++)//����
        for (int j = 0; j < 20; j++)//��iλ��ȡֵ,ȡ��20�ǰ�[0,9]��Ϊ����ǰ��ȫΪ0��״̬�洢�ռ䣬[10��19]��Ϊǰ�������������Ĵ洢�ռ�
            for (int k = 0; k < 400; k++)// i��0 ����λ�ϵĽ���� + 200, ���ڰ� k�ķ�Χ��[-200,200] ƽ�Ƶ���[0,400]
                dp[i][j][k] = t;
    base[1] = 1;
    for (int i = 2; i < 21; i++)//base ����Ϊ��׼�� ������λ����Ҫ *10, ��λ����Ҫ*100
        base[i] = base[i - 1] * 10 % mod;
    cin >> l >> r >> s;
    cout << (solve(r, s) - solve(l - 1, s) + mod) % mod << endl;
    return 0;
}