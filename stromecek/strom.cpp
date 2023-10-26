
#include <iostream>
using namespace std;

int main()
{
	//koruna
	int vyska;
	int VyskaKmene;
	int SirkaKmene;
	cout << "Jak velky ma byt tento stromecek? ";
	cin >> vyska;
	cout << "Zadejte vysku kmene: ";
	cin >> VyskaKmene;
	cout << "Zadejte sirku kmene: ";
	cin >> SirkaKmene;
	for (int i = 0; i < vyska; i++) {
		for (int m = 0; m < vyska - i - 1; m++) {
			cout << " ";
		}
		for (int j = 0; j < 2 * i + 1; j++) {
			cout << "*";
		}
		cout << endl;
	}
	// kmen
	for (int i = 0; i < VyskaKmene; i++) {
		for (int m = 0; m < vyska-SirkaKmene/2 -1; m++) {
			cout << " ";
		}
		for (int h = 0; h < SirkaKmene; h++) {
			cout << "#";
		}
			cout << endl;
		
	}
}


