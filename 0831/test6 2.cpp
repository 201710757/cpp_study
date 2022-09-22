#include<iostream>
#define MAX 9
using namespace std;


int N;
int res;

int board [MAX][MAX] = {0,};

void axisX()
{
    int vis[MAX] = {0,};

}
void axisY()
{
    int vis[MAX] = {0,};
}
void axis9()
{
    int vis[MAX] = {0,};
}

void dfs(int pos)
{
    if(pos == N)
    {
        res += 1;
        return;
    }
    for(int i=0;i<N;i++)
    {
        // arr[pos] = i;
        bool _flag = true;
        for(int j=0;j<pos;j++)
        {
            // if(arr[pos] == arr[j] || pos-j == abs(arr[pos] - arr[j])) _flag = false;
        }
        if(_flag) dfs(pos + 1);
    }
}
int main(void)
{
    for(int i=0;i<MAX;i++)
    {
        for(int j=0;j<MAX;j++)
        {
            int n = 0;
            cin>>n;
            board[i][j] = n;
        }
    }
    cin>>N;
    dfs(0);
    cout<<res;


    return 0;
}