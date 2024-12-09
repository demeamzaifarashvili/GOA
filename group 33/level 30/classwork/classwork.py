# try da expect gvadgeba errorebis tavidan asarideblad 
# name error 
# index error
# value error

try:
    print("variable")
except NameError as e:
    print(f"NameError  {e}")



try:
    my_list = [8, 6, 3, 8, 8]
    print(my_list[6])  #aq ari index error 6 idex ar gvaqvs

except IndexError as a:
    print(f"IndexError : {a}")


try:
    number = int("deme")  
except ValueError as b:
    
    print(f"ValueError : {b}")
