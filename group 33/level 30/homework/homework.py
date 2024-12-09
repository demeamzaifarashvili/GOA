def list (numbers):
    total = 0
    for num in numbers:
        if isinstance(num, str): 
            total += int(num)  
        else:
            total += num  
    return total