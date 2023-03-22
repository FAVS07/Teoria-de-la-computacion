#include <bits/stdc++.h>
#include <string>
typedef long long ll;
using namespace std;

string numbinario (ll num,ll &con,ll TamanoCadena){
    ll cociente, residuo, binario = 0, posicion = 1;
   	cociente = num;
   while (cociente > 0) {
      residuo = cociente % 2;
      if(residuo == 1)con++;
      binario += residuo * posicion;
      posicion *= 10;
      cociente /= 2;

   }
   string BinarioCadenaFinal,NumeroBinario;
   NumeroBinario = std::to_string(binario);
   if(TamanoCadena > NumeroBinario.size()){
   		for(ll i =0; i< TamanoCadena-NumeroBinario.size() ;i++){
   			 BinarioCadenaFinal += '0';
		}
		BinarioCadenaFinal =  BinarioCadenaFinal + NumeroBinario;
		return BinarioCadenaFinal;
   }else{
   	    BinarioCadenaFinal = NumeroBinario;
		return  BinarioCadenaFinal;
   }
   
}
   	
int main() {
	ofstream archivo("numeros.txt"); // abre el archivo para escritura
	ofstream archivo2("numerosdeunos.txt");
		ll universo;
		cout << "Por favor ingrese el numero del universo que desea"<< endl;
		cin >>universo;
		if (archivo.is_open()) {
		ll k = (pow(2,universo));
			for(ll i =0; i<= universo;i++){
				ll k2 = (pow(2,i));
				archivo << "***********************Universo "<< i << endl;
				if(k2 == 1){
					archivo << "e"<< endl;
				}else{
					for(ll j =0; j<k2 ; j++){
						ll contador=0;
						string cadena;
						cadena = numbinario(j,contador,i);
						archivo << cadena << endl;
						archivo2 << contador<<","<< j<< endl;
			
					}
				}
		
			}
			cout << "la k es "<< k << endl;
			archivo.close();
    		archivo2.close();
	}else{
		 cout << "No se pudo abrir el archivo" << endl;
	}

}
