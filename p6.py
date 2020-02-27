d={}
keys=[]
vals=[]
for i in range(0,3):
	vals.append(input("Enter Name: "))
	keys.append(input("Enter USN: "))
for i in keys:
	for j in vals:
		d[i]=j
		vals.remove(j)
		break
print(d)