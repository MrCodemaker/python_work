responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where would you like to holiday?")

    responses[name] = response

    repeat = input("Whould you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to spend the holiday in " + response + ".")
