#include <string>
#include <iostream>
#include <vector>
#include <cmath>
#include <list>

using namespace std;
char oper[24+1][4+1] = {0,};
int cnt = 0;

void swap(char arr[], int num1, int num2)
{
    char tmp = arr[num1];
    arr[num1] = arr[num2];
    arr[num2] = tmp;
}

void per(char arr[], int index, int arr_size)
{
    if(arr_size-1 == index)
    {
        for(int i=0;i<arr_size;i++)
            oper[cnt][i] = arr[i];
        cnt++;
        
        return;
    }
    for(int i=index;i<arr_size;i++)
    {
        swap(arr, index, i);
        per(arr, index+1, arr_size);
        swap(arr, index, i);
    }
}

int main(void) {
    string expression = "100-200*300-500+20";
    long long answer = -987654321LL;
    vector<int>arr;
    char o[3] = {'+', '-', '*'};
    per(o, 0, sizeof(o)/sizeof(char));
    
    for(int i=0;i<cnt;i++)
    {
        list<long long>num1;
        list<char>operato1;
        
        string tmp = "";
        for(int s = 0;s<expression.size();s++)
        {
            if(!(expression[s] >= '0' && expression[s] <= '9'))
            {
                num1.push_back(stoi(tmp));
		cout<<num1.back()<<" "<<expression[s]<<endl;
                tmp = "";
                operato1.push_back(expression[s]);
            }
            else tmp += expression[s];  
        }
	num1.push_back(stoi(tmp));
	cout<<endl;
        list<long long>::iterator itr1;
        itr1 = num1.begin();
        
        list<char>::iterator itr2;
        itr2 = operato1.begin();
        
        list<long long>num(num1);
	cout<<"num show : "<<endl;
	for(auto s : num)
	    cout<<s<<" ";
        list<char>operato(operato1);
        for(int j=0;j<4;j++)
        {
            char op = oper[i][j];
            int idx=0;
            for(itr2 = operato.begin(); itr2 != operato.end(); )
            {
                if(*itr2 == op)
                {
                    itr1 = num.begin();
                    long long num_tmp = 0LL;
                    
                    itr2 = operato.erase(itr2);
                    for(int k=0;k<idx;k++) ++itr1;
                    
                    if(*itr2 == '+')
                    {    
                        num_tmp = ((*itr1) + (*(++itr1)));
                    }
                    else if(*itr2 == '-')
                    {
                        num_tmp = ((*itr1) - (*(++itr1)));
                    }
                    else if(*itr2 == '*')
                    {
                        num_tmp = ((*itr1) * (*(++itr1)));
                    }
                    --itr1;
                    itr1 = num.erase(itr1);
                    itr1 = num.erase(itr1);
                    
                    num.insert(itr1, num_tmp);
                    idx--;
                }
                else ++itr2;
                idx++;
            }
        }
	cout<<"num : ";
	for(auto sss : num)
	{
	    cout<<sss<<" ";
	}
	cout<<endl;
        if(answer < abs(num.front()))
            answer = abs(num.front());
    }
    cout<<answer<<endl;
    return 0;
}
