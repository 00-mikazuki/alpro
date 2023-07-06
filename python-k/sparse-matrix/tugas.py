import ModulSparseMatrix as spars

print('\n')
print('matrik-1')
baris = int(input('Jumlah baris = '))
kolom = int(input('Jumlah kolom = '))
jumData = int(input('jumlah data='))
matrix1 = spars.createSparseMatrix(baris, kolom, jumData)

print(' ')

print('matrik-2')
baris = int(input('Jumlah baris = '))
kolom = int(input('Jumlah kolom = '))
jumData = int(input('jumlah data='))
matrix2 = spars.createSparseMatrix(baris, kolom, jumData)

print(' ')

kaliMatrix = spars.crossMatrix(matrix1, matrix2)


print('matrik 1=')
print(spars.displaySparseMatrix(matrix1))
print(' ')

print('matrik 2=')
print(spars.displaySparseMatrix(matrix2))
print(' ')

print('Hasil =')
print(spars.displaySparseMatrix(kaliMatrix))