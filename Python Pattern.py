s='Python'
p=[s[:i]for i in range(len(s)+1)]
print(*(p+p[::-1]),sep='\n')