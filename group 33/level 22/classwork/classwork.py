
#1
def exclamation_marks(s: str) -> str:
    return s.replace('!', '')


print(exclamation_marks("Hello World!"))  
print(exclamation_marks("hello world")) 
print(exclamation_marks("hello world"))  
print(exclamation_marks("hello world"))

#2
def hoop_encouragement():
        
        n = int(input("How many times did the hoop go around? "))
        
        if n <= 0:
            print("good")
        elif n < 5:
            print("nice Keep ")
        elif n < 10:
            print("good")
        else:
            print("amazing")


#3

def set_alarm(employed: bool, vacation: bool) -> bool:
    return employed and not vacation

print(set_alarm(True, False))  
print(set_alarm(True, True))   
print(set_alarm(False, False))  
print(set_alarm(False, True)) 