def fun(a):
    b = a[:]
    c= []
    for i in range(len(a)-1):
        a[i], a[i+1] = a[i+1], a[i]
        c.append(a)
        a = b[:]
    print("a", a)
    print("b", b)
    print("c", c)

a = [1,2,3]
fun(a)