s = str(input("Введите текст "))
a = str(input("Введите первую букву "))
b = str(input("Введите вторую букву "))
if len (a)>1 or len(b)>1:
    print('Неверные данные!')
else:
    index = 0
    while index < len(s):
        print(s[index])
        if s[index] == a and s[index + 2] == b:
            index += 1
        index += 1
