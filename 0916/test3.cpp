#include<iostream>
using namespace std;


int save[21][21][21];

int f(int a, int b, int c)
{

    if (a<=0 || b<=0 || c<=0) return 1;
    else if (a>20 || b>20 || c>20) return f(20, 20, 20);
    else if (a<b && b<c)
    {
        // known
        if (save[a][b][c] != 0) 
            return save[a][b][c];
        // unknown
        else 
        {
            save[a][b][c] = f(a,b,c-1) + f(a,b-1,c-1) - f(a,b-1,c);
            return save[a][b][c];
        }

    }
    else
    {
        // known
        if (save[a][b][c] != 0) 
            return save[a][b][c];
        // unknown
        else 
        {
            save[a][b][c] = f(a-1,b,c) + f(a-1,b-1,c) + f(a-1,b,c-1) - f(a-1,b-1,c-1);
            return save[a][b][c];
        }
    }
    
}

int main(void)
{
    int a=0, b=0, c=0;
    while (true)
    {
        cin >>a>>b>>c;

        if(a==-1 && b==-1 && c==-1) break;
        cout << "w(" <<a<< ", " <<b<< ", " <<c<< ") = " << f(a,b,c) << endl;
    }
    
    return 0;
}