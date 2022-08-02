/**
 *    author:  hari
 *    created: 03.08.2022 02:59:32
**/
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
  int n,k; cin>>n>>k;
  long a[n+1],s=0,dem=0;
  for (int i=1;i<=n;i++) cin>>a[i], s+=a[i];
  while (k*n-s>float(n/2)) s+=k, n++, dem++;
  cout<<dem;
  cout<<endl;
}
