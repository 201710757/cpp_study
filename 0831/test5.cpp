#include<iostream>
#define MAX 15
using namespace std;


int N;
int res;

int arr [MAX] = {0,};

void dfs(int pos)
{
    if(pos == N)
    {
        res += 1;
        return;
    }
    for(int i=0;i<N;i++)
    {
        arr[pos] = i;
        bool _flag = true;
        for(int j=0;j<pos;j++)
        {
            if(arr[pos] == arr[j] || pos-j == abs(arr[pos] - arr[j])) _flag = false;
        }
        if(_flag) dfs(pos + 1);
    }
}
int main(void)
{
    cin>>N;
    dfs(0);
    cout<<res;


    return 0;
}