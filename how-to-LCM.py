def lcm2(x, y):
    c = 1
    while True:
        if (x * c) % y == 0:
            return(x * c)
            break
        c += 1
print(lcm2(1001, 21))
