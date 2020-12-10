#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#define N 100

typedef struct InputData
{
    int a[N],n;
}InputData;

InputData getData()
{
    InputData I;
    //这里可以加一个while true来保证n<N
    printf("Enter n : ");
    scanf("%d",&I.n);
    printf("Enter numbers : ");
    int index = 0;
    while(true)
    {
        if(scanf("%d",&I.a[index]) == EOF || getchar() == '\n')
            break;
        index ++;
    }
    return I;
}

int count(int a[],int n,int x)
{
    int times = 0;
    for(int i = 0; i < n; i ++)
    {
        if(a[i] == x)
            times += 1;
    }
    return times;
}

int check(int a[],int n)
{
    int times = 0;
    int index;
    for(int i = 0; i < n; i ++)
    {
        if(i + 1 > n)
            break;
        //if(a[i] != a[i+1])
            //times += 1;
        //in this function (check) Must NOT compare between any elements in the array a. <-这有什么意义啊？？？
        index = a[i];
        if(index != a[i+1])
        {
            times += 1;
        }
    }
    return times;
}

bool exclusive(int a[],int n)
{
    if(check(a,n) == n)
        return true;
    else
        return false;
}

void call_count()
{
    InputData I = getData();
    int x;
    printf("Enter x : ");
    scanf("%d",&x);
    int times = count(I.a,I.n,x);
    printf("%d appears %d times\n",x,times);
}

void call_check()
{   
    InputData I = getData();
    printf("Total %d numbers\n",check(I.a,I.n));
}

void call_exclusive()
{
    InputData I = getData();
    if(exclusive(I.a,I.n))
        printf("series exclusive\n");
    else
    {
        printf("series NOT exclusive\n");
    }
}

int main()
{
    //call_count();
    //call_check();
    //call_exclusive();
    return 0;
}