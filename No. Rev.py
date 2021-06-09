no=int(input("Enter your no \n"))
remainder = []
while no!=0:
    remainder.append(no%10)
    no//=10
print ("".join(map(str,remainder)))