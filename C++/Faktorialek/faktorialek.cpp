#include <iostream>
using namespace std;

int faktorial(int f)
{
	int vysledek=1;
	int i;
	for (i = 1; i <= f; i++) {
		vysledek = i * vysledek;
	}
	return vysledek;
}
int main()
{
	int f;
	int a;
	cout << "Pro jake cislo chcete vypocitat faktorial? ";
	cin >> f;
	a = faktorial(f);
	cout << "Faktorial cisla " << f << " je " << a << endl;

}