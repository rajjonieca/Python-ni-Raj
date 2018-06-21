import os
import sys

my_dict = {'Name':'Joyce',
           'School':'AU',
           'Age':20}

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

for key in my_dict:
    print(key, my_dict[key])


#List Comprehension
even_squares = [i ** 2 for i in range(1,11) if i % 2 == 0]

print(even_squares)

#Cubes by Four

cubes_by_four = [i ** 3 for i in range(1,11) if ((i ** 3) % 4) == 0]

print(cubes_by_four)