num1 = float(input("enter number: "))
num2 = float(input("enter number: "))

po = num1 + num2
dif = num1 - num2
pro = num1 * num2
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = ""


print("plus:", po)
print("minus:", dif)
print("gamravleba:", pro)
print("gayofa :", quotient)





price__item = float(input("enter price: "))
quantity = int(input("enter how many: "))

total = price__item * quantity


print("unda gadaixadot:", total)