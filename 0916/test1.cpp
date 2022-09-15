#include<iostream>
using namespace std;


int _min = 987654321;

int N;

int board[20+1][20+1];
int team[21];

void dfs(int n, int s)
{
    if (n == N / 2)
    {
        int start = 0, link = 0;

        for(int i=0;i<N;i++)
        {
            if (team[i] == 1)
            {
                for(int j=0;j<N;j++)
                {
                    if(team[j] == 1) start += board[i][j];
                }
            }
            else
            {
                for(int j=0;j<N;j++)
                {
                    if(team[j] == 0) link += board[i][j];
                }
            }
        }

        int tmp = abs(start-link);
        if (_min > tmp) _min = tmp;
        return;
    }

    for(int i=s;i<N;i++)
    {
        team[i] = 1;
        dfs(n+1, i+1);
        team[i] = 0;
    }
}
int main(void)
{
    cin >> N;

    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            cin>>board[i][j];
        }
    }
    dfs(0,0);
    cout<<_min<<endl;

    return 0;
}