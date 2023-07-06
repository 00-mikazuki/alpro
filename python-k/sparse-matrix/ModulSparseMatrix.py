def createSparseMatrix(baris, kolom, jumData):
  stop = False
  matrix = []

  for i in range(baris):
    isi = []
    for j in range(kolom):
      isi.append(0)
    matrix.append(isi)

  for i in range(jumData):
    indBaris = int(input('baris ke ?'))
    indKolom = int(input('kolom ke ?'))
    temp = 'matrik [' + str(indBaris) + ',' + str(indKolom) + ']= '
    matrix[indBaris][indKolom] = int(input(temp))

  return matrix


def displaySparseMatrix(matrix):
  temp = ''
  for i in range(len(matrix)):
    temp += '| '
    for j in range(len(matrix[0])):
      temp += str(matrix[i][j]) + ' '
    temp += '|\n'

  return temp


def crossMatrix(mat1, mat2):
  xmat = []
  if len(mat1[0])==len(mat2):
    for i in range(len(mat1)):
      mat = []
      for j in range(len(mat2[0])):
        jumlah = 0
        for k in range(len(mat1[0])):
          jumlah += mat1[i][k]*mat2[k][j]
        mat.append(jumlah)
      xmat.append(mat)
    return xmat
  elif len(mat2[0])==len(mat1):
    for i in range(len(mat2)):
      mat = []
      for j in range(len(mat1[0])):
        jumlah = 0
        for k in range(len(mat2[0])):
          jumlah += mat2[i][k]*mat1[k][j]
        mat.append(jumlah)
      xmat.append(mat)
    return xmat
