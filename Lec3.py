'''
Lec3

List and Set
'''

my_list = [ 1,2,3,4,5 ]

print(type(my_list))

my_nested_list= [1,2,3,my_list]
print(my_nested_list)

my_list[0]=6

print(my_list)

print(my_list[:])

x,y,z =['a','b','c']
print(x)

my_list.append(7)
print(my_list)

my_list.remove(5)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print(my_list + [8,9])

my_list.extend([8,9])
print(my_list)

print( 9 in my_list)

print(len(my_list))

print(len( my_nested_list))

print('hello world.'[0])

my_letters = ['a','a','b', 'b', 'c']
print(my_letters)

print(set( my_letters ))

my_letters_set = set( my_letters )

print('d' in my_letters_set)

print(list(my_letters_set)[0])
