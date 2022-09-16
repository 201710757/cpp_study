#include<iostream>
#include<vector>
using namespace std;


int T;
long long P[101] = {0,};


void f(int n)
{
	P[1] = P[2] = P[3] = 1;
	for (int i=4;i<=n;i++)
	{
		//if (P[i] != 0) return P[i];
		//else
		//{
		if (P[i] == 0)
			P[i] = P[i-3] + P[i-2];
		//}
	}
}

int main(void)
{
    vector<long long> res ;
	cin >> T;
	for (int i=0;i<T;i++)
	{
		int tmp = 0;
		cin >> tmp;
		f(tmp);
		res.push_back(P[tmp]);
		// cout<<P[tmp]<<endl;
	}
    for(auto n:res) cout<<n<<endl;
	return 0;
}


