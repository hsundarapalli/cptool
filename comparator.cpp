#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int main (int argc, char**argv) {
	 std::ifstream expected_output (argv[1]);
	 std::ifstream received_output (argv[2]);
	 int test_num = stoi(argv[3]);
	 vector<string> ex, rcv;
	 while(expected_output){
			string x;
			expected_output >> x;
			ex.push_back(x);
		}
 	while(received_output){
			string x;
			received_output >> x;
			rcv.push_back(x);
		}
		cout << ("Testcase " + to_string(test_num) + (ex == rcv ? " passed" : " failed")) << endl;

}