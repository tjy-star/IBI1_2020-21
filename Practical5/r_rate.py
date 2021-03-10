r=1.1
#r is the rate that people infected infect others
x=84
#x is the number of the initial students
i=1
while i <=5:
#the loop will run five times
    x=x*r+x
    i=i+1
x = str(x)
print("the number of the people who are infected is " + x)
#print the last number of people who are infected
