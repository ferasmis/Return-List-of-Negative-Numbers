## Author: Feras
## Description: A method named getNegativeNumber that accepts a list of integer and return a new list of negative numbers.  

def getNegativeNumber(mylist):
    negativeMyList= []
    for i in mylist:
        if i < 0:
            negativeMyList.append(i)
    return negativeMyList
print(getNegativeNumber(mylist = list(range(-10, 10))))
