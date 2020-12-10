//不知道会不会检测有空格的情况 建议自己加上
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//这里是Python/Python Homework/hw1q4.py C语言的实现
/*
#define N 100
bool checkStart(int a[],int currentIndex,int Length,int sumfornow,int x)
{
    if(a[currentIndex] + sumfornow > x)
        return false;
    if(a[currentIndex] + sumfornow == x)
        return true;
    else
    {
        if(currentIndex + 1 == Length)
            return false;
        return checkStart(a ,currentIndex + 1, Length, sumfornow + a[currentIndex], x);
    }
    return false;
}

int main()
{
    int a[N],x;
    printf("Enter numbers : ");
    int index = 0;
    while(true)
    {
        int status = scanf("%d",&a[index]);
        if(status == EOF || getchar() == '\n' || a[index] == -1)
        {
            break;
        }
        index ++;
    }
    printf("Enter x : ");
    scanf("%d",&x);
    int Length = sizeof(a)/sizeof(int);
    bool flag = false;
    for(int i = 0; i < Length; i ++)
    {
        if(checkStart(a,i,Length,0,x))
        {
            flag = true;
            printf("we get %d starting at position %d\n",x,i+1);
            break;
        }
    }

    if(!flag)
        printf("can not get %d\n",x);
    return 0;
}


bool explore(int a[],int x)
{
    return false;
}
上面的方法有一个确定的上限 （100） 不符合题目要求
*/

//我觉得这个写的好拖沓！ 希望有人能改进一下

bool checkStart(int a[],int currentIndex,int sumfornow,int x)
{
    
    if(a[currentIndex] + sumfornow > x)
        return false;
    if(a[currentIndex] + sumfornow == x)
        return true;
    else
    {
        if(a[currentIndex + 1] == EOF)
            return false;
        return checkStart(a ,currentIndex + 1, sumfornow + a[currentIndex], x);
    }
    return false;
}

bool explore(int a[],int x)
{
    bool flag = false;
    for(int i = 0; i < sizeof(a); i ++)
    {
        if(a[i] == EOF)
            break;
        if(checkStart(a,i,0,x))
        {
            printf("Can find a start at pos %d \n",i+1);
            flag = true;
            return true;
        }
    }
    if(flag == false)
        return false;
}

int main()
{
    int *a = (int*)(malloc(sizeof(int)));
    printf("Enter numbers : ");
    int index = 0;
    while(true)
    {
        int status = scanf("%d",a+index);
        if(status == EOF || getchar() == '\n')
        {
            break;
        }
        index ++;
        a = realloc(a,sizeof(int));
    }
    printf("Enter x : ");
    int x;
    scanf("%d",&x);

    if(!explore(a,x))
        printf("Can not find a start");
}