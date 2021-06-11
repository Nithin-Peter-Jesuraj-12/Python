def fibonacci(term):
    term=int(input(" until which number??"))
    counter = 0
    a=0
    b=1
    if term==0:
        print("term: 0: ",a)
    elif term<0:
        while term<0:
            print("Invalid number: ",term)
            return fibonacci(term)
    elif term==1:
        print("term: 0: ",a)
        print("term: 1: ",b)
    else:
        print ("term 0: ",b)
        while counter<term:
            sum=a+b
            a=b
            b=sum
            counter+=1
            print("term ",counter, ": ",sum)
fibonacci(True)
    