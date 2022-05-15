#Write your code below this line 👇
def prime_checker(number):
    divideByOne = 0
    divideBySelf = 0
    divideByOther = 0
    
    for i in range(1, number + 1):
        if i == 1:
            if number%1 == 0:
                divideByOne = 1
                #print("divisible by 1")
        if i == number:
            if number%i == 0:
                divideBySelf = 1
                #print("divisible by self")
        if (i != 1) and (i != number):
            if number%i ==0:
                divideByOther = 1
                #print(f"divisible by another number {i}")

    if divideByOne == 1 and divideBySelf == 1 and divideByOther == 1:
        print("It's not a prime number.")
    elif divideByOne == 1 and divideBySelf == 1 and divideByOther == 0:
        print("It's a prime number.")
