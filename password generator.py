import random
lowercase="abcdefghijklmnopqrstuvwxyz"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,_-"
all=lowercase+uppercase+numbers+symbols
length=15
password="".join(random.sample(all, length))
print(password)