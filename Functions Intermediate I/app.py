import random
def randInt(min= 50 , max= 50 ):
    num = random.random()
    return num
print(randInt())


import random
def randInt(min= 50 , max= 50 ):
    num = random.random()
    return random.random() * 50
print(randInt(max=50)) 

import random
def randInt(min= 50 , max= 50 ):
    num = random.random()
    return random.random() * 25 + 10
print(randInt(min=50))

import random
def randInt(min= 50 , max= 50 ):
    num = random.random()
    return round(num)
print(randInt(min=50, max=500)) 