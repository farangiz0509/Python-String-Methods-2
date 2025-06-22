text = "today's {date} , lesson at {time} ."
date = input("enter the name of day : ")
time = input("enter the time : ")

print(text.format(date = date, time = time))