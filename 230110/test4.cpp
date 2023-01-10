#include<iostream>
#include<algorithm>

#define MAX_N 1000010
using namespace std;

int arr[MAX_N];

void q(int s, int e)
{
    if(s>=e) return;

    int middle = (s+e) / 2;
    int piv = arr[middle];
    int l = s;
    int r = e;

    while(l<=r)
    {
        while(arr[l] < piv) l++;
        while(arr[r]>piv) r--;

        if (l<=r)
        {
            int tmp = arr[l];
            arr[l] = arr[r];
            arr[r] = tmp;

            l++;
            r--;
        }
    }
    if(s < r) q(s, r);
    if(e > l) q(l, e);
}

int main(void)
{

    int N;
    cin >> N;
    for(int i=0;i<N;i++)
    {
        cin >> arr[i];
    }

    sort(arr, arr + MAX_N);
    // q(0, N-1);

    for(int i=0;i<N;i++)
    {
        cout<<arr[i]<<'\n';
    }

    return 0;
}

