/**
 *    author:  newuser
 *    created: 03.08.2022 17:03:04
**/
#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
  long long a, b, m, r, i = 0;
  cin >> a >> b >> m >> r;
  int c[m+1] = {0};
  vector<int> d;
    
  while(c[r] < 2){
    r = (a*r+b)%m;
    c[r]++;
    d.push_back(r);
  }
  while(d[i] != d[d.size()-1]) i++;
  cout << d.size()-i-1;
  
  return 0;
}
