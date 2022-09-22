#include<iostream>
#include<deque>

using namespace std;

int N, M;
int board[201][201];

deque<pair<int, int> > que;

int res = 0;

int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};

int bfs()
{
    que.push_back(make_pair(0,0));

    while(!que.empty())
    {
        int x = que.front().first, y = que.front().second;
        que.pop_front();

        for(int i=0;i<4;i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx >= 0 && ny >= 0 && nx <N && ny <M)
            {
                if(board[nx][ny] == 1) 
                {
                    board[nx][ny] = board[x][y]+1;
                    que.push_back(make_pair(nx,ny));
                }
            }
        }
    }

    return board[N-1][M-1];
    
}
int main(void)
{
    cin >> N>>M;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            cin >> board[i][j];
        }
    }
    cout<<bfs()<<endl;
    return 0;
}