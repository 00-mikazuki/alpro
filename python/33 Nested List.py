data0 = [1,2]
data1 = [3,4,5]
list2D = [data0,data1]
print(f'list biasa = {data0}')
print(f'list 2D = {list2D}')

peserta0 = ['ucup',50,'Laki-laki']
peserta1 = ['otong',10,'Laki-laki']
peserta2 = ['dedeh',60,'Perempuan']

listPeserta = [peserta0,peserta1,peserta2]
print(f'peserta = {listPeserta}')

for peserta in listPeserta:
    print(f'nama\t: {peserta[0]}')
    print(f'umur\t: {peserta[1]}')
    print(f'kelamin\t: {peserta[2]}\n')

# dengan reference
listCopy = listPeserta.copy()
print(f'peserta2 = {listCopy}')
peserta0[0] = 'Michael'
print(f'peserta2 = {listCopy}')
print(f'peserta = {listPeserta}')
