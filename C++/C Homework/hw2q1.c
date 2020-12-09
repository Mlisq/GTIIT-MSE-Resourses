#include <stdio.h>
#define N 100

int count(int a[],int n,int x)
{
    int times = 0;
    for(int i = 0; i < n; i ++)
    {
        if(a[i] == x)
            times ++;
    }
    return times;
}

int cheak(int a[],int n)
{
    int times = 0;
    for(int i = 0; i < n; i ++)
    {
        if(i + 1 == n)
            break;
        if(a[i] != a[i+1])
            times += 1;
    }
    return times;
}

int main()
{
    int a[] = {1,2,3,4,5,6};
    printf("%d",cheak(a,6));
    return 0;
}