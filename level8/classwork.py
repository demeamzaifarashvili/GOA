#classwork: 1
pasword_1 = input("please enter your pasword: " )
pasword_2 = input("please reenter your pasword: ")

print(pasword_1 == pasword_2)

#classwork: 2
num = int(input("please enter number:  "))

print(num > 5 or num <= 10)

#classwork: 3
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False 

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # Fals

#classwork: 4
num = 5

print("----------- AND -----------")

print(num >= 1 and num <= 10) # True 
print(num >= 1 and num <= 4) # False 
print(num > 5 and num <= 10) # False 
print(num > 5 and num > 10) # False  

print("----------- OR -----------")

print(num >= 1 or num <= 10) # True
print(num >= 1 or num <= 4) # True
print(num > 5 or num <= 10) # True
print(num > 5 or num > 10) # False

