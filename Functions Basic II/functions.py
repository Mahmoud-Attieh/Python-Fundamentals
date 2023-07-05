def countDown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)  # append like a push in js
    return newList


def print_return(list):
    print(list[0])
    return list[1]

def first_length(list):
    y=len(list)+list[0]
    return y


def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = [] # greaterthan = list[1] , thats mean if the list contain just a one of emlements , it will be to display a false , and if contain more one elm ,it will be cheak 
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList


def length_and_value(size,value): # i Def the func 
    newList = [] 
    for i in range(size):
        newList.append(value)
    return newList





print(countDown(5))
print (print_return([1,2]))
print(first_length([1,2,3,4,5]))
print(values_greater_than_second([2,3]))
print(values_greater_than_second([5,2,3,2,1,4]))
print(length_and_value(4,7))
print(length_and_value(6,2))


