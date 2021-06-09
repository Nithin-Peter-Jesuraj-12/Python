'''num=int(input("enter a number "))

for x in range(1,num+1):
    for y in range(1,x+1):
        print(y,end="")
    print(str(x)*(num-x))



    print("\n")'''



'''myString="123456"
count=6

for x in range(0,6):
    print(myString[:x]+count*myString[x])
    count-=1'''



n=int(input('Enter a value-> '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(1,n-i+1):
        print(j,end=' ')
    print()