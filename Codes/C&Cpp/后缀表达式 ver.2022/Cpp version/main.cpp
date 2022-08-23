#include "PfEps.h"
#include <iostream>
#include <cstring>

int main()
{
    std::string str;
    std::getline(std::cin, str);
    Postfix_Eps eps(str);
    std::cout << eps.getContents();
    return 0;
}