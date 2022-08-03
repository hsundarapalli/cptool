/**
 *    author:  hari
 *    created: 03.08.2022 04:58:03
**/
#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int tt;cin>>tt;
	while(tt--){
		int n;cin>>n;
		string s,t;
		cin>>s>>t;
		vector<set<int>>v(3);
		for(int i=0;i<n;i++){
			v[s[i]-'a'].insert(i);
		}
		// for(auto i:v){
		// 	for(int j:i)cout<<j<<" ";cout<<endl;
		// }
		bool ok=true;
		auto checka=[&](int x){
			bool dumok=true;
			if(!v[1].empty()){
				dumok &=(x<*v[1].begin());
			}
			if(!v[2].empty()){
				dumok&=(x<*v[2].begin());
			}
			v[0].erase(x);
			return dumok;
		};
		for(int i=0;i<n;i++){
			if(t[i]=='a'){
				if(v[0].empty()){
					ok=false;
					break;
				}
				if(!checka(*v[0].begin())){
					ok=false;
					break;
				}
				//cout<<"h1"<<endl;
 
			}
			else if(t[i]=='b'){
				if(v[1].empty()){
					ok=false;
					break;
				}
				if(v[2].empty()){
					v[1].erase(*v[1].begin());
					continue;
				}
				if(*v[1].begin()<*v[2].begin()){
					v[1].erase(*v[1].begin());
					continue;
				}
				else{
					ok=false;
					break;
				}
				//cout<<"h2"<<endl;
 
			}
			else{
				if(v[2].empty()){
					ok=false;
					break;
				}
				if(v[0].empty()){
					v[2].erase(*v[2].begin());
					continue;
				}
				if(*v[2].begin()<*v[0].begin()){
					v[2].erase(*v[2].begin());
					continue;
				}
				else{
					ok=false;
					break;
				}
								//cout<<"h3"<<endl;
			}
		}
		cout<<(ok ? "YES":"NO")<<"\n";
	}
}
