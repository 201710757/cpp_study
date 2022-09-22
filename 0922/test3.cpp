#include<iostream>
#include<vector>
using namespace std;

int N, K;
int S, X, Y;
int board[201][201];


int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};
void _virus(int x, int y, int k)
{
    for(int i=0;i<4;i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx >= 0 && ny >= 0 && nx <N && ny <N)
        {
            if(board[nx][ny] == 0) 
            {
                board[nx][ny] = k;
                // virus(nx, ny);
            }
        }
    }
}

void f(int k)
{
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            if(board[i][j] == k)
            {
                _virus(i,j,k);
                return;
            }
        }
    }
}


int main(void)
{
    cin >> N >> K;

    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            cin >> board[i][j];
        }
    }
    cin >> S >> X >> Y;

    for(int i=0;i<S;i++) 
    {
        for(int _k=1;_k<=K;_k++) f(_k);
    }
    cout<<board[X-1][Y-1]<<endl;

    return 0;
}