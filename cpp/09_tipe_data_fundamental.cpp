#include <iostream>
#include <limits>

using namespace std;

int main()
{

  // bilangan bulat
  int a = 5; // 32-bit
  unsigned int a1 = 5;
  long long b = 6; // 64-bit
  short c = 7; // 16-bit

  // bilangan decimal
  float d = 1.0;
  double e = 2.5;

  // character
  char f = 'a'; // character 1-bit

  // boolean
  bool g = true; // true/false

  cout << c << endl;
  cout << sizeof(a1) << " byte" << endl;
  cout << numeric_limits<unsigned int>::max() << endl;
  cout << numeric_limits<unsigned int>::min() << endl;

  return 0;
}