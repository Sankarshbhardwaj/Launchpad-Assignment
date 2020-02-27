x=input()
y=x.split()
z=[]
l=len(y)-1
while l>=0:
	z.append(y[l])
	l=l-1
print(" ".join(z))