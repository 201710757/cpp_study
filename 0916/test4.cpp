#include<iostream>
using namespace std;

int N;

long long tile[1000001];

int c1=0, c2=0;
void f(int n)
{
    tile[1] = 1; // 1
    tile[2] = 2; // 00 11
    tile[3] = 3; // 000(x) 001 100 111
    // tile[4] = 5; // 0011 0000 1001 1100 1111

    for(int i=4;i<=n;i++)
    {
        tile[i] = (tile[i-1] + tile[i-2]) % 15746;
    }
}

int main(void)
{
    cin >> N;

    f(N);

    cout<<tile[N]<<endl;
    
    return 0;
}