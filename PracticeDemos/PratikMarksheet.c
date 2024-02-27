// Marksheet

#include<stdio.h>
int main()
// marks[20][6] = {
//     {54,43,76,35,76,77},
//     {55,75,33,87,34,87},
//     {45,87,46,35,23,54},
//     .
//     .
// };
{
    int press,Marathi, Hindi, English, History, maths, science,rollNo, marks[20][6] =
    {
        {14,65,12,16,15,31},
        {25,89,23,26,25,72},
        {35,76,33,36,35,63},
        {43,99,43,46,45,84},
        {55,43,53,56,55,35},
        {65,62,63,66,65,13},
        {75,46,73,76,75,36},
        {85,61,83,86,45,57},
        {95,13,93,96,35,78},
        {39,87,33,36,25,37},
        {48,46,23,73,15,79},
        {47,36,29,79,25,78},
        {46,46,28,78,35,76},
        {45,36,27,77,45,73},
        {44,96,26,76,55,16},
        {43,36,25,75,65,26},
        {42,76,24,74,75,36},
        {41,84,23,73,85,46},
        {35,36,22,72,95,56},
        {95,46,21,71,35,66},
    };

   // int ;
     printf("Press\n 1 for any student one subjet mark\n 2 for .any one student result\n 3 for all sttudent result\n = ");
        scanf("%d",&press);

    for (int i = 0; i <= 3; i++)
    {
        if(press==1)
        // press 1 : marks
        //     enter roll number = 1
        //     press 0 : marathi
        //     press 1 : hindi
        //     press 2 : English
        //     .
        //     .
        //     enter a sub code = 2
        //     marks = 33
        { int code;
            printf("Enter a roll No. =");
            scanf("%d",&rollNo);
            
            if (rollNo==0)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[0][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[0][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[0][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[0][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[0][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[0][5]);
            }
            }
 //________________________________________________________________________________________________
            if (rollNo==1)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[1][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[1][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[1][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[1][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[1][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[1][5]);
            }
            }
        //_______________________________________________________________________________________________________
            if (rollNo==2)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[2][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[2][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[2][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[2][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[2][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[2][5]);
            }
            }
    //________________________________________________________________________________
            if (rollNo==3)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[3][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[3][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[3][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[3][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[3][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[3][5]);
            }
            }

//______________________________________________________________________________________________
            if (rollNo==4)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[4][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[4][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[4][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[4][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[4][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[4][5]);
            }
            }
            //_____________________________________________________________________
            if (rollNo==5)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[5][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[5][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[5][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[5][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[5][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[5][5]);
            }
            }
            //_________________________________________________________________________
            if (rollNo==6)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[6][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[6][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[6][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[6][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[6][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[6][5]);
            }
            }
            //________________________________________________________________________________
            if (rollNo==7)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[7][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[7][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[7][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[7][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[7][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[7][5]);
            }
            }
            //_______________________________________________________________________________________
            if (rollNo==8)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[8][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[8][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[8][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[8][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[8][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[8][5]);
            }
            }
            //_________________________________________________________________________________________
            if (rollNo==9)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[9][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[9][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[9][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[9][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[9][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[9][5]);
            }
            }
            //____________________________________________________________________________________________________
            if (rollNo==10)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[10][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[10][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[10][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[10][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[10][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[10][5]);
            }
            }
            //________________________________________________________________________________________________
            if (rollNo==11)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[11][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[11][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[11][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[11][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[11][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[11][5]);
            }
            }
            //__________________________________________________________________________________________________
            if (rollNo==12)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[12][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[12][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[12][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[12][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[12][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[12][5]);
            }
            }
            //________________________________________________________________________________________
            if (rollNo==13)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[13][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[13][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[13][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[13][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[13][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[13][5]);
            }
            }
            //_________________________________________________________________________________________________________
            if (rollNo==14)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[14][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[14][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[14][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[14][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[14][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[14][5]);
            }
            }
            //_________________________________________________________________________________
            if (rollNo==15)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[15][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[15][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[15][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[15][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[15][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[15][5]);
            }
            }
            //____________________________________________________________________________________
            if (rollNo==16)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[16][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[16][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[16][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[16][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[16][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[16][5]);
            }
            }
            //__________________________________________________________________________________________
            if (rollNo==17)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[17][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[17][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[17][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[17][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[17][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[17][5]);
            }
            }
            //__________________________________________________________________________________________________
            if (rollNo==18)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[18][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[18][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[18][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[18][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[18][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[18][5]);
            }
            }
            //_________________________________________________________________________________________________________
            if (rollNo==19)
            {
            printf("Enter a subjet code \n1 for Marathi\n2 for Hindi\n3 for English\n4 for history\n5 for science\n6 for Maths =\n");
            scanf("%d",&code);
            if(code==1)
            {
                printf("Marathi = %d",marks[19][0]);
            }
            else if(code==2)
            {
                printf("Hindi = %d",marks[19][1]);
            }
            else if(code==3)
            {
                printf("English = %d",marks[19][2]);
            }
            else if(code==4)
            {
                printf("History = %d",marks[19][3]);
            }
            else if(code==5)
            {
                printf("Science = %d",marks[19][4]);
            }
            else if(code==6)
            {
                printf("Maths = %d",marks[19][5]);
            }
            }
  
            break;
        }

        else if(press==2)
        
        // press 2 : result
        //     enter roll number = 1
        //     marathi = 
        //     hindi = 
        //     english = 
        //     .
        //     .
        //     .
        {
            printf("Enter a roll No. =");
            scanf("%d",&rollNo);
            printf("rollNO  \tmar\thin\teng\this\tsci\tmaths\n");
            if (rollNo==0)
            {
            printf("rollNo 0\t%d",marks[0][0]);
            printf("\t%d",marks[0][1]);
            printf("\t%d",marks[0][2]);
            printf("\t%d",marks[0][3]);
            printf("\t%d",marks[0][4]);
            printf("\t%d",marks[0][5]); 
            }
            else if (rollNo==1)
            {
            printf("\nrollNo 1\t%d",marks[1][0]);
            printf("\t%d",marks[1][1]);
            printf("\t%d",marks[1][2]);
            printf("\t%d",marks[1][3]);
            printf("\t%d",marks[1][4]);
            printf("\t%d",marks[1][5]);
            }
            else if(rollNo==2)
            {
            printf("\nrollNo 2\t%d",marks[2][0]);
            printf("\t%d",marks[2][1]);
            printf("\t%d",marks[2][2]);
            printf("\t%d",marks[2][3]);
            printf("\t%d",marks[2][4]);
            printf("\t%d",marks[2][5]);         
            }
            else if(rollNo==3)
            {
            printf("\nrollNo 3\t%d",marks[3][0]);
            printf("\t%d",marks[3][1]);
            printf("\t%d",marks[3][2]);
            printf("\t%d",marks[3][3]);
            printf("\t%d",marks[3][4]);
            printf("\t%d",marks[3][5]);
            }
            else if(rollNo==4)
            {            
            printf("\nrollNo 4\t%d",marks[4][0]);
            printf("\t%d",marks[4][1]);
            printf("\t%d",marks[4][2]);
            printf("\t%d",marks[4][3]);
            printf("\t%d",marks[4][4]);
            printf("\t%d",marks[4][5]);
            }
            else if (rollNo==5)
            {
            printf("\nrollNo 5\t%d",marks[5][0]);
            printf("\t%d",marks[5][1]);
            printf("\t%d",marks[5][2]);
            printf("\t%d",marks[5][3]);
            printf("\t%d",marks[5][4]);
            printf("\t%d",marks[5][5]);
            }
            else if(rollNo==6)
            {
            printf("\nrollNo 6\t%d",marks[6][0]);
            printf("\t%d",marks[6][1]);
            printf("\t%d",marks[6][2]);
            printf("\t%d",marks[6][3]);
            printf("\t%d",marks[6][4]);
            printf("\t%d",marks[6][5]);
            }
            else if(rollNo==7)
            {
            printf("\nrollNo 7\t%d",marks[7][0]);
            printf("\t%d",marks[7][1]);
            printf("\t%d",marks[7][2]);
            printf("\t%d",marks[7][3]);
            printf("\t%d",marks[7][4]);
            printf("\t%d",marks[7][5]);
            }
            else if(rollNo==8)
            { 
            printf("\nrollNo 8\t%d",marks[8][0]);
            printf("\t%d",marks[8][1]);
            printf("\t%d",marks[8][2]);
            printf("\t%d",marks[8][3]);
            printf("\t%d",marks[8][4]);
            printf("\t%d",marks[8][5]);
            }
            else if(rollNo==9)
            {
            printf("\nrollNo 9\t%d",marks[9][0]);
            printf("\t%d",marks[9][1]);
            printf("\t%d",marks[9][2]);
            printf("\t%d",marks[9][3]);
            printf("\t%d",marks[9][4]);
            printf("\t%d",marks[9][5]);
            }
            else if(rollNo==10)
            {printf("\nrollNo 10\t%d",marks[10][0]);
            printf("\t%d",marks[10][1]);
            printf("\t%d",marks[10][2]);
            printf("\t%d",marks[10][3]);
            printf("\t%d",marks[10][4]);
            printf("\t%d",marks[10][5]);
            }
            else if(rollNo==11)
            {
            printf("\nrollNo 11\t%d",marks[11][0]);
            printf("\t%d",marks[11][1]);
            printf("\t%d",marks[11][2]);
            printf("\t%d",marks[11][3]);
            printf("\t%d",marks[11][4]);
            printf("\t%d",marks[11][5]);
            }
            else if(rollNo==12)
            {
            printf("\nrollNo 12\t%d",marks[12][0]);
            printf("\t%d",marks[12][1]);
            printf("\t%d",marks[12][2]);
            printf("\t%d",marks[12][3]);
            printf("\t%d",marks[12][4]);
            printf("\t%d",marks[12][5]);
            }
            else if(rollNo==13)
            {
            printf("\nrollNo 13\t%d",marks[13][0]);
            printf("\t%d",marks[13][1]);
            printf("\t%d",marks[13][2]);
            printf("\t%d",marks[13][3]);
            printf("\t%d",marks[13][4]);
            printf("\t%d",marks[13][5]);
            }
            else if(rollNo==14)
            {
            printf("\nrollNo 14\t%d",marks[14][0]);
            printf("\t%d",marks[14][1]);
            printf("\t%d",marks[14][2]);
            printf("\t%d",marks[14][3]);
            printf("\t%d",marks[14][4]);
            printf("\t%d",marks[14][5]);
            }
            else if(rollNo==15)
            {
             printf("\nrollNo 15\t%d",marks[15][0]);
             printf("\t%d",marks[15][1]);
             printf("\t%d",marks[15][2]);
            printf("\t%d",marks[15][3]);
            printf("\t%d",marks[15][4]);
            printf("\t%d",marks[15][5]);
            }
            else if(rollNo==16)
            {
            printf("\nrollNo 16\t%d",marks[16][0]);
            printf("\t%d",marks[16][1]);
            printf("\t%d",marks[16][2]);
            printf("\t%d",marks[16][3]);
            printf("\t%d",marks[16][4]);
            printf("\t%d",marks[16][5]);
            }
            else if(rollNo==17)
            {
            printf("\nrollNo 17\t%d",marks[17][0]);
            printf("\t%d",marks[17][1]);
            printf("\t%d",marks[17][2]);
            printf("\t%d",marks[17][3]);
            printf("\t%d",marks[17][4]);
            printf("\t%d",marks[17][5]);
            }
            else if(rollNo==18)
            {
            printf("\nrollNo 18\t%d",marks[18][0]);
            printf("\t%d",marks[18][1]);
            printf("\t%d",marks[18][2]);
            printf("\t%d",marks[18][3]);
            printf("\t%d",marks[18][4]);
            printf("\t%d",marks[18][5]);
            }
            else if(rollNo==19)
            {
            printf("\nrollNo 19\t%d",marks[19][0]);
            printf("\t%d",marks[19][1]);
            printf("\t%d",marks[19][2]);
            printf("\t%d",marks[19][3]);
            printf("\t%d",marks[19][4]);
            printf("\t%d",marks[19][5]);   
            }
            else 
            {
                printf("You enter invalid rollNo");
            }
            break;
        }
        else if(press==3)
        // press 3 : whole result
        //                 mar     hin     eng     his     sci     math 
        // roll No 0       12      78      78      56      45      34
        // roll No 1       12      78      78      56      45      34
        // roll No 2       12      78      78      56      45      34
        // roll No 3       12      78      78      56      45      34
        // roll No 4       12      78      78      56      45      34
        // roll No 5       12      78      78      56      45      34
        // .
        // .
        // .
        // roll No 19       12      78      78      56      45      34
        {
            printf("rollNO  \tmar\thin\teng\this\tsci\tmaths\n");
            printf("rollNo 0\t%d",marks[0][0]);
            printf("\t%d",marks[0][1]);
            printf("\t%d",marks[0][2]);
            printf("\t%d",marks[0][3]);
            printf("\t%d",marks[0][4]);
            printf("\t%d",marks[0][5]);
            
            printf("\nrollNo 1\t%d",marks[1][0]);
            printf("\t%d",marks[1][1]);
            printf("\t%d",marks[1][2]);
            printf("\t%d",marks[1][3]);
            printf("\t%d",marks[1][4]);
            printf("\t%d",marks[1][5]);
           
            printf("\nrollNo 2\t%d",marks[2][0]);
            printf("\t%d",marks[2][1]);
            printf("\t%d",marks[2][2]);
            printf("\t%d",marks[2][3]);
            printf("\t%d",marks[2][4]);
            printf("\t%d",marks[2][5]);
            
            printf("\nrollNo 3\t%d",marks[3][0]);
            printf("\t%d",marks[3][1]);
            printf("\t%d",marks[3][2]);
            printf("\t%d",marks[3][3]);
            printf("\t%d",marks[3][4]);
            printf("\t%d",marks[3][5]);
            
            printf("\nrollNo 4\t%d",marks[4][0]);
            printf("\t%d",marks[4][1]);
            printf("\t%d",marks[4][2]);
            printf("\t%d",marks[4][3]);
            printf("\t%d",marks[4][4]);
            printf("\t%d",marks[4][5]);
            
            printf("\nrollNo 5\t%d",marks[5][0]);
            printf("\t%d",marks[5][1]);
            printf("\t%d",marks[5][2]);
            printf("\t%d",marks[5][3]);
            printf("\t%d",marks[5][4]);
            printf("\t%d",marks[5][5]);
            
            printf("\nrollNo 6\t%d",marks[6][0]);
            printf("\t%d",marks[6][1]);
            printf("\t%d",marks[6][2]);
            printf("\t%d",marks[6][3]);
            printf("\t%d",marks[6][4]);
            printf("\t%d",marks[6][5]);
            
            printf("\nrollNo 7\t%d",marks[7][0]);
            printf("\t%d",marks[7][1]);
            printf("\t%d",marks[7][2]);
            printf("\t%d",marks[7][3]);
            printf("\t%d",marks[7][4]);
            printf("\t%d",marks[7][5]);
            
            printf("\nrollNo 8\t%d",marks[8][0]);
            printf("\t%d",marks[8][1]);
            printf("\t%d",marks[8][2]);
            printf("\t%d",marks[8][3]);
            printf("\t%d",marks[8][4]);
            printf("\t%d",marks[8][5]);
            
            printf("\nrollNo 9\t%d",marks[9][0]);
            printf("\t%d",marks[9][1]);
            printf("\t%d",marks[9][2]);
            printf("\t%d",marks[9][3]);
            printf("\t%d",marks[9][4]);
            printf("\t%d",marks[9][5]);
            
            printf("\nrollNo 10\t%d",marks[10][0]);
            printf("\t%d",marks[10][1]);
            printf("\t%d",marks[10][2]);
            printf("\t%d",marks[10][3]);
            printf("\t%d",marks[10][4]);
            printf("\t%d",marks[10][5]);
            
            printf("\nrollNo 11\t%d",marks[11][0]);
            printf("\t%d",marks[11][1]);
            printf("\t%d",marks[11][2]);
            printf("\t%d",marks[11][3]);
            printf("\t%d",marks[11][4]);
            printf("\t%d",marks[11][5]);
            
            printf("\nrollNo 12\t%d",marks[12][0]);
            printf("\t%d",marks[12][1]);
            printf("\t%d",marks[12][2]);
            printf("\t%d",marks[12][3]);
            printf("\t%d",marks[12][4]);
            printf("\t%d",marks[12][5]);
            
            printf("\nrollNo 13\t%d",marks[13][0]);
            printf("\t%d",marks[13][1]);
            printf("\t%d",marks[13][2]);
            printf("\t%d",marks[13][3]);
            printf("\t%d",marks[13][4]);
            printf("\t%d",marks[13][5]);
            
            printf("\nrollNo 14\t%d",marks[14][0]);
            printf("\t%d",marks[14][1]);
            printf("\t%d",marks[14][2]);
            printf("\t%d",marks[14][3]);
            printf("\t%d",marks[14][4]);
            printf("\t%d",marks[14][5]);
            
            printf("\nrollNo 15\t%d",marks[15][0]);
            printf("\t%d",marks[15][1]);
            printf("\t%d",marks[15][2]);
            printf("\t%d",marks[15][3]);
            printf("\t%d",marks[15][4]);
            printf("\t%d",marks[15][5]);
            
            printf("\nrollNo 16\t%d",marks[16][0]);
            printf("\t%d",marks[16][1]);
            printf("\t%d",marks[16][2]);
            printf("\t%d",marks[16][3]);
            printf("\t%d",marks[16][4]);
            printf("\t%d",marks[16][5]);
            
            printf("\nrollNo 17\t%d",marks[17][0]);
            printf("\t%d",marks[17][1]);
            printf("\t%d",marks[17][2]);
            printf("\t%d",marks[17][3]);
            printf("\t%d",marks[17][4]);
            printf("\t%d",marks[17][5]);
            
            printf("\nrollNo 18\t%d",marks[18][0]);
            printf("\t%d",marks[18][1]);
            printf("\t%d",marks[18][2]);
            printf("\t%d",marks[18][3]);
            printf("\t%d",marks[18][4]);
            printf("\t%d",marks[18][5]);
            
            printf("\nrollNo 19\t%d",marks[19][0]);
            printf("\t%d",marks[19][1]);
            printf("\t%d",marks[19][2]);
            printf("\t%d",marks[19][3]);
            printf("\t%d",marks[19][4]);
            printf("\t%d",marks[19][5]);

            break;
        }     
        else
        {
            printf("You press Invalid number");
            break;
        }
    }   
}