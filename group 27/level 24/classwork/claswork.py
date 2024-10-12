def even_list(number_list):
    res_list = []

    for num in number_list:
        if num%2 == 0:
            res_list.append(num)
        return res_list
    print(even_list([1,2,3,4,5,6,7,8,9]))    


def string_func(string_list):
    res_list = []

    for string in string_list:
        if len(string) <= 4:
            res_list.append(string)

            return res_list
        print(string_func(["hello" "gio" "nika" "func" "shsywugsuw"]))

def prime_chck(user_num):
    is_prime = True

    for i in range(2,user_num):
        if user_num%1 == 0:
            is_prime = False
    return is_prime
print(prime_chck(10))
