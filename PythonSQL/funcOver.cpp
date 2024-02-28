// polymorphism

// compile time
//     function overloading
// run time 
//     function overriding


// ====================================
#include<iostream>
using namespace std;

void calc(int a,int b)
{
    cout<<a + b<<endl;
}

void calc(double a,int b)
{
    cout<<a-b<<endl;
}

void calc(int a,double b)
{
    cout<<a*b<<endl;
}

void calc(double a,double b)
{
    cout<<a / b<<endl;
}

void calc(int a)
{
    cout<<a*a;
}

void calc(double a)
{
    cout<<a*a*a;
}

int main()
{
    calc(6.0);
}