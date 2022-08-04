#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N=1e6;
int a[N];
#ifdef LOCAL
#include debug.h
#else
#define debug(...) 42
#define debnl(...) 42
#endif
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin>>T;
	while(T--)
	{
		int n,k;
		cin>>n>>k;
		for(int i=1;i<=n;i++)
        {
			cin>>a[i];
		}
		sort(a+1,a+1+n);
		LL sum=0;
		for(int i=1;i<=n;i+=k)
		{
			if(a[i]<0)sum-=a[i];
		}
		for(int i=n;i>=1;i-=k)
		{
			if(a[i]>0)sum+=a[i];
		}
		cout<<2*sum-max(abs(a[1]),abs(a[n]))<<"\n";
	}

}
