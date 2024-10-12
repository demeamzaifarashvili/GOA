#homework: 1
num = 7
print("----------and---------")
print(num >= 3 and num <= 10)
print(num >= 8 and num <= 4)  
print(num > 6 and num <= 9)  
print(num > 5 and num > 10) 
print(num > 9 and num > 11)  

print("-----------or-----------")
print(num >= 1 or num <= 10) 
print(num >= 5 or num <= 4)   
print(num > 7 or num <= 13)
print(num > 8 or num > 9) 
print(num > 6 and num > 9)

#homework: 2
num1 = int(input(" enter number: "))
num2 = int(input("enter second number"))

print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)

#homework: 3
#განხილვა ამ კოდის კომენტარებით რატომ True ან False
num = 5
print("----------- AND -----------")

#როგორ მუშაობს (AND) ოპერატორი:ოპერატორი AND აბრუნებს True-ს თუ
#ორივე სწორია სხვა შემთხვევაში დააბრუნებს False-ს

print(num >= 1 and num <= 10) # True (1.True + 2.True = True)
print(num >= 1 and num <= 4) # False (1.True + 2.False = False)
print(num > 5 and num <= 10) # False (1.False + 2.False = False) 
print(num > 5 and num > 10) # False  (1.False + 2.False = False)

print("----------- OR -----------")

#როგორ მუშაობს (OR) ოპერატორი:OR ოპერატორი აბრუნებს True-ს
#თუ ერთი მაინც არის True თუ ორივე არასწორია დააბრუნებს False-ს

print(num >= 1 or num <= 10) # True  (1.True + 2.True = True) 
print(num >= 1 or num <= 4) # True   (1.True + 2.False = True)
print(num > 5 or num <= 10) # True   (1.False + 2.True = True)
print(num > 5 or num > 10) # False   (1.False + 2.False = False)
 
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False 

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False