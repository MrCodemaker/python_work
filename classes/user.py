class User():
    def _init_(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + last_name
        self.age = age

    def describe_user(self):
        print("User name is " + self.full_name.title() + ".")
        print("He is " + str(self.age) + " yers old!")

    def greet_user(self):
        print("Hello, dear " + self.full_name.title() + "!")


user_1 = User('jason', 'momoa', 39)
print(user_1.describe_user())
print(user_1.greet_user())

user_2 = User('john', 'ortiz', 50)
print(user_2.describe_user())
print(user_2.greet_user()

     