#include<iostream>
using namespace std;
int N;
int A[11] = {0,};
int calc[4] = {0,};

int _log[11] = {0,};

int _max = -987654321, _min = 987654321;
void dfs(int n)
{
    if(n == N)
    {
        int res = A[0];
        for(int i=1;i<N;i++)
        {
            if(_log[i] == 0) res += A[i];
            else if (_log[i] == 1) res -= A[i];
            else if (_log[i] == 2) res *= A[i];
            else if (_log[i] == 3) res /= A[i];
        }

        if (res>_max) _max = res;
        if (res<_min) _min = res;

        return;
    }
    else
    {
        for(int i=0;i<4;i++)
        {
            if(calc[i] == 0) continue;
            calc[i] -= 1;

            _log[n] = i;
            dfs(n+1);
            _log[n] = 0;
            
            calc[i] += 1;
        }
    }
}
int main(void)
{
    cin >> N;
    for(int i=0;i<N;i++) cin >> A[i];
    for(int i=0;i<4;i++) cin >> calc[i];
    
    dfs(1);

    cout<<_max<<'\n'<<_min<<endl;

    return 0;
}