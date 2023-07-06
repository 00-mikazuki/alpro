#include <iostream>

using namespace std;

int main()
{

  int a = 3;
  int b = 2;

  bool hasil;
  
  // operator logika : not, and, or

  // not
  hasil = !(a == 3);

  // and atau && : kedua nilai true untuk menghasilkan true
  cout << "untuk and \n";
  hasil = (a == 3) and (b == 2); // true and true
  cout << hasil << endl;
  hasil = (a == 4) and (b == 2); // false and true
  cout << hasil << endl;
  hasil = (a == 3) && (b == 3); // true and false
  cout << hasil << endl;
  hasil = (a == 4) && (b == 3); // false and false
  cout << hasil << endl;

  // or atau || : salah satu nilai true untuk menghasilkan true
  cout << "untuk or \n";
  hasil = (a == 3) or (b == 2); // true or true
  cout << hasil << endl;
  hasil = (a == 4) or (b == 2); // false or true
  cout << hasil << endl;
  hasil = (a == 3) || (b == 3); // true and false
  cout << hasil << endl;
  hasil = (a == 4) || (b == 3); // false and false
  cout << hasil << endl;



  return 0;
}