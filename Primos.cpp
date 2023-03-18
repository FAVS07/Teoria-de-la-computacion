#include <iostream>
#include <bits/stdc++.h>
#include <string>

using namespace std;

bool esPrimo(int n) {
    if (n <= 1) {
        return false;
    }

    for (int i = 2; i <= n/2; i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}
int binario(int num){
	int cociente, residuo, binario = 0, posicion = 1;
   cociente = num;
   while (cociente > 0) {
      residuo = cociente % 2;
      binario += residuo * posicion;
      posicion *= 10;
      cociente /= 2;
   }
   return binario;
	
}
int main() {
    int num;
	ofstream archivo("Primos.txt"); // abre el archivo para escritura
    cout << "Ingrese el numero: ";
    cin >> num;
	if (archivo.is_open()) {
		archivo<< "numero 	 binario"<< endl;
    for (int i =0; i <= num; i++) {
        if (esPrimo(i)) {
            archivo << i << " = ";
            archivo << binario(i)<< endl;
        }
        
        
    }
    cout << endl;
	}else {
        cout << "No se pudo abrir el archivo" << endl;
    }
    return 0;
}
