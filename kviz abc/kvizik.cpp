#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

   struct kviz //uklada spolecne veci nejakych veci (jmena pejsku)
   {
    /* data */
    string otazka;
    string a;
    string b;
    string c;
    char odpoved;
   };

int main()
{
    /* kód */
    kviz kvizik; //vlastni "datovy typ" vytvarim
    string radek;
    char odpoved;
    int skore = 0;
    fstream myFile;
    vector <kviz> dotaznicek; //seznam veci
    myFile.open("kvizik.txt", ios::in);
    if (myFile.is_open()){
        while(getline(myFile, radek))
        {
        stringstream ss(radek);
        getline(ss, kvizik.otazka, ';');
        getline(ss, kvizik.a, ';');
        getline(ss, kvizik.b, ';');
        getline(ss, kvizik.c, ';');
        ss >> kvizik.odpoved;
        dotaznicek.push_back(kvizik); //pushback uklada veci na posledni misto v seznamu, funguje jen u vektoru
        }
        myFile.close();
    }
     for (int i=0; i < 3; i++)
        {
            cout << dotaznicek[i].otazka;
            cout << "a. " << dotaznicek[i].a;
            cout << "b. " << dotaznicek[i].b;
            cout << "c. " << dotaznicek[i].c;
            cin >> odpoved;
            if(odpoved==dotaznicek[i].odpoved);
                skore++;
        }
        cout << "Vase skore je: " << skore;                
    

    return 0;
}
