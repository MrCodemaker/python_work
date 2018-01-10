spyki = {'kind': 'dog', 'owner': 'john'}
lucky = {'kind': 'cat', 'owner': 'sarah'}
jacky = {'kind': 'rat', 'owner': 'jane'}
hati = {'kind': 'parrot', 'owner': 'matt'}
lori = {'kind': 'hamster', 'owner': 'bill'}

pets = [spyki, lucky, jacky, hati, lori]

for pet_name, pet_info in (pets.items()):
    print("\nPet name: " + pet_name)
    owner = pet_info['owner']
    print("\tOwner: " + owner)
