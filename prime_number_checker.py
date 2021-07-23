
# coding exercise - prime number checker

# def prime_checker(number):
#     if number % 2 == 1:
#         print(f"this {number} is a prime number")
#     elif number == 2:
#         print(f"This {number} is a prime number")
#     else:
#         print(f"This {number} is not a prime number")

# alternatively

def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            # Not prime
            is_prime = False
            print(i)
            # print("This is not a prime number")            
    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")
    

n = int(input("Check this number: "))
prime_checker(number = n)