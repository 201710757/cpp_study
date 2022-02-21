#include <string>
#include<algorithm>
#include<map>
#include<iostream>
using namespace std;

int main(void) {
    string str1 = "FRANCE";
    string str2 = "french";
    int answer = 0;
    map<string, int>cnt_map1;
    map<string, int>cnt_map2;
    
    
    // transform(str1.begin(), str1.end(), str1.begin(), ::tolower);
    // transform(str2.begin(), str2.end(), str2.begin(), ::tolower);
    for(int i=0;i<str1.size()-1;i++)
    {
        string tmp = str1.substr(i, 2);
        transform(tmp.begin(), tmp.end(), tmp.begin(), ::tolower);
        
        if((!(tmp[0] >= 'a' && tmp[0] <= 'z')) || (!(tmp[1] >= 'a' && tmp[1] <= 'z')))
            continue; // if 0 : i += 1 & if 1 : i += 2
        else
	{
            cnt_map1[tmp] += 1; // total
	    cout<<"check : "<<tmp<<endl;
	}
    }
    
    for(int i=0;i<str2.size()-1;i++)
    {
        string tmp = str2.substr(i, 2);
        transform(tmp.begin(), tmp.end(), tmp.begin(), ::tolower);
        
        if((!(tmp[0] >= 'a' && tmp[0] <= 'z')) || (!(tmp[1] >= 'a' && tmp[1] <= 'z')))
            continue; // if 0 : i += 1 & if 1 : i += 2
        else
	{
	    cout<<"check2 : "<<tmp<<endl;
            cnt_map2[tmp] += 1; // total
	}    
    }
    
    double g = 0, s = 0;
    for(auto iter1 : cnt_map1)
    {
	bool _flag = false;
        for(auto iter2 : cnt_map2)
        {
            if(iter1.first == iter2.first)
            {
		cout<<"same : "<< iter1.first<<endl;
		_flag = true;
                if(iter1.second > iter2.second)
                {
                    s += iter1.second;
                    g += iter2.second;
                }
                else
                {
                    s += iter2.second;
                    g += iter1.second;
                }
            }
        }
	if(!_flag)
	{
	    cout<<"no : "<<iter1.first<<endl;
	    s += iter1.second;
	}
    }
    cout<<"g : " << g << " / s : "<< s << endl;
    answer = (int)(g/s * 65536);
    
    return answer;
}
