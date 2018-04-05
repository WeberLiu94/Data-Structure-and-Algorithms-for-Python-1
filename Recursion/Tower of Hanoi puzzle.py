def move(n, a, buffer, c):
    if n == 1 :
        print(a,"->",c)
        return
    move(n-1, a, c, buffer) #通过C的帮助，将a的n-1个盘子移动到b
    move(1, a, buffer, c)   #将a的最下面一个移动到c
    move(n-1, buffer, a, c) #通过a将b的盘子移动到c


move(4, "a", "b", "c")

#我们不关心上面的盘子到底有几个，我们每次的操作就是把最底下的盘子通过缓冲区 b柱 buffer 移动到c柱。