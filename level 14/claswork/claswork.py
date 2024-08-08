#1
sum_odd = 0
for num in range(1, 11, 2):
    sum_odd += num
print(sum_odd)

sum_multiples_of_5 = 0

#2
for num in range(0, 101, 5):
    sum_multiples_of_5 += num
print( sum_multiples_of_5)


#3
for num in range(20, -1, -1):
    print(num)

#4
num = 0      
even = 0   
while num <= 10:
    if num % 2 == 0:
        even += num
    num += 1
print(even)  

#5
num = 1        
odd = 0   
while num <= 10:
    odd += num
    num += 2
print(odd)

#6
num = 20
while num >= 0:
    print(num)
    num -= 1