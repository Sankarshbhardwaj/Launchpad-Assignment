lis_1 = [1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]
lis_2 = list()
for i in lis_1:
	if i not in lis_2:
		lis_2.append(i)
print(lis_2)
