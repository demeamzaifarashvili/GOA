import random

lottery_number = random.randint(1, 100)
print(f"number lattary: {lottery_number}")

if lottery_number == 6:
    print("tou won house")
elif lottery_number == 30:
    print("you won ticket!")
else:
    print("you won 1 dollar.")



age = int(input("enter age: "))
is_student = input("status (yes/no): ").strip().lower()

if age < 18 or is_student == 'yes':
    print("sale")
else:
    print("not sale")