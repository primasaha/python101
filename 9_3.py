class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print("User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print()

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!\n")


user1 = User("Prima", "Saha", 28, "prima.saha@gmail.com", "New York")
user2 = User("Hanna", "Islam", 35, "hanna.islam@gmail.com", "London")
user3 = User("Nazme", "Chan", 22, "nazme.chan@gmail.com", "Toronto")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()