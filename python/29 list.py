## cara alternatif membuat list
dataRange = range(0,10,2) # range(start,stop,step)
dataList = list(dataRange)
print(dataList)

# membuat list dengan for loop, list comprehension
listFor = [i for i in range(0,10)]
print(listFor)
listFor = [i**2 for i in range(0,10)]
print(listFor)

# membuat list dengan for dan if
listForIf = [i for i in range(0,10) if i != 5]
print(listForIf)

listForIf = [i for i in range(0,10) if i%2 == 0]
print(listForIf)

listForIf = [i**2 for i in range(0,10) if i%2 == 1]
print(listForIf)