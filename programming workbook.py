from usefulcont import useful
#print(((((1 + 1) ** 5) % 7) - 10) / 2)

# def wow(num):
#     if num < 10:
#         return False
#     else:
#         return True

# print(len(chr(65)))

# print(float(input("wow input a number \n")) + 5)

# num = float(input("input a number \n"))
# print(num + 1)

# words = input("Wow input some words and I'll sort them\n").split()
# print("wow you entered " + str(len(words)) + " words!\nThose words sorted is " +  " ".join(sorted(words)))
#
# words = list()
# for i in range(1,6):
#     words.append(str(input("Wow put a word in\n")))
# print(" ".join(sorted(words))

# income = float(input("Input your monthly income in pounds and pence\n"))
# rent = float(input("Input your monthly rent in pounds and pence\n"))
# print("You will have " + str(12 * (income - rent)) + " left over at the end of the year.")
#
# money = float(input("How much money do you have?\n"))
# if money >= 4:
#     print("Wow you can get fish and chips")
# elif money >= 3:
#     print("You can get fish but no chips")
# elif money >=2:
#     print("You can get chips but no fish")
# else:
#     print("You can't buy anything")
#
# for i in range(4):
#     print("c uwu oim twt\n")
# for i in range(2,4):
#     print("C uwu oim twt\n")
#
# for i in ("herro"):
#     print(i)
#
# for number in range(100):
#     print(number)
# for number in range(10,42):
#     print(number)
# for number in range(10,14):
#     print("this is number " + str(number))
#
# for n in range(1,20,2):
#     print(n)
# for n in range(10,-5,-1):
#     print(n)
#
# people = ["real friend one","real friend two","real friend three"]
# for i in people:
#     print(i)
#
# for i in range(0,3):
#     print(i)
#     print(people[i])

#chal1
# num = int(input("Input a number\n"))
# for i in range(1,num + 1):
#     print(i)
#chal2
# mult = int(input("How many multiples of 3 do you want?\n"))
# for i in range(1,mult + 1):
#     print(i * 3)
#chal3
# times = float(input("Which number's times tables would you like to do?\n"))
# for i in range(1,13):
#     print(i * times)
#chal4
# word = "".join(str(input("input a word\n")).split())
# for i in word:
#     print(i)
#chal5
# wow = []
# words = str(input("input a sentence\n"))
# for i in words:
#     if useful.isletter(i) == True:
#         wow.append("*")
#     else:
#         wow.append(i)
# print("".join(wow))

#chal 1
pas = str(input("What's the password?\n")).lower()
if pas == "flynn":
    print("Access granted")
else:
    print("Access denied")

#chal2
name = str(input("What's your name?\n")).lower()
if name == "flynn":
    print("You're a red face")
elif name == "charlie":
    print("You are amazing")
elif name == "jarvis":
    print("Wow it's Just A Really Very Intelligent System!")
elif name == "Jacob":
    print("You're fat")
else:
    print("I don't know you GET OUT")

#chal3i
num = int(input("Input a positive integer\n"))
numbers = list()
numbers.append(str(num))
while num > 0:
    num = num - 1
    numbers.append(str(num))
print(" ".join(numbers))

#chal3ii
num = int(input("Input a positive integer\n"))
numbers = list()
numbers.append(str(num))
while num > 0:
    num = num - 2
    if num <= 0:
        break
    numbers.append(str(num))
print(" ".join(numbers))

#chal4
sent = str(input("Input a sentence\n")).split()
print(len(sent))

#chal5
msg = str(input("Input your message\n"))
shift = int(input("Input your shift\n"))
truemsg = list()
msglen = len(msg)
num = 0
msginnum = list()
msgnum = 0
for x in range(0, msglen):
    if msg[msgnum].isalpha() == True:
        letter = ord(msg[msgnum])
        if useful.islower(chr(letter)) == True:
            letter = letter + shift
            while letter > 122:
                letter -= 26
            while letter < 96:
                letter += 26
        elif useful.ishigher(chr(letter)) == True:
            letter = letter + shift
            while letter > 90:
                letter -= 26
            while letter < 65:
                letter += 26
        msginnum.append(int(letter))
    else:
        msginnum.append(ord(msg[msgnum]))
    msgnum += 1
while num != msglen:
    if msginnum[num] > 95 and msginnum[num] < 123:
        letter = msginnum[num]
        truemsg.append(chr(letter))
    else:
        truemsg.append(chr(msginnum[num]))
    num += 1
print("".join(truemsg))

#chal6
msg = str(input("Input your message\n"))
word = int(input("Input your encoding word\n"))
truemsg = list()
msglen = len(msg)
while len(word) < len(msg):
    word = word + word
num = 0
msginnum = list()
msgnum = 0
for x in range(0, msglen):
    if msg[msgnum].isalpha() == True:
        letter = ord(msg[msgnum])
        shift = ord(word[x]) - 96
        if useful.islower(chr(letter)) == True:
            letter = letter + shift
            while letter > 122:
                letter -= 26
            while letter < 96:
                letter += 26
        elif useful.ishigher(chr(letter)) == True:
            letter = letter + shift
            while letter > 90:
                letter -= 26
            while letter < 65:
                letter += 26
        msginnum.append(int(letter))
    else:
        msginnum.append(ord(msg[msgnum]))
    msgnum += 1
while num != msglen:
    if msginnum[num] > 95 and msginnum[num] < 123:
        letter = msginnum[num]
        truemsg.append(chr(letter))
    else:
        truemsg.append(chr(msginnum[num]))
    num += 1
print("".join(truemsg))