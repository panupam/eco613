#include<stdio.h>
int main()
{
    int a,b,c,sum=0;
    scanf("%d%d%d",&a,&b,&c);
    sum+=a/3;
    a=a%3;
    sum+=b/3;
    b=b%3;
    sum+=c/3;
    c=c/3;
    if( a>0& b>0 & c>0)
    {
        if(a>1&b>1 & c>1)
        {
            sum+=2;
        }else{
            sum+=1;
        }
    }
    printf("%d",sum);
    return 0;
}