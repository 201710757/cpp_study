#include<iostream>

using namespace std;

int N, M;
int board[1001][1001];

int res = 0;

int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};
void dfs(int x, int y, int ice)
{
    for(int i=0;i<4;i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx >= 0 && ny >= 0 && nx <N && ny <M)
        {
            if(board[nx][ny] == 0) 
            {
                board[nx][ny] = ice;
                dfs(nx, ny, ice);
            }
        }
    }
}

int main(void)
{
    cin >>N >> M;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            cin >> board[i][j];
        }
    }
    int ice = 1;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            if(board[i][j] == 0) 
            {
                dfs(i, j, ice);
                ice ++;
            }

        }
    }
    cout<<ice-1<<endl;


    return 0;
}