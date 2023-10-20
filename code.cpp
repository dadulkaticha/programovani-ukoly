// advent kodu.cpp : Tento soubor obsahuje funkci main. Provádění programu se tam zahajuje a ukončuje.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int i;
	int j;
	int k;
	fstream myFile;
	vector <int> cisilko;
	{
		myFile.open("2000.txt", ios::in);
		if (myFile.is_open()) {
			string radek;
			while (getline(myFile, radek))
			{
				cisilko.push_back(stoi(radek));
			}
			myFile.close();
		}
		for (i = 0; i < cisilko.size(); i++)
		{
			for (j = i+1; j < cisilko.size(); j++)
			{
				for (k= j+1; k < cisilko.size(); k++)
				{
					if (cisilko[i] + cisilko [j] + cisilko [k] == 2020)
						cout << cisilko[i] * cisilko[j] * cisilko[k];
				}
			}
		}

	}
}

// Spuštění programu: Ctrl+F5 nebo nabídka Ladit > Spustit bez ladění
// Ladění programu: F5 nebo nabídka Ladit > Spustit ladění

// Tipy pro zahájení práce:
//   1. K přidání nebo správě souborů použijte okno Průzkumník řešení.
//   2. Pro připojení ke správě zdrojového kódu použijte okno Team Explorer.
//   3. K zobrazení výstupu sestavení a dalších zpráv použijte okno Výstup.
//   4. K zobrazení chyb použijte okno Seznam chyb.
//   5. Pokud chcete vytvořit nové soubory kódu, přejděte na Projekt > Přidat novou položku. Pokud chcete přidat do projektu existující soubory kódu, přejděte na Projekt > Přidat existující položku.
//   6. Pokud budete chtít v budoucnu znovu otevřít tento projekt, přejděte na Soubor > Otevřít > Projekt a vyberte příslušný soubor .sln.
