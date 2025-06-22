text = "hello my name is {name} and i'm {age} "

name = input("enter name: ")
age= int(input("enter the age : "))

print(text.format(age = age, name = name))