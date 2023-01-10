#include<iostream>
using namespace std;

const int MAX_N = 1001;
const int MAX_k = MAX_N;
const int MAX_x = 10000;
int arr[MAX_N];

int N, k;
int main(void)
{
    cin >>N>>k;

    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
    }

    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            if(arr[i] > arr[j])
            {
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
    
    cout << arr[k-1]<<endl;



    return 0;
}