prompt = "\nPlease enter the your age to know the price of the ticket:")

active = True
while active:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("The ticket is free!")
    elif (age >= 3) and (age <= 12):
        print("The ticket costs 10$")
    elif age > 12:
        print("The ticket costs 15$")
    elif age == 'quit':
        break
    elif age == 'quit':
        active = False
    else:
        print("You're either too young or too old!")
