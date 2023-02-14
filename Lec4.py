'''
Lecture 4 
Dictionary and Tuple
'''

my_tuple = ('a', 'b', 'c', 'd', 'e')

#my_tuple[0]= 'f' cannot change tuple
print( type(my_tuple[0]))

#my_tuple = ('a') not a tuple 
#my_tupe = ('a',) a tuple due to the comma 

my_car = {
    'color': 'red', 
    'maker': 'toyota',
    'year': 2015
}
print(my_car)

print(my_car['year'])

print(my_car.items())

print(my_car.values())

print(my_car.get('color'))
print(my_car['color'])
#27 and 28 are the same 

my_car['model'] = 'venza' #adding a new value into dictionary
print(my_car)

my_car['year'] = 2020 #replacing a value in dictionary 
print(my_car)

print( len(my_car) ) #states the number of key value pairs

print( 'red' in my_car) #false because 'red' is a value and is not a key 'color' would be true 

print( 'red' in my_car.values() )

