class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            age = 0;
        else:
            age = initialAge
    def amIOld(self, age):
        if age < 13:
            print("You are young.")
        elif (age >= 13 and age<18):
            print("You are a teenager.")
        else:
            print("You are old.")# Do some computations in here and print out the correct statement to the console
    def yearPasses(self, age):
        age=age+1# Increment the age of the person in here
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld(age)
    for j in range(0, 3):
        p.yearPasses(age)
    p.amIOld(age)
    print("")
