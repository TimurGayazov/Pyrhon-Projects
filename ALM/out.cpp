#include <iostream> 
using namespace std; 
 
int main() { 
    int i = 1; 
    int sum = 0; 
    setlocale(0, ""); 
    loop1:
    { 
        int j = 0; 
        loop2:{ 
            int k = 0; 
            loop3:{ 
                sum = sum + i; 
                k++; 
            } if(k < 1){
	goto loop3;
}
            j++; 
        } if(j < 1){
	goto loop3;
}
        i++; 
    } if(i < 1000){
	goto loop3;
}
    loop4:{ 
        int j = 0; 
        loop5:{ 
            sum = sum + i; 
            j++; 
        } if(j < 1){
	goto loop5;
}
        i++; 
    } if(i < 1000){
	goto loop5;
}
 
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
 
