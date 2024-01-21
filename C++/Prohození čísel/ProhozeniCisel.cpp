#include <iostream>
using namespace std;

void VymenaHodnot(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int x = 5;
    int y = 10;

    cout << "Pred prohozenim: x = " << x << ", y = " << y << endl;

    VymenaHodnot(&x, &y);

    cout << "Po prohozeni: x = " << x << ", y = " << y << endl;

    return 0;
}