x=1
y=1
i=1
#x and y are the initial numbers
while i<=11:
#the loop will end by running 11 times
	t=y
	y=x+y
	x=t
	i=i+1
print(y) 
#finally print the thirteenth number
