/**
 *    author:  hari
 *    created: 03.08.2022 07:51:13
**/
#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
  long long l,r,ans=0;
cin>>l>>r;
for(int i=0;l<=r;++i)
{
  long long n=0,j=i,k=1;
  while(j>=0)
  {
    if(j&1)
    {
      n+=k*7;
    }
    else
    {
      n+=k*4;
    }
    k*=10;
    j=j/2-1;
  }
  if(n>=l)
  {
    ans+=1LL*(min(r,n)-l+1)*n;
    l=min(r,n)+1;
  }
}
cout<<ans<<endl;
return 0;

}
