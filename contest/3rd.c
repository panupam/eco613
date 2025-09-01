#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int i,a[n],z=-1;
    for(i=0;i<n;i++)
    {
        scanf("%d",a+i);
    }
    for(i=0;i<n;i++)
    {
        int count=0;
        for(int j=0;j<n;j++)if(a[j]%a[i]==0) count++;
        if (count==a[i])
        {
            if(z<a[i])z=a[i];
        }
        
        
    }
    printf("%d",z);
    return 0;
}