// function overriding

// #include<iostream>
// using namespace std;

// class Base
// {
//     public:
//         void info()
//         {
//             cout<<"I am a base class\n";
//         }
// };

// class Derive : public Base
// {
//     public:
//         void info()
//         {
//             cout<<"I am a derive class\n";
//         }
// };

// int main()
// {
//     Derive obj;
//     obj.info();
// }


// =============================


// #include<iostream>
// using namespace std;

// class Employee
// {
//     public:
//     int Eid;
//     string name;
//         void getData(int E, string n)
//         {
//                 Eid = E;
//                 name = n;
//         }
//         void printData()
//         {
//             cout<<"Eid = "<<Eid<<endl; 
//             cout<<"Name = "<<name<<endl; 
//             cout<<"leaves = "<<8<<endl; 
//         }
// };

// class Programmer : public Employee
// {
//     public:
//         void printData()
//         {
//             cout<<"Eid = "<<Eid<<endl; 
//             cout<<"Name = "<<name<<endl; 
//             cout<<"leaves = "<<10<<endl; 
//         }
// };

// int main()
// {
//     // Employee sanjana;
//     // sanjana.getData(101, "Sanjana");
//     // sanjana.printData();

//     Programmer sanjana;
//     sanjana.getData(101, "Sanjana");
//     sanjana.printData();
// }
