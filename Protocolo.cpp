#include <iostream>
#include <ctime>
#include <fstream>
#include <random>
#include <bitset>
#include <unistd.h>

typedef long long ll;

using namespace std;

void GenerarCadenas(){
    ofstream Archivo;
    Archivo.open("Cadenas.txt");
    random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> distribucion(0, 2000000000);
    for (int i = 0; i <= 1000000; i++){
       
		ll numero_aleatorio = distribucion(gen);
		bitset<64> bits(numero_aleatorio);
		string cadena_binaria = bits.to_string();
		Archivo << cadena_binaria << endl;
					
        
    }
    
Archivo.close();
}

void Automata(int &estado, char cadena){
 	if(cadena == '1'){
			switch(estado){
				case 0:
					estado =1;
				break;
				case 1:
					estado =0;
				break;
				case 2:
					estado = 3;
				break;	
				case 3:
					estado = 2;
				break;
	
					
			}
	}else{
			switch(estado){
				case 0:
					estado =3;
				break;
				case 1:
					estado =2;
				break;
				case 2:
					estado = 1;
				break;	
				case 3:
					estado = 0;
				break;
			}
					
		}
		
 }

bool Read(){
ifstream archivo("Cadenas.txt");
ofstream archivo2("Aceptadas.txt");
ofstream archivo3 ("NoAceptadas.txt");
  string linea;
  int numlinea=0;
if (archivo2.is_open() ) {
	  while (getline(archivo, linea)) {
		  	int estado=0;
		    for(int i =0; i<linea.size(); i++){
				Automata(estado, linea[i]);
			}
		
			if(estado == 0){
				archivo2 <<numlinea<< " "<<linea<< endl;
			}else{
				archivo3 <<numlinea<<" " <<linea<< endl;
			}
			numlinea++;
	  }
	  archivo.close();
    return true;
}else{
	return  false;
}
  
  
}

bool StarVerifica(bool On_Off){
    if(On_Off){
        cout<<"Esta prendido..."<<endl;
        GenerarCadenas();
        sleep(3);
        if(Read())
            return true;
        else
            return false;
    }
    else{
        cout<<"Esta apagado..."<<endl;
        return false;
    }
}

int main(){
    srand(time(NULL));
    bool prendido=true;
    while(prendido){
        prendido=StarVerifica(bool(rand()%2));
        sleep(3);
     	
    }
    cout << "Adios"<< endl;
}
 // bool(rand()%2)
