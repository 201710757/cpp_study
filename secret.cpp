#include<iostream>
#include<vector>
#include<string>

using namespace std;

vector<int> f(int n)
{
    vector<int> two;
    while(n>0)
    {
        two.push_back(n%2);
        n /= 2;
    }
    return two;
}

int main(void)
{
    const int N = 5;
    vector<int>arr = {9, 20, 28, 18, 11};
    vector<int>arr1 = {30, 1, 21, 17, 28};
    vector<string> answer;
    vector<vector<int> > arr;
    
    for(int i=0;i<arr1.size();i++)
    {
        vector<int>tmp = f(arr1[i]);
        vector<int>tmp1 = f(arr2[i]);
        
        for (int j=tmp.size()-1; j>=0; j--)
            arr[i][j] += (tmp[j] + tmp1[j]);
    }
    // for(int i=0;i<arr2.size();i++)
    // {
    //     vector<int>tmp = f(arr2[i]);
    //     for(int j=0;j<tmp.size();j++)
    //         arr[i][j] += tmp[j];
    // }
    for(int i=0;i<arr.size();i++)
    {
        string s = "";
        for(int j=0;j<arr[i].size();j++)
        {
            if(arr[i][j] >=1)
                s += "#";
            else if (arr[i][j] == 0)
                s += " ";
                
        }
        answer.push_back(s);
    }
}
