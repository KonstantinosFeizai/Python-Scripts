# Classes are a way to bundle data and functionality together.
# Creating a new class creates a new type of object, from which new instances can be instantiated.


# A class is a blueprint for creating objects. Objects are instances of classes.
class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed}"

    def bark(self):
        print(f"{self.name} says Woof!")

    def dog_breed(self):
        print(f"{self.name} is a {self.breed}")


class Employee:

    # Class variable
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay, dog=None):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        self.dog = dog  # Instance variable for the dog's name
        Employee.num_of_emps += 1  # Increment the class variable for each new instance

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def show_dog(self):
        if self.dog:
            print(f"{self.first} has a dog named {self.dog}.")
        else:
            print(f"{self.first} does not have a dog.")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod
    def display_all_employees(cls, employees):
        print("\nList of Employees:")
        for emp in employees:
            print(f"{emp.fullname()} - Email: {emp.email} - Pay: {emp.pay}")
        print("")


# creating an object of the class Dog
my_dog = Dog("Buddy", 5, "Golden Retriever")
my_dog2 = Dog("Max", 3, "Poodle")
my_dog3 = Dog("Charlie", 2, "Beagle")

# creating an object of the class Employee
emp_1 = Employee('John', 'Doe', 50000, my_dog)
emp_2 = Employee('Jane', 'Smith', 60000, my_dog2)
emp_3 = Employee('Jim', 'Brown', 70000)
emp_4 = Employee('Alice', 'Johnson', 80000)

emps = [emp_1, emp_2, emp_3, emp_4]
Employee.display_all_employees(emps)

print("--------------------")

dogs = [my_dog, my_dog2, my_dog3]
# Loop through the list of dogs and call their methods
for dog in dogs:
    print(dog)
    dog.bark()
    dog.dog_breed()
    print("")

print("--------------------")
# loop through the list of employees and call their methods
for emp in emps:
    print(emp.fullname())
    emp.show_dog()
    print("")

print("--------------------")

while True:
    # Ask the user if they want to increase the pay
    answer = input(
        "Do you want to increase the pay? (yes/no): ").strip().lower()
    if answer == 'yes':
        while True:
            try:
                # Ask for the raise amount
                amount = float(
                    input("Enter the raise amount (e.g., 1.05 for 5% increase): "))

                # Validate the raise amount
                if amount <= 0:
                    print("Raise amount must be greater than 0. Please try again.")
                elif amount > 2:
                    print(
                        "Raise amount must be less than or equal to 2. Please try again.")
                else:
                    # Apply the raise if the input is valid
                    Employee.raise_amount = amount
                    for emp in emps:
                        emp.apply_raise()
                    print(f"New raise amount is: {Employee.raise_amount}")
                    break  # Exit the inner loop after successful input
            except ValueError:
                print("Invalid input. Please enter a valid number for the raise amount.")
        break  # Exit the outer loop after processing the raise
    elif answer == 'no':
        print("No increases in pay at this time.")
        break  # Exit the loop if the user chooses not to increase pay
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("--------------------")
# Sort employees by pay in ascending order
sorted_emps = sorted(emps, key=lambda emp: emp.pay, reverse=True)

# Display all employees ordered by pay
Employee.display_all_employees(sorted_emps)
print("---------------------")
