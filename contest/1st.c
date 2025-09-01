#include<stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int A[n];
    for(int i=0;i<n;i++){
        scanf("%d",A+i);
    }
    int count=0;
    if(A[1]/2.0<A[0]) count++;
    for(int i=1;i<n-1;i++)
    {
        if((A[i+1]+A[i-1])/2.0<A[i]) count++;
    }
    if (A[n-2]/2.0 <A[n-1]) count++;
    printf("%d",count);
    return 0;
}