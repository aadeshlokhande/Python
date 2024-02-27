// heirarchical inheritance 

#include<iostream>
using namespace std;

class Parent
{
    public:
        void ParentQuality()
        {
            cout<<"singing"<<endl;
        }
};

class Child1 : public Parent
{
    public:
        void Child1Quality()
        {
            cout<<"Dance"<<endl;
        }
};

class Child2 : public Parent
{
    public:
        void Child2Quality()
        {
            cout<<"Poetry"<<endl;
        }
};

int main()
{
    // Parent kishanlal;
    // kishanlal.ParentQuality();
    
    // Child1 pratik;
    // pratik.Child1Quality();
    // pratik.ParentQuality();
    
    Child2 rohit;
    rohit.Child2Quality();
    rohit.ParentQuality();
}


// animal 
// employee
// add - multi 










