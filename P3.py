lis_1 =[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
ele = 2
lis_2 = list()
for i in range(0,len(lis_1)):
	if ele == lis_1[i]:
		lis_2.append(i)
print(lis_2)