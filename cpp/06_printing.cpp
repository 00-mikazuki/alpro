#include <iostream>

// latihan pendahuluan

// fungsi utama / pintu untuk menuju ke program
int main() // kepala fungsi, input argumen
{ // badan fungsi
// setiap memanggil fungsi main, maka akan menjalankan apa yg ada dalam bodynya
  std::cout << "Hello \n"; // \n : new line / menambahkan baris baru
  // "Hello" : string / text
  std::cout << "World" << std::endl; // satu baris disebut statement, diakhiri dengan ;
  // cout : console out
  // << : operator insertion
  // endl : end line / akhir dari baris
  std::cin.get();
  // cin : console input
  // get() : mengambil enter

  return 0;
  // return : mengembalikan nilai saat fungsi berhasil dijalankan
}