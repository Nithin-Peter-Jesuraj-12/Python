a=int(input("Enter the 1st side of the Triangle \n"))
b=int(input("Enter the 2nd side of the Triangle \n"))
c=int(input("Enter the 3rd side of the Triangle \n"))
if(((a+b)>c) & ((a+c)>b) & ((c+b)>a)):
    if((a==b)&(b==c)):
        print("Equilateral Triangle \n")
    elif((a==b)|(b==c)|(c==a)):
        print("Isoceles Triangle \n")
    elif(((a**2)+(b**2)==(c**2))|((c**2)+(b**2)==(a**2))|((a**2)+(c**2)==(b**2))):
        print("Right Angled Triangle \n")
    elif(a!=b|b!=c|c!=a):
        print("Scalene Triangle \n")
else: print("Triangle is not possible with your provided sides \n")