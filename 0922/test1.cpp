#include<iostream>
#include<vector>
using namespace std;

int N, K, X, M;
int board[300001];


vector<int> res;
int main(void)
{
    cin >> N >> M >> K >> X;

    for(int i=0;i<M;i++)
    {
        int s, e;
        cin >> s >> e;

        if(s == X)
        {
            board[e] = 1;
        }
        else
        {
            if(board[s] != 0)
            {
                if(board[s] + 1 < board[e]) board[e] = board[s] + 1;
                else if (board[e] == 0) board[e] = board[s] + 1;
            }
            else
            {
                board[e] = board[s] + 1;
            }
        }

    }

    for(int i=1;i<=N;i++)
    {
        if(board[i] == K) res.push_back(i);
    }
    if(res.size() == 0) cout<<-1<<endl;
    else
    {
        for(int i=0;i<res.size();i++) cout<<res[i]<<endl;
    }
    return 0;
}