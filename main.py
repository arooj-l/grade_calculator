#garde_calculator 

#list to hold all the grades
marks = []

#loop to add marks into the list until user enter done
while True:
    user_input = input("Enter mark or type done: ")
#if user wants to stop
    if user_input.lower() == "done": 
        break 
#try converting input to number
    try:
        mark = float(user_input)
        marks.append(mark)
    except ValueError:
        print("Invalid input. Please enter a number.")

   
#after loop ends
if not marks:
    print("No marks were entered.")
else:
    total = sum(marks)
    print("Total: ", total)
    average = total/len(marks)
    print("Average: ", average)
    #assign grade
    if average >= 90:
        grade = "A" 
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    print("Grade: ", grade)

