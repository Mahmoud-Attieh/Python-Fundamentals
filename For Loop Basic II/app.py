def Biggie_Size(list):
    for i in range(len(list)):
        if list[i]>0:
            list[i]='Big'
    return list

def Count_Positives(list):
    count = 0
    for val in list:
        if val > 0:
            count += 1
    list[len(list)-1] = count
    return list



def Sum_Total(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def Average(list):
    sum = 0
    for i in list:
        sum += i
    return (sum/len(list))


def length(list):
    return len(list)


def Min(list):
    if len(list)<0:
        return False
    MinInt = list[0]
    for i in list:
        if i<MinInt:
            MinInt = i
    return MinInt


def Max(list):
    if len(list)<0:
        return False
    MaxInt = list[0]
    for i in list:
        if i>MaxInt:
            MaxInt = i
    return MaxInt


#8 : i could not slove it , 

def Reverse_List(list):
    for i in range(0, (len(list)-1)//2):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list


print(Biggie_Size([-1, 3, 5, -5]))
print(Count_Positives([-1,1,1,1]))
print(Count_Positives([1,6,-4,-2,-7,-2]))
print(Sum_Total([1,2,3,4]))
print(Sum_Total([6,3,-2]))
print(Average([1,2,3,4]))
print(length([37,2,1,-9]))
print(length([]))
print(Min([37,2,1,-9]))
print(Max([37,2,1,-9]))
print(Reverse_List([37,2,1,-9]))