#include<iostream>
#define MAX 9
using namespace std;

int N=0, M=0;
int arr[MAX] = {0,};
bool vis[MAX] = {0,};
void dfs(int cnt, int before)
{
    if(cnt == M)
    {
        for(int i=0;i<M;i++) cout<<arr[i]<<' ';
        cout<<"\n";
        return;
    }
    for(int i=before;i<N;i++)
    {
        if(!vis[i])
        {
            vis[i] = true;
            arr[cnt] = i+1;
            dfs(cnt + 1, i);
            vis[i] = false;
        }
    }
}
int main(void)
{
    cin>>N>>M;
    dfs(0, 0);

    return 0;
}