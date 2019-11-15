//yangjungah
#include <iostream>
#include <stack>
#include <string>
using namespace std;
string balance(string s) {
	stack<char> st;
	char cur = ' ';
	for(int i = 0 ; i <s.length(); i++)
	{
		if (st.empty() && (s[i]== ')' || s[i] == ']')) {
			return "no";
		}
		if (s[i] == '(' || s[i] == '[') {
			st.push(s[i]);
			cur = s[i];
		}
		if ((cur == '(' && s[i] == ']') || (cur == '[' && s[i] == ')')) {
			return "no";
		}
		if ((cur == '(' && s[i] == ')') || (cur == '[' && s[i]==']')) {
			st.pop();
			if(!st.empty())
				cur = st.top();
		}
	}
	if (st.empty())
		return "yes";
	else
		return "no";
}
int main() {

	string s;

	while (true) {
		
		cin.clear();
		getline(cin, s);
		if (s == ".")
			break;
		cout << balance(s) << endl;
	}
	return 0;
}