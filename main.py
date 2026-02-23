#garde_calculator 

#list to hold all the grades
marks = []

#loop to add marks into the list until user enter done
while True:
    user_input = input("Enter mark or type done: ")

    if user_input == "done":
        break

    marks.append(float(user_input))
#test to see if list contains all teh element
#print(marks)

total = sum(marks)

print(total)


