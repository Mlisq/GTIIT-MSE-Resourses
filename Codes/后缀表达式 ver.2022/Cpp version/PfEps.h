#include <cstring>
#include <stack>
#include <iostream>

class Postfix_Eps
{
    public:
    Postfix_Eps(std::string input);
    std::string getContents(){
        return contents;
    }
    double calculateResult();
    int priority(char marker);

    private:
    std::string contents;
    
};