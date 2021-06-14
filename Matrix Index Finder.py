def find_index(array,element):
    for line in array:
        if element in line:
            i=array.index(line)
            j=line.index(element)
            pass
    indexes=[i,j]
    return indexes
myArray = [
    ['banana','jam'],
    ['mango','apple']
]
index_a = find_index(myArray,'banana')
index_b = find_index(myArray,'apple')
print(index_a)
print(index_b)