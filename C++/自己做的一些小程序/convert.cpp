/**
 * 中缀表达式问题 Made by BY in 2014
 以前的程序解决不了二位以上的数字运算 如: 21+2 -> 212+ -> 2 1+2 -> 2 3 -> ERROR!
 我想出了如下的思路的思路: 21+2 -> 21~2+ -> 21+2 -> 23
 33+22 -> 33~22+ -> 33+22 -> 55
 2+21 -> 2~21+ -> 2+21 -> 23
 */

#include <iostream> 
#include <stack>
#include <string>
using namespace std;
string ToBack(string);
int ToResult(string);
bool isint(char);
int GetType(char);
void print();
static string text;
int main(void)
{
	while (text != "quit")
	{
		print();
	}
	return 0;
}

void print()
{
	cin >> text;
	cout << ToResult(ToBack(text)) << endl;
	text = "";
}

string ToBack(string str)
{
	string result;
	bool stillint = false;
	stack<char> s;
	for (int i = 0; i < str.length(); i++)
	{
		char c = str.at(i);
		if (isint(c))
		{
			if (stillint)
			{
				if (i + 1 != str.length())
				{
					if (isint(str.at(i + 1)))
					{
						result.append(1, c);
					}
					else {
						stillint = false;
						result.append(1, c);
						result.append(1, '~');
					}
				}
				else {
					result.append(1, c);
				}
			}
			else {
				result.append(1, c);
				stillint = true;
			}
		}
		else {
			if (stillint)
			{
				result.append(1, '~');
				stillint = false;
			}
			if (c == '(')
			{
				s.push(c);
			}
			else {
				if (c == ')')
				{
					while (s.top() != '(')       //是右括号 就依次出栈 知道遇到做括号为止
					{
						result.append(1, s.top());
						s.pop();
					}
					s.pop();      //去掉左括号
				}
				else
				{
					if (s.empty())         //这一点很容易遗忘
					{
						s.push(c);
					}
					else
					{
						if (GetType(c) > GetType(s.top()))       //如果优先级大于栈首
							s.push(c);
						else
						{
							while (!s.empty() && GetType(c) <= GetType(s.top()))   //知道栈空或者优先级小了为止
							{
								result.append(1, s.top());
								s.pop();
							}
							s.push(c);
						}
					}
				}
			}
		}
	}
	while (!s.empty()) {
		result.append(1, s.top());
		s.pop();
	}
	return result;
}

int ToResult(string str)
{
	int val = 0;
	stack<int> result_s;
	for (int i = 0; i < str.length(); ++i) {   //233~1+
		char c = str.at(i);
		if (isint(c))
		{
			val = val * 10 + (int)(c - '0');
		}
		if (c == '~')
		{
			result_s.push(val);
			val = 0;
		}
		if (isint(c) && !isint(str.at(i + 1)) && str.at(i + 1) != '~')
		{
			result_s.push(val);
			val = 0;
		}
		if (c == '+')
		{
			int x = result_s.top();
			result_s.pop();
			int y = result_s.top();
			result_s.pop();
			result_s.push(x + y);
		}
		if (c == '-')
		{
			int x = result_s.top();
			result_s.pop();
			int x2 = result_s.top();
			result_s.pop();
			result_s.push(x2 - x);
		}
		if (c == '*')
		{
			int x = result_s.top();
			result_s.pop();
			int x2 = result_s.top();
			result_s.pop();
			result_s.push(x * x2);
		}
		if (c == '/')
		{
			int x = result_s.top();
			result_s.pop();
			int x2 = result_s.top();
			result_s.pop();
			result_s.push(x2 / x);
		}
	}
	int result = result_s.top();
	result_s.top();
	return result;
}

bool isint(char c)
{
	if ('0' <= c && c <= '9')
		return true;
	return false;
}

int GetType(char c)
{
	if (c == '+' || c == '-')
		return 1;
	if (c == '*' || c == '/')
		return 2;
	return 0;
}