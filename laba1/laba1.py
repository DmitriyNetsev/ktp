d = int(input("Введите день рождения: "))
m = int(input("Введите месяц рождения: "))
y = int(input("Введите месяц рождения: "))
d1 = int(input("Введите сегодняшний день: "))
m1 = int(input("Введите текущий месяц: "))
y1 = int(input("Введите текущий год: "))
v = False
if (y1 % 4 == 0):
    v = True
    if (y1 % 100 == 0):
        v = False
        if (y1 % 400 == 0):
            v = True
if (y > y1):
    print("Неверные данные!")
else:
    if (y1 > 0):
        if (m1 > m):
            y2 = y1 - y
            if (d1 < d):
                m2 = m1 - m - 1
                if (m1 == 1 |m1 == 2 |m1 == 4 |m1 == 6 |m1 == 8 |m1 == 9 |m1 == 11 ):
                    d2 = 31 + d1 - d
                if (m1 == 5 |m1 == 7 |m1 == 10 |m1 == 12):
                    d2 = 30 + d1 - d
                if (m1 == 3):
                    if(v):
                        d2 = 29 + d1 - d
                    else:
                        d2 = 28 + d1 - d
            else:
                m2 = m1 - m
                d2 = d1 - d
        if (m1 < m):
            y2 = y1 - y - 1
            m2 = 12 + m1 - m
            if (d1 < d):
                m2 = m1 - m - 1
                if (m1 == 1 | m1 == 2 | m1 == 4 | m1 == 6 | m1 == 8 | m1 == 9 | m1 == 11):
                    d2 = 31 + d1 - d
                if (m1 == 5 | m1 == 7 | m1 == 10 | m1 == 12):
                    d2 = 30 + d1 - d
                if (m1 == 3):
                    if (v):
                        d2 = 29 + d1 - d
                    else:
                        d2 = 28 + d1 - d
            else:
                m2 = 12 + m1 - m
                d2 = d1 - d
        if (m1 == m):
            if (d1 < d):
                y2 = y1 - y - 1
                m2 = 11
                if (m1 == 1 | m1 == 2 | m1 == 4 | m1 == 6 | m1 == 8 | m1 == 9 | m1 == 11):
                    d2 = 31 + d1 - d
                if (m1 == 5 | m1 == 7 | m1 == 10 | m1 == 12):
                    d2 = 30 + d1 - d
                if (m1 == 3):
                    if (v):
                        d2 = 29 + d1 - d
                    else:
                        d2 = 28 + d1 - d
            else:
                y2 = y1 - y
                m2 = 0
                d2 = d1 - d
    else:
        if (m1 > m):
            y2 = y1 - y - 1
            if (d1 < d):
                m2 = m1 - m - 1
                if (m1 == 1 | m1 == 2 | m1 == 4 | m1 == 6 | m1 == 8 | m1 == 9 | m1 == 11):
                    d2 = 31 + d1 - d
                if (m1 == 5 | m1 == 7 | m1 == 10 | m1 == 12):
                    d2 = 30 + d1 - d
                if (m1 == 3):
                    if (v):
                        d2 = 29 + d1 - d
                    else:
                        d2 = 28 + d1 - d
            else:
                    m2 = m1 - m
                    d2 = d1 - d
        if (m1 < m):
            y2 = y1 - y - 2
            m2 = 12 + m1 - m
            if (d1 < d):
                m2 = m1 - m - 1
                if (m1 == 1 | m1 == 2 | m1 == 4 | m1 == 6 | m1 == 8 | m1 == 9 | m1 == 11):
                    d2 = 31 + d1 - d
                if (m1 == 5 | m1 == 7 | m1 == 10 | m1 == 12):
                    d2 = 30 + d1 - d
                if (m1 == 3):
                    if (v):
                        d2 = 29 + d1 - d
                    else:
                        d2 = 28 + d1 - d
            else:
                m2 = 12 + m1 - m
                d2 = d1 - d
        if (m1 == m):
            if (d1 < d):
                y2 = y1 - y - 2
                m2 = 11
                if (m1 == 1 | m1 == 2 | m1 == 4 | m1 == 6 | m1 == 8 | m1 == 9 | m1 == 11):
                    d2 = 31 + d1 - d
                if (m1 == 5 | m1 == 7 | m1 == 10 | m1 == 12):
                    d2 = 30 + d1 - d
                if (m1 == 3):
                    if (v):
                        d2 = 29 + d1 - d
                    else:
                        d2 = 28 + d1 - d
            else:
                y2 = y1 - y - 1
                m2 = 0
                d2 = d1 - d
print("Со дня рождения прошло ",y2, "лет ", m2, "месяцев и ", d2, " дней")

