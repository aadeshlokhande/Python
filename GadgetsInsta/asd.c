#include <stdio.h>
int main()
{
    int i,k;
    char op;
    double first,second;
    printf("\tRohit Sawaikar \n");
    
    for(int i = 1; i<=4 ; i++)
    {
        printf("enter an operand (+,-,*,/) :");
        scanf(" %c",&op);
        
        printf("enter two operands:");
        scanf("%lf %lf",&first,&second);
    
            switch(op)
        {
            case '+':
                printf("%.1lf + %.1lf = %.1lf\n", first, second, first + second);
            break;
            
            case '-':
                printf("%.1lf - %.1lf = %.1lf\n", first, second, first - second);
            break;
            
            case '*':
                printf("%.1lf * %.1lf = %.1lf\n", first, second, first * second);
            break;
            
            case '/':
                printf("%.1lf / %.1lf = %.1lf\n",first, second, first / second);
            break;
            
            
            default:
            printf("error ! operator is not correct\n");
        
            
        }
    }
    
 return 0;   
}