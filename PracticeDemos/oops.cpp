// class ------------>       
// object ---------->  

// class className
// {
//     public:
//         statements;
// };


#include<iostream>
using namespace std;

class Student
{
    public:
        string name;
        int age;
        int rollnumber;
        int mark;

    void getData(string n, int a,int r,int m)
    {
        name = n;
        age = a;
        rollnumber = r;
        mark = m;
    }

    void printData()
    {
        cout<<name<<endl;
        cout<<age<<endl;
        cout<<rollnumber<<endl;
        cout<<mark<<endl;
    } 
};

int main()
{
    Student pratik,durgesh,kumar,rohit;
    pratik.getData("Pratik", 18, 101, 450);
    durgesh.getData("Durgesh", 118, 1101, 1450);
    kumar.getData("Kumar", 218, 2101, 2450);
    rohit.getData("rohit", 318, 3101, 3450);
    
    kumar.printData() ;
    // cout<< kumar.rollnumber;
}








