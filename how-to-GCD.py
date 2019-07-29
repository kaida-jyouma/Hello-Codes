def gcd(x, y = 1):
	xdiv = []
	ydiv = []
	for i in range(1, x + 1):
		if x % i == 0:
			xdiv.append(i)
	for j in range(1, y + 1):
		if y % j == 0:
			ydiv.append(j)
	retgcd = 0
	for k in xdiv:
		if (k in ydiv):
			retgcd = k
	return(retgcd)
print(gcd(10, 15))
