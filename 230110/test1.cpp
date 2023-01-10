#include<iostream>
#define MAX 1001
using namespace std;

int N;
int arr[MAX];

int main(void)
{
    cin >> N;

    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
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
    for(int i=0;i<N;i++) cout<<arr[i]<<endl;
    return 0;
}