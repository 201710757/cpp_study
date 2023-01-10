#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(void)
{
    int N;
    cin >>N;

    vector<int>v(N);
    for(int i=0;i<N;i++) cin>>v[i];
    
    vector<int>n_v(v);
    sort(n_v.begin(), n_v.end());
    n_v.erase(unique(n_v.begin(), n_v.end()), n_v.end());

    for(int i=0;i<N;i++)
        cout << lower_bound(n_v.begin(), n_v.end(), v[i]) - n_v.begin() <<' ';
    
    return 0;
}