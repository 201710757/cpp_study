#include<iostream>
#include<vector>
using namespace std;
// 341 - real 334
int board[9][9];
int N,M;
bool check[9][9];
int max_res = -987654321;

int copy_board[9][9];

int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};
void virus(int x, int y)
{
    for(int i=0;i<4;i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx >= 0 && ny >= 0 && nx <N && ny <M)
        {
            if(copy_board[nx][ny] == 0) 
            {
                copy_board[nx][ny] = 2;
                virus(nx, ny);
            }
        }
    }
}

int safe_place()
{
    int res = 0;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            if (copy_board[i][j] == 0) res++;
        }
    }
    return res;
}

void dfs(int cnt)
{
    if (cnt == 3)
    {
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                copy_board[i][j] = board[i][j];
            }
        }
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                if(copy_board[i][j] == 2) virus(i,j);
            }
        }
        int sp = safe_place();
        if(max_res < sp) max_res = sp;
        
        return;
    }
    for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                if(board[i][j] == 0)
                {
                    board[i][j] = 1;
                    dfs(cnt + 1);
                    board[i][j] = 0;
                }
            }
        }
}

int main(void)
{
    int max_size = -987654321;

    cin >> N >> M;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            cin >> board[i][j];
            if (board[i][j] != 0) check[i][j] = false;
            else check[i][j] = true;
        }
    }


    dfs(0);

    cout<<max_res<<endl;

    return 0;
}