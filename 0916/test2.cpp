#include<iostream>
using namespace std;

int N;

int fibo[41+1];

int c1=0, c2=0;
void f2(int n)
{
    fibo[1] = 1;
    fibo[2] = 1;

    for(int i=3;i<n;i++)
    {
        fibo[i] = fibo[i-1] + fibo[i-2];
        c2 += 1;
    }
}

int f1(int n)
{
    if (n ==1 || n==2) 
    {
        c1 += 1;
        return 1;
    }
    return f1(n-1) + f1(n-2);
}
int main(void)
{
    cin >> N;

    int o=f1(N);
    f2(N);

    cout<<c1<<' '<<c2<<endl;
    
    return 0;
}