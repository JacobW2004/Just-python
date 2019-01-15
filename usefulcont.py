class useful:
    def ishigher(string):
        if ord(string) < 91 and ord(string) > 64:
            return True
        else:
            return False

    def islower(string):
        if ord(string) < 123 and ord(string) > 96:
            return True
        else:
            return False

    def isletter(string):
        if (ord(string) < 91 and ord(string) > 64) or (ord(string) < 123 and ord(string) > 96):
            return True
        else:
            return False

    def binary(bin1):
        bin1 = str(bin1)
        tot = 0
        for i in range(1, len(bin1) + 1):
            if bin1[-(i)] == "1":
                tot += 2 ** (i - 1)
        return (tot)

    def caesare(msg, shift):
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
        return ("".join(truemsg))

    def letterfreq(text):
        text = text.lower()
        shift = ord("a")
        abc = []
        for i in range(0, 26):
            abc.append(0)
        for i in range(len(text)):
            if ord(text[i]) - shift < 26 and ord(text[i]) - shift > -1:
                abc[ord(text[i]) - shift] = abc[ord(text[i]) - shift] + 1
        big = 0
        for i in range(0, 25):
            if abc[i] > big:
                big = abc[i]
                tot = i
        return ((tot - tot * 2) + 4)

    def vigenere(msg,word):
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
        return ("".join(truemsg))

    def autocaesar(encrypted):
        return useful.caesare(encrypted,useful.letterfreq(encrypted))