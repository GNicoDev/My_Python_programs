def method(a, b, c, d, e, f):
    if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
        print(5)
    elif a == 0 and b == 0 and c == 0 and d == 0:
        print(5)
    else:
        determinant = a * d - b * c
        determinantX1 = e * d - b * f
        determinantX2 = a * f - e * c
        # if a == 0 and c == 0:
        #     if e * d == b * f and b != 0:
        #         print(4, '{0:.6f}'.format(e / b))
        #     else:
        #         print(0)
        # elif b == 0 and d == 0:
        #     if e * c == a * f and a != 0:
        #         print(3, '{0:.6f}'.format(e / a))
        #     else:
        #         print(0)
        if determinant == 0:
            if determinantX1 == 0 and determinantX2 == 0:
                if f != 0:
                    if e % f == 0:
                        print(1, '{0:.6f}'.format(-c / d), '{0:.6f}'.format(f / d))
                    elif f % e == 0:
                        print(1, '{0:.6f}'.format(-c / d), '{0:.6f}'.format(f / d))
                elif e != 0:
                    if f % e == 0:
                        print(1, '{0:.6f}'.format(-a / b), '{0:.6f}'.format(e / b))
                    elif e % f == 0:
                        print(1, '{0:.6f}'.format(-a / b), '{0:.6f}'.format(e / b))
                else:
                    print(5)
            else:
                print(0)
        elif determinant != 0:
            x1 = determinantX1 / determinant
            x2 = determinantX2 / determinant
            print(2, '{0:.6f}'.format(x1), '{0:.6f}'.format(x2))

t = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1],
     [0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 1, 0],
     [0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1],
     [0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1], [0, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 1],
     [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 1, 1],
     [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 0, 1, 1, 0, 0],
     [1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1],
     [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 1, 0],
     [1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0], [1, 1, 1, 0, 1, 1],
     [1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]]

for i in t:
    a = i[0]
    b = i[1]
    c = i[2]
    d = i[3]
    e = i[4]
    f = i[5]
    
    # здесь сам текст программы, вывод я записывал в строковую переменную res
    
    print(a, b, e)
    print(c, d, f)
    method(a, b, c, d, e, f)
    print('--------')
