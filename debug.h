template<class T>void debug(T v);
template<class T1,class T2> void debug(pair<T1,T2> p);
template<class T>void debug(vector<T>v);
template<class T>void debug(set<T>v);
template<class T>void debug(multiset<T>v);
template<class T>void debug(unordered_set<T>v);
template<class T>void debug(unordered_multiset<T>v);
template<class T1,class T2>void debug(map<T1,T2>v);
template<class T1,class T2>void debug(multimap<T1,T2>v);
template<class T1,class T2>void debug(unordered_map<T1,T2>v);
template<class T1,class T2>void debug(unordered_multimap<T1,T2>v);
template<class T>void debug(vector<vector<T>>v);
template<class T>void debug(T v[],int size);

int debug_num_count=1;

void debnl(int x){cerr<<debug_num_count++<<"\n";}	
void debnl(){cerr<<endl;}
template<class T>void debug(T v){cerr<<v<<" ";}
template<class T1,class T2> void debug(pair<T1,T2>v){cerr<<"("<<v.first<<","<<v.second<<")";}
template<class T>void debug(vector<T>v){cerr<<"[ ";for(auto i:v)debug(i);cerr<<"]";cerr<<endl;}
template<class T>void debug(set<T>v){cerr<<"[ ";for(auto i:v)debug(i);cerr<<"]";cerr<<endl;}
template<class T>void debug(multiset<T>v){cerr<<"[ ";for(auto i:v)debug(i);cerr<<"]";cerr<<endl;}
template<class T>void debug(unordered_set<T>v){cerr<<"[ ";for(auto i:v)debug(i);cerr<<"]";cerr<<endl;}
template<class T>void debug(unordered_multiset<T>v){cerr<<"[ ";for(auto i:v)debug(i);cerr<<"]";cerr<<endl;}
template<class T1,class T2>void debug(map<T1,T2>v){cerr<<"[";cerr<<endl;for(auto i:v){debug(i.first);cerr<<":";debug(i.second);cerr<<endl;}cerr<<"]";cerr<<endl;}
template<class T1,class T2>void debug(multimap<T1,T2>v){cerr<<"[";cerr<<endl;for(auto i:v){debug(i.first);cerr<<":";debug(i.second);cerr<<endl;}cerr<<"]";cerr<<endl;}
template<class T1,class T2>void debug(unordered_map<T1,T2>v){cerr<<"[";cerr<<endl;for(auto i:v){debug(i.first);cerr<<":";debug(i.second);cerr<<endl;}cerr<<"]";cerr<<endl;}
template<class T1,class T2>void debug(unordered_multimap<T1,T2>v){cerr<<"[";cerr<<endl;for(auto i:v){debug(i.first);cerr<<":";debug(i.second);cerr<<endl;}cerr<<"]";cerr<<endl;}
template<class T>void debug(vector<vector<T>>v){cerr<<"[ ";for(auto i:v){debug(i);}cerr<<"]"<<endl;}
template<class T>void debug(T v[],int size){cerr<<"[ ";for(int i=0;i<size;i++){debug(v[i]);}cerr<<"]"<<endl;}

template <typename T, typename... Types>
void debug(T var1, Types... var2)
{
  debug(var1);
  debug(var2...);
}
#define debug(...) cerr<<"[" << #__VA_ARGS__ << "] : ";debug(__VA_ARGS__);


