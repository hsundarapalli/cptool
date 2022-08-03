#include<bits/stdc++.h>
using namespace std;
long long a[200020];
int main()
{
	int t;
	scanf("%d",&t);
	while (t)
	{
		t--;
		int n;
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%lld",&a[i]);
		sort(a+1,a+n+1);
		long long x=a[1]+a[2]+a[3],y=a[n]+a[n-1]+a[n-2];
		if ((x==a[1]||x==a[2]||x==a[3])&&(y==a[n]||y==a[n-1]||y==a[n-2])&&(a[1]+a[n]==0||a[1]==0||a[n]==0||n==3||(n==4&&(a[1]+a[2]+a[4]==a[1]||a[1]+a[2]+a[4]==a[2]||a[1]+a[2]+a[4]==a[3]||a[1]+a[2]+a[4]==a[4])&&(a[1]+a[3]+a[4]==a[1]||a[1]+a[3]+a[4]==a[2]||a[1]+a[3]+a[4]==a[3]||a[1]+a[3]+a[4]==a[4])))) printf("YES\n");
		else printf("NO\n");
	}
}
