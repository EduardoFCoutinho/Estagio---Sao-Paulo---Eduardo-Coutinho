#include <iostream>

using namespace std;

int main() {
    int INDICE = 13, SOMA = 0, K = 0;
    while (K < INDICE) {
        K = K + 1;
        SOMA = SOMA + K;
    }
    cout << "A soma é: " << SOMA << endl;
    return 0;
}

//Explicação: O código soma todos os números de 1 até 13, resultando em 91.
