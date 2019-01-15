import time
from random import randint


def nocheat(numberoflines):
    for i in range(numberoflines):
        print("No cheating")


score = 0
num = 0
done = 0
qs = int(input("How many questions do you want to do?\n"))
rqs = qs - 1
qlist = list()
alist = list()
dlist = list()
dalist = list()
temp = 0
noqlist = list()
for i in range(qs):
    question = input("Input a question\n").lower()
    qlist.append(question)
    answer = input("Input the answer\n").lower()
    alist.append(answer)
while score < qs:
    if done == 1:
        print("You got " + str(score) + " out of " + str(qs))
        time.sleep(2)
    nocheat(20)
    done = 1
    num = 0
    dlist = list()
    while num < qs:
        num += 1
        temp = randint(0,rqs)
        while temp in dlist:
            temp = randint(0, rqs)
        dlist.append(temp)
        print(qlist[temp])
        ans = input().lower()
        if ans == alist[temp]:
            score += 1
            print("Correct")
            dalist.append(ans)
        else:
            print("Incorrect")
print("You got them all correct")