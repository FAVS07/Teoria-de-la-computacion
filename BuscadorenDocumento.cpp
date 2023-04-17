#include <iostream>
#include <fstream>

using namespace std;
void Buscador ( int &estado, char cadena){
	if(cadena== 'a'){
			switch(estado){
				case 4:
					estado =17;
				break;
				case 5:
					estado =6;
				break;
				case 16:
					estado = 17;
				break;	
				case 19:
					estado = 20;
				break;	
				case 25:
					estado = 17;
				break;	
				default:
					estado = 1;
				break;		
			}
	}else if(cadena == 'b'){
			switch(estado){
				case 3:
					estado =4;
				break;
				case 9:
					estado =16;
				break;
				case 14:
					estado = 16;
				break;	
				case 15:
					estado = 16;
				break;	
				case 22:
					estado = 16;
				break;
				case 24:
					estado = 25;
				break;
				case 27:
					estado = 16;
				break;
				
				
				default:
					estado = 1;
				break;		
			}
				
	}else if(cadena== 'e'){
			switch(estado){
				case 2:
					estado =3;
				break;
				case 8:
					estado =9;
				break;
				case 13:
					estado = 14;
				break;	
				case 21:
					estado = 22;
				break;	
				case 23:
					estado = 24;
				break;
				case 26:
					estado = 27;
				break;	
				default:
					estado = 15;
				break;		
			}
			
				
	}else if(cadena == 'g'){
				
			switch(estado){
				case 20:
					estado =21;
				break;
				default:
					estado = 1;
				break;		
			}
	}else if(cadena== 'i'){
			switch(estado){
				case 11:
					estado =12;
				break;
				default:
					estado = 1;
				break;		
			}		
	}else if(cadena== 'm'){
			switch(estado){
				case 4:
					estado =5;
				break;
				case 25:
					estado =5;
				break;
				default:
					estado = 1;
				break;		
			}				
	}else if(cadena== 'n'){
			estado = 26;
				
	}else if(cadena== 'p'){
			estado =19;
				
	}else if(cadena == 'r'){
			switch(estado){
				case 9:
					estado =10;
				break;
				default:
					estado = 1;
				break;		
			}				
	}else if(cadena == 's'){
			switch(estado){
				case 4:
					estado =11;
				break;
				case 6:
					estado =7;
				break;
				case 25:
					estado = 11;
				break;
				default:
					estado = 1;
				break;		
			}			
	}else if(cadena == 't'){
			switch(estado){
				case 7:
					estado =8;
				break;
				case 12:
					estado =13;
				break;
				case 27:
					estado =28;
				break;
				default:
					estado = 1;
				break;		
			}			
	}else if(cadena == 'w'){
			switch(estado){
				case 22:
					estado =23;
				break;
				default:
					estado = 2;
				break;		
			}			
	}else if(cadena == 'y'){
			switch(estado){
				case 17:
					estado =18;
				break;
				default:
					estado = 1;
				break;		
			}
				
	}else{
			estado =1;
			
	}	
}

int main() {
    ifstream archivo_entrada;
    archivo_entrada.open("w.html");
    ofstream Historia("Historia.txt");
    ofstream Palabras("Palabras.txt");
    if (!archivo_entrada.is_open()) {
        cout << "No se pudo abrir el archivo" << endl;
        return 1;
    }

    string linea;
    int estado=0;
	int numweb=0, numwebmaster=0,numwebsite =0, numebay=0, numpageweb=0, numnet =0;
	int numLinea =0;
    while (getline(archivo_entrada, linea)) {
        	for(int i =0; i< linea.size(); i++){
	        	Buscador(estado, linea[i]);
	        
					Historia <<"'q"<<estado <<"'";
					switch(estado){
						case 4:
							Palabras <<"web en "<< numLinea <<" pos "<<i-2<<"-"<< i<< endl;
							numweb++;
						break;
						case 10:
							Palabras <<"webmaster en "<< numLinea <<" pos "<< i-7<<"-"<<i<<endl;
							numwebmaster++;
						break;
						case 14:
							Palabras <<"website en "<< numLinea <<" pos "<< i-6<<"-"<<i<<endl;
							numwebsite++;
						break;
						case 18:
							Palabras <<"ebay en "<< numLinea <<" pos "<< i-3<<"-"<<i<<endl;
							numebay++;
						break;
						case 25:
							Palabras <<"pageweb en "<< numLinea <<" pos "<<i-6<<"-"<< i<<endl;
							numpageweb++;
							numweb++;
						break;
						case 28:
							Palabras <<"net en "<< numLinea <<" pos "<< i-2<< "-"<<i<<endl;
							numnet++;
						break;
						default:
						break;		
					}
				
				
			}
		Historia << "\n";
		numLinea++;
    }
    cout << "\n";
    cout << "numero de web "<< numweb<< endl;
    cout << "numero de website "<< numwebsite<< endl;
    cout << "numero de webmaster "<< numwebmaster<< endl;
    cout << "numero de ebay "<< numebay<< endl;
    cout << "numero de pageweb "<< numpageweb<< endl;
    cout << "numero de net "<< numnet<< endl;
    
    archivo_entrada.close();
    
    return 0;
}
