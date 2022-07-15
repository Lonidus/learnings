def f1():
    def f2():
        nonlocal x
        x = 27
        print('in f2 x =', x)

    def f3():
        nonlocal x
        x = 54
        print('in f3 x =', x)

    print('in f1 x =', x)
    f3()
    f2()
    print('in f1 x =', x)


x = 42
f1()
print('x =', x)
