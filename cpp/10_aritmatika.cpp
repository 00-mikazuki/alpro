#include <iostream>

using namespace std;

int main()
{

  int a = 6;
  int b = 4;

  int hasil;

  // operator +, -, *, /, %

  // penjumlahan
  hasil = a + b;
  cout << a << " + " << b << " = " << hasil << endl;

  // pengurangan
  hasil = a - b;
  cout << a << " - " << b << " = " << hasil << endl;

  // perkalian
  hasil = a * b;
  cout << a << " * " << b << " = " << hasil << endl;

  // pembagian
  hasil = a / b;
  cout << a << " / " << b << " = " << hasil << endl;
  // jika ingin mendapatkan hasil koma, maka salah satu variabel yg dioperasikan harus bertipe data float, dan variabel memori juga harus bertipe float

  // modulus
  hasil = a % b;
  cout << a << " % " << b << " = " << hasil << endl;
  // modulus tidak bisa melakukan operasi antara integer dan float

  // urutan eksekusi
  hasil = (a + b) * a;
  cout << hasil << endl;


  return 0;
}