#include<iostream>
using namespace std;

const int N = 5;
int arr[N];

int main(void)
{
    int sum = 0;

    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
        sum += arr[i];
    }

    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            if(arr[i] < arr[j])
            {
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
    cout<<sum / N << endl;
    cout<<arr[N/2]<<endl;
    return 0;
}