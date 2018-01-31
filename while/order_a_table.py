seats = input("How many seats do you want to reserve a table?")
seats = int(seats)

    if seats > 8:
        message = "Unfortunately, you will have to wait until such"
        message += " a number of seats is available"
        print(message)
    else:
        print("You table is ready!")
