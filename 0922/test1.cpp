#include<iostream>
#include<vector>
#include<deque>

using namespace std;

int N, K, X, M;
int board[300010];
vector<int>v_l[300010];
deque<int> que;


int main(void)
{
    
    cin >> N >> M >> K >> X;

    for(int i=0;i<M;i++)
    {
        int s, e;
        cin >> s >> e;
        v_l[s].push_back(e);
    }

    que.push_back(X);
    while(!que.empty())
    {
        int pos = que.front();
        que.pop_front();

        for(auto p : v_l[pos])
        {
            if(board[p] == 0)
            {
                board[p] = board[pos] + 1;
            }
            
            que.push_back(p);
        }
    }


    bool _flag = true;
    for(int i=1;i<=N;i++)
    {
        if(board[i] == K && i != X) 
        {
            _flag = false;
            cout<<i<<endl;
        }
    }
    if(_flag) cout<<-1<<endl;
    
    return 0;
}