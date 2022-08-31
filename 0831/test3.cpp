#include<iostream>
#define MAX 9
using namespace std;

int N=0, M=0;
int arr[MAX] = {0,};
bool vis[MAX] = {0,};
void dfs(int cnt)
{
    if(cnt == M)
    {
        for(int i=0;i<M;i++) cout<<arr[i]<<' ';
        cout<<"\n";
        return;
    }
    for(int i=0;i<N;i++)
    {
        arr[cnt] = i+1;
        dfs(cnt + 1);
    }
}
int main(void)
{
    cin>>N>>M;
    dfs(0);

    return 0;
}