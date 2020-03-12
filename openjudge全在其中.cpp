#include <stdio.h>
int main()
{
    char ori[100010],tra[100010];
    int i,j;
    while(scanf("%s%s",ori,tra) != EOF)
    {
        for(i = 0,j = 0;ori[i] != '\0' && tra[j] != '\0';)
        {
            while(ori[i] != tra[j] && tra[j] != '\0') j++;
            if(tra[j] != '\0') {i++;j++;}
        }
        ori[i] == '\0'? printf("Yes\n") : printf("No\n");
    }
    return 0;
}