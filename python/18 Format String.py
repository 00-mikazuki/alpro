# angka
angka = 2000.5
formatStr = f'angka = {angka}'
print(formatStr)

# bil bulat
angka = 15
formatStr = f'angka = {angka}'
print(formatStr)

# bil ordo ribuan
angka = 2000000
formatStr = f'jutaan = {angka:,}'
print(formatStr)

# bil desimal
angka = 2005.54321
formatStr = f'desimal = {angka:.3f}'
print(formatStr)

# menampilkan leading zero
angka = 2005.54321
formatStr = f'desimal = {angka:010.3f}' # dari jumlah digit
print(formatStr)

# menampilkan tanda + atau -
angkaMinus = -10
angkaPlus = 10.1234
formatMinus = f'minus = {angkaMinus:+d}'
formatPlus = f'plus = {angkaPlus:+.2f}'
print(formatMinus)
print(formatPlus)

# memformat persen
persentase = 0.045
formatPersen = f'persen = {persentase:.2%}'
print(formatPersen)

# melakukan operasi aritmatika di dlm placeholder
harga = 10000
jumlah = 5
formatStr = f'harga total = Rp. {harga*jumlah:,}'
print(formatStr)

# format angka lain (binary, octal, hexadecimal)
angka = 255
formatBinary = f'binary = {bin(angka)}'
formatOctal = f'octal = {oct(angka)}'
formatHex = f'hex = {hex(angka)}'

print(formatBinary)
print(formatOctal)
print(formatHex)