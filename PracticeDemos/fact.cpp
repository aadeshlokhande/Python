// #include<iostream>
// using namespace std;
// int fact(int n)
// {
//     if(n==1 || n==0)
//     {
//       return 1;
//     }
//     else
//     {
//         return (n*fact(n-1));
//     }
// }

// int main()
// {
//     int n ,f;
//     cout<<"Enter a number: \n";
//     cin>>n;
//     if(n<0)
//     {
//         cout<<"Invalid Input";
//     }
//     else
//     {
//         f= fact(n);
//         cout<<f;
//     }
//     return 0;
// }





// =================================================================
// 5! = 5x4x3x2x1
// 4! = 4x3x2x1

// 5! = 5x4!
// n! = n x (n-1)!---------------> 1

// 1! = 1
// 0! = 1


// #include <iostream>
// using namespace std;

// int factorial(int a )
// {
//    if(a==1 || a==0)
//    {
//        return 1;
//    }
//    else
//    {
//        return a * factorial(a-1);
//    }
// }

// int main()
// {
//     int num,ans;
//     cout<<"enter a number = ";
//     cin>>num;
//     ans=factorial(num);
//     cout<<ans;
// }

// ==============================================
// #include<iostream>
// using namespace std;


// void table(int a)
// {
//     int num = 1;
//     if(num<=10)
//     {
//         cout<<num*a<<endl;
//         ++num;
//         table(a);
//     } 
// }

// int main()
// {
//     int abc;
//     cout<<"enter a number = ";
//     cin>>abc;
//     table(abc);
// }
