def process(a):
    result=0;
    for i in a:
        result^=(1<<(i-1));
    return result
def DP():
    minx=-1e9
    n,m=map(int, raw_input().split())
    dp = []
    lim=(1<<m)
    for i in range(n+6):
        dp.append([0] * (lim+10))
    for i in range(n+6):
        for j in range(lim):
            dp[i][j]=minx
####################################################
    much=[]
    state=[]
    for i in range(n):
        a,b=map(int, raw_input().split())
        much.append(a)
        one_state=[]*b
        one_state=map(int, raw_input().split())
        state.append(process(one_state))
#####################################################
    dp[0][0]=0
    for i in range(1,n+1):
        for j in range(lim):
            dp[i][j]=dp[i-1][j]
            dp[i][j]=max(dp[i-1][j],dp[i-1][j^state[i-1]]+much[i-1])
    return dp[n][lim-1]
t=input()
for i in range(t):
    print(DP())
