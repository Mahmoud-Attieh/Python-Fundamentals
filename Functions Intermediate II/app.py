x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0]=15 # x will be change 10 to 15
students[0]['last_name'] = 'Brayent' # will be chnage to bray
sports_directory['soccer'][0]='Andres' # messi to andres
z[0]['y']=30 # y change from 20 to 30

print(x)
print(students[0])
print(sports_directory)
print(z)

#2 , we must to creat a func iterateDictionary(some_list)
# just for students

def iterateDictionary(some_list):
    import random
    random_number=random.randint(0,len(some_list))
    print(some_list[random_number])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 


#3
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2('first_name',students) 


#4 

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]),key)
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])
        print("")

dojo = {'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)













