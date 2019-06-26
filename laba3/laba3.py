from array import array
a=str(input('Введите первую строчку '))
b=str(input('Введите вторую строчку '))
c=str(input('Введите искомую букву '))
d = False
for letter in a:
    if letter == c:
        d = True
        break
if d:
    for letter in b:
        if letter == c:
            d = True
            break
        else:
            d = False
if d:
    print('T')
else:
    print('F')
