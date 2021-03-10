a=150402
b=190784
c=100321
d=abs(a-c)
e=abs(b-a)
x=1<2
y=1>2
if d<e:
	print("e is greater than d")
else:
	print("d is greater than e")
z=(x and not y)or(y and not x)
w=x!=y
print(z)
print(w)
