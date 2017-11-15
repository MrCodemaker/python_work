guests = ['steve jobs', 'mark zuckerberg', 'steve wozniak', 'bill gates']

print("Mr " + guests[0].title() + " i would like to invite you for dinner")
print("Mr " + guests[1].title() + " i would like to invite you for dinner")
print("Mr " + guests[2].title() + " i would like to invite you for dinner")
print("Mr " + guests[3].title() + " i would like to invite you for dinner")

print("\nUnfortunately Mr " + guests[1].title() + " will not be able!")

could_not_come = guests.pop(1).title() 
print(guests)
print(could_not_come)

guests.insert(1, 'guido van rossum')
print(guests)

print("\nMr " + guests[0].title() + " i would like to invite you for dinner")
print("\nMr " + guests[1].title() + " i would like to invite you for dinner")
print("\nMr " + guests[2].title() + " i would like to invite you for dinner")
print("\nMr " + guests[3].title() + " i would like to invite you for dinner")

print("\nThe dinner was joined by three more guests")

guests.insert(0, 'gabe newell')
guests.insert(2, 'pavel durov')
guests.append('linus torvalds')

print("\nMr " + guests[0].title() + " i would like to invite you for dinner")
print("\nMr " + guests[1].title() + " i would like to invite you for dinner")
print("\nMr " + guests[2].title() + " i would like to invite you for dinner")
print("\nMr " + guests[3].title() + " i would like to invite you for dinner")
print("\nMr " + guests[4].title() + " i would like to invite you for dinner")
print("\nMr " + guests[5].title() + " i would like to invite you for dinner")
print("\nMr " + guests[6].title() + " i would like to invite you for dinner")

print(guests)
print("\nI offer my deepest apologies, but unfortunately only 2 people can come to dinner")

could_not_come = guests.pop().title()

print("\nMr " + guests.pop().title() + " i'm sorry to cancel the invitation!")
print("\nMr " + guests.pop().title() + " i'm sorry to cancel the invitation!")
print("\nMr " + guests.pop().title() + " i'm sorry to cancel the invitation!")
print("\nMr " + guests.pop().title() + " i'm sorry to cancel the invitation!")

print(guests)

print("\nMr " + guests[0].title() + " an earlier invitation remains in effect!")
print("\nMr " + guests[1].title() + " an earlier invitation remains in effect!")

del guests[0]
del guests[0]

print(guests)
