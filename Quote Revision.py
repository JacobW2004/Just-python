import time


def nocheat(numberoflines):
    for i in range(numberoflines):
        print("No cheating")


score = 0
num = 0
done = 0
quotes = int(input("How many quotes do you want to revise?\n"))
qlist = list()
noqlist = list()
for i in range(quotes):
    quote = input("Input a quote\n").lower()
    qlist.append(quote)
while score < quotes:
    noqlist = list()
    if done == 1:
        print("You got " + str(score) + " out of " + str(quotes))
        time.sleep(3)
    nocheat(50)
    done = 1
    num = 0
    score = 0
    print("\n \n \nQuote test start\n")
    while num < quotes:
        quote = input("Input a quote\n").lower()
        if quote not in noqlist and quote in qlist:
            print("Correct\n")
            score = score + 1
            noqlist.append(quote)
        elif quote in noqlist and quote in qlist:
            print("You already said that one.\n")
        else:
            print("Sorry, that's not a quote.\n")
        num = num + 1
print("Good job! You're done. You know your quotes.")
