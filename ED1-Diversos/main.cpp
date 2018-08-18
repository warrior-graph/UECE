#include <iostream>
#include <string>
#include <vector>

#include "dtree.hpp"

void menu()
{
    std::cout << "(1) Create Tree\n"
              << "(2) Show Tree\n"
              << "(3) Prune Tree property\n"
              << "(4) Exit\n";
}
inline void clear()
{
    for(int i = 0; i <  100; ++i) std::cout << '\n';
}
int main()
{
    std::ios_base::sync_with_stdio(false);
    int input, n_prop;
    std::vector<std::string> question;
    std::string property;
    DTree DT = DTree();
    clear();
    while(true)
    {
        menu();
        std::cin >> input;
        switch (input)
        {
            case 1:
                std::cout << "Type the number of preperties: \n";
                std::cin >> n_prop;
                question = std::vector<std::string>(n_prop);
                std::cout << "Type " << n_prop << " property labels\n";
                for(size_t i = 0; i < n_prop; ++i)
                    std::cout << "Label " << i + 1 << ": ",
                    std::cin >> question[i], std::cout << '\n';
                DT.create(question);
                break;
            case 2:
                clear();
                DT.show(DT.root, 0);
                std::cout << "\n\n";
                break;
            case 3:
                std::cout << "Type a property to be pruned: ";
                std::cin >> property;
                DT.prune(property);
                break;
            case 4:
                return 0;
            default:
                break;
        }
    }
    return 0;
}
