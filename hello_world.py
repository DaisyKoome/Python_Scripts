# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 17:40:58 2018

@author: Daisy
"""
print("Hello Python world!")

message="Hello python world!"
print(message)

message="Hello Python Crash Course world!"
print(message)

message="My name is Daisy Koome"
print (message)

name="ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())

first_name="ada"
last_name="lovelace"
full_name=first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message="Hello, "+full_name.title()+"!"
print(message)

print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language=' python'
print(favorite_language)
favorite_language=favorite_language.lstrip()
print(favorite_language)

message="One of Python's strengths is its diverse community"
print(message)


print('2+2=',2+2)
print('2+3*4=',2+3*4)
print('(2+3)*4=',(2+3)*4)
print('3**2=',3**2)
print('3*0.1=',3*0.1)

age=23
message="Happy "+str(age)+"rd birthday!!"
print(message)

bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[1])
print(bicycles[3].title())
print(bicycles[-2])

message="My first bicycle was a "+(bicycles[2].upper())+"."
print(message)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0,'kamikaze')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle=motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

last_owned=motorcycles.pop()
print("The last motorcycle I owned was a "+last_owned.title()+".")

motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(1)
print("The first motorcycle I owned was a "+first_owned.title()+".")

motorcycles=['honda','yamaha','suzuki']
motorcycles.remove('suzuki')
print(motorcycles)

Too_expensive='honda'
motorcycles.remove(Too_expensive)
print("\nA "+Too_expensive.title()+" is too expensive for me.")

cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)


print("\nHere is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)

cars.reverse()
print(cars)
cars.reverse()

len(cars)
print("Length= "+str(len(cars))+ ".")



magicians=['alice','david','carolina']
for magician in magicians:
    print("\n"+magician)
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick, "+magician.title()+".\n")
    
for value in range(1,6):
    print(value)
    
numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)


digits=[1,2,3,4,5,6,7,8,9,0]    
Minimum=min(digits)
print(Minimum)

Maximum=max(digits)
print(Maximum)

Total=sum(digits)
print(Total)


squares=[value**2 for value in range(1,11)]
print(squares)


players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players in my team:")
for player in players[:3]:
    print(player.title())
    

my_foods=['pizza','falafel','carrot cake']
friends_foods=my_foods[:]
print(my_foods)
print("My favorite foods are: "+str(my_foods)+".")
print("\nMy friend's favorite foods are: "+str(my_foods)+".")
    
    






