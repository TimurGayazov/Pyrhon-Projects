#include <iostream>
using namespace std;

int main() {
    int i = 1;
    int sum = 0;
    setlocale(0, "");
    do
    {
        int j = 0;
        do {
            int k = 0;
            do {
                sum = sum + i;
                k++;
            } while (k < 1);
            j++;
        } while (j < 1);
        i++;
    } while (i < 1000);
    do {
        int j = 0;
        do {
            sum = sum + i;
            j++;
        } while (j < 1);
        i++;
    } while (i < 1000);

    i = 0;
    if (i == 0) {
        cout << "gagaga do {" << endl;
    } while (i < 1) {
        cout << "woops" << endl;
        i++;
    }
    cout << "Сумма чисел от 1 до 1000 = " << sum << endl;
    return 0;
}
