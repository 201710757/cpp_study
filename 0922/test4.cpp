#include<iostream>
#include<vector>
using namespace std;

// pdf 339, page 346
string p;

string dfs(string _input)
{
    if(_input.compare("") == 0)
    {
        return "";
    }

    int check = 0;
    if(_input[0] == '(') check ++;
    else check --;
    for(int i=1;i<_input.size();i++)
    {
        if(_input[i] == '(') check ++;
        else check--;

        if(check == 0) 
        {
            return dfs(_input.substr(0, i+1)) + dfs(_input.substr(i+1));
        }
    }
    
}

int main(void)
{
    cin >> p;
    dfs(p);

    return 0;
}