#garde_calculator 

#list to hold all the grades
marks = []

#loop to add marks into the list until user enter done
while True:
    user_input = input("Enter mark or type done: ")
#Error Handling, if the user types any string (abc ...)
    if user_input.lower() == "done": #if user enter upper case
        break
    
    try:
        mark = float(user_input)
        marks.append(mark)
    except ValueError:
        print("Invalid input. Please enter a number.")

   
#test to see if list contains all teh element
#print(marks)

total = sum(marks)

print(total)


