def factorial(reeeee):
    rhe = 2
    rhee = 1
    while rhe <= reeeee:
        rhee *= rhe
        rhe += 1
    return(rhee)

defactor = int(input("Enter the number that you want to de-factor\n"))
num = 1
number = 1
while defactor / number != 1:
    num += 1
    number = factorial(num)
print(str(defactor) + " defactorial'd is " + str(num))