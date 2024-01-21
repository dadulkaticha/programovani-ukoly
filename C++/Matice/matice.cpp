#include <stdlib.h>    //random
#include <iostream>  //cout, cin
#include <string>   //string (text)
#include <time.h> 

using namespace std;

struct Matice
{
    int** matice;
    int radky;
    int sloupce;
};
Matice NovaMatice (int radky, int sloupce);
void NapsaniMatice(Matice Matice);
Matice SoucetMatic (Matice matice1, Matice matice2);
Matice NasobeniMatic (Matice matice1, Matice matice2);

int main()
{
    srand (time(NULL));
    Matice matice1, matice2, matice3, matice4;
    int radky1, sloupce1, radky2, sloupce2;
    cout<<"Pocet radku prvni matice: ";
    cin>>radky1;
    cout<<"Pocet sloupcu prvni matice: ";
    cin>>sloupce1;
    matice1=NovaMatice(radky1, sloupce1);
    NapsaniMatice(matice1);

    cout<<"Pocet radku druhe matice: ";
    cin>>radky2;
    cout<<"Pocet sloupcu druhe matice: ";
    cin>>sloupce2;
    matice2=NovaMatice(radky2, sloupce2);
    NapsaniMatice(matice2);
    cout << endl;
    matice3=SoucetMatic(matice1, matice2);
    NapsaniMatice(matice3);
    cout << endl;
    matice4=NasobeniMatic(matice1, matice2);
    NapsaniMatice(matice4);

        getchar(); getchar();
        return 0;
}

Matice NovaMatice (int radky, int sloupce)
{
    int** Maticka = new int* [radky];
    Matice Matice;
    Matice.radky = radky;
    Matice.sloupce = sloupce;
    for (int i=0; i<radky; i++)
        {
            Maticka[i]=new int[sloupce];
        }

        for (int i=0; i<radky; i++)
        {
            for(int j=0; j<sloupce; j++)
            {
                Maticka[i][j] = rand() % 10;
            }
        }     
    Matice.matice = Maticka; 
    return Matice;
} 

void NapsaniMatice(Matice Matice)
{
     for (int i=0; i<Matice.radky; i++)
        {
            for(int j=0; j<Matice.sloupce; j++)
            {
                cout<< Matice.matice [i][j] << " ";
            }
        cout << endl;
        }     
}

Matice SoucetMatic(Matice matice1, Matice matice2) {
    if (matice1.radky != matice2.radky || matice1.sloupce != matice2.sloupce)
    {
        cout << "Pro scitani musi matice mit stejny pocet radku a sloupcu." << endl;
        Matice prazdnaMatice = NovaMatice(0, 0);
        //vrati prazdnou matici
        return prazdnaMatice;
    }

    Matice finalniMatice = NovaMatice(matice1.radky, matice1.sloupce);

    for (int i = 0; i < matice1.radky; i++)
    {
        for (int j = 0; j < matice1.sloupce; j++)
        {
            finalniMatice.matice[i][j] = matice1.matice[i][j] + matice2.matice[i][j];
        }
    }

    return finalniMatice;
}

Matice NasobeniMatic(Matice matice1, Matice matice2)
{
    if (matice1.sloupce != matice2.radky) 
    {
        cout << "Pro nasobeni musi byt pocet sloupcu prvni matice roven poctu radku matice druhe." << endl;
        Matice prazdnaMatice = NovaMatice(0, 0);
        //vrati prazdno matici
        return prazdnaMatice;
    }

    Matice finalniMatice = NovaMatice(matice1.radky, matice2.sloupce);

    for (int i = 0; i < matice1.radky; i++) 
    {
        for (int j = 0; j < matice2.sloupce; j++) 
        {
            finalniMatice.matice[i][j] = 0;
            for (int k = 0; k < matice1.sloupce; k++) 
            {
                finalniMatice.matice[i][j] += matice1.matice[i][k] * matice2.matice[k][j];
            }
        }
    }

    return finalniMatice;
}