/**
 *    author:  newuser
 *    created: 03.08.2022 17:01:13
**/
#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
  int n;
  cin >> n;
  string s[n];
  for (int i = 0; i < n; i++)
    cin >> s[i];
  for(int i = 1; i <= s[0].size(); i++)
    for (int j = 0; j < n; j++)
      if (s[j].substr(0, i) != s[0].substr(0, i))
        return cout << i - 1 << endl, 0;
}
