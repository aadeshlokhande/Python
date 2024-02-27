#include<stdio.h>
int main()
{
    int op,a,b,ans;
    for (int i = 1; i<=4; i++)
    {
        printf("enter equation saperate with space = ");
        scanf("%d%d%d",&a,&op,&b);
        
        switch(op)
        {
            case '+':
                ans = a + b;
                printf("%d + %d = %d\n",a,b,ans);
                break;
            
            case 45:
                ans = a - b;
                printf("%d - %d = %d\n",a,b,ans);
                break;
    
            case 42:
                ans = a * b;
                printf("%d * %d = %d\n",a,b,ans);
                break;
            
            case 47:
                ans = a / b;
                printf("%d / %d = %d\n",a,b,ans);
                break;
        }
    }
}