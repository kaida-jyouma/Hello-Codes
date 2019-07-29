def rt(x, y = 2):
    num = x
    prm = 0 
    for i in range(16):
        ct = 10 ** -(i)
        while prm ** y < num:
            prm += ct
        prm -= ct
    return(prm)
print(rt(2))
print(rt(2, 3))
