import webbrowser

indexlist = ["FirstIndex"]
securelist = []
passcord1 = 1234
zxcvversion = "0.1.0"
commandlist = [
    "exit",
    "showindex",
    "showcommand",
    "sumcalc",
    "addword",
    "clearall",
    "removeword",
    "entersecure",
    "say",
    "chatbot",
    "zxcv --version",
    "openwebsite",
    "getindexnumber",
    "showreplaylist",
    "addreplay",
    "wordloop"
]
chatbotlist = [
    "hello", "hi!",
    "hey siri", "What????????",
    "ping", "pong"
]
securemessage = ""

def wordAction():
    if word in indexlist:
        print(word, 'was already added')
    else:
        print(word, 'is not added to index')
        print('Do you want to add index?')
        addqu = input('Y/n: ')
        if addqu == "Y":
            indexlist.append(word)
            print(word, 'is available')
        else:
            print("OK")


def commandAction():
    if word in commandlist:
        if word == "showindex":
            print(indexlist)
        elif word == "showcommand":
            print(commandlist)
        elif word == "sumcalc":
            sumcalc()
        elif word == "addword":
            addword()
        elif word == "removeword":
            removeword()
        elif word == "clearall":
            print("Do you want to clear all?")
            clearqu = input('Y/n: ')
            if clearqu == "Y":
                indexlist.clear()
                print("Success!")
            else:
                print("OK")
        elif word == "entersecure":
            securearea()
        elif word == "say":
            say()
        elif word == "chatbot":
            chatbot()
        elif word == "zxcv --version":
            print(zxcvversion)
        elif word == "openwebsite":
            openwebsite()
        elif word == "showreplaylist":
            print(chatbotlist)
        elif word == "getindexnumber":
            getindexnumber()
        elif word == "addreplay":
            addreplay()
        elif word == "wordloop":
            wordloop()

        else:
            print("Don't know this command")

def sumcalc():
    calcx = input('X: ')
    calcx = int(calcx)
    calcy = input('Y: ')
    calcy = int(calcy)
    print(calcx+calcy)

def addword():
    addword = input("Enter: ")
    if addword in indexlist:
        print(addword, "is already added")
    else:
        indexlist.append(addword)
        print(addword, "is added")

def removeword():
    removeword = input('Enter: ')
    if removeword in indexlist:
        print("Do you want to remove", removeword, "?")
        clearqu = input('Y/n: ')
        if clearqu == "Y":
            indexlist.remove(removeword)
            print("Success!")
        else:
            print("Stopped remove")
    else:
        print(removeword, 'is not in index')

def securearea():
    passok = input("Passcord: ")
    passok = int(passok)
    if passok == passcord1:
        print("Login!")
        securemessage = "None"
        while True:
            secureword = input('Secure: ')
            if secureword == "exit":
                print("Transh and exit!")
                break
            elif secureword == "addmessage":
                securemessage = input('EnterMessage: ')
                print("Success!")
            elif secureword == "showmessage":
                    print(securemessage)
            elif secureword == "erasemessage":
                print("Do you want to erase?")
                surequ = input('Y/n: ')
                if surequ == "Y":
                    securemessage = ""
                    print("Success!")
                else:
                    print("Not erase")
            elif secureword == "":
                None
            else:
                print("Not found", secureword)
            
        
    else:
        print("Incorrect")

def say():
    word2 = input('Say Word: ')
    print("Do you know what to happen?")
    surequ = input('Y/n: ')
    if surequ == "Y":
        count = 0
        try:
            while True:
                print(count, word2)
                count += 1
                print(count)
                print(count)
        except KeyboardInterrupt:
            print('Exit')
    else:
        print("OK")

def openwebsite():
    url = input("EnterURL: ")
    webbrowser.open(url)

def chatbot():
    print("Welcome to chat bot!")
    while True:
        talk = input('Your message: ')
        talk = talk.lower()
        if talk == "exit":
            break
        elif talk in chatbotlist:
            replay1 = chatbotlist.index(talk)+1
            print("Bot message:",chatbotlist[replay1])
        else:
            print("Bot message: ??????????????? ????????????????????????")


def getindexnumber():
    print("indexlst")
    print(indexlist)
    getword = input('Word: ')
    if getword in indexlist:
        print(indexlist.index(getword))
    else:
        print(getword,"is not added to index")

def addreplay():
    sendmessage = input("Send Message: ").lower()
    replaymessage = input("Replay Message: ").lower()
    if sendmessage in chatbotlist:
        print(sendmessage, "is already added")
    elif replaymessage in chatbotlist:
        print(sendmessage, "is already added")
    else:
        chatbotlist.append(sendmessage)
        chatbotlist.append(replaymessage)
        print("Success!")

def wordloop():
    loopword = input('Loop Word: ')
    print("How many loops?")
    loop = input('loop: ')
    loopx = input('loop2: ')
    loop = int(loop)
    loopx = int(loopx)
    count = 1
    for i in range(loop*loopx):
        print(count, loopword)
        count += 1

def normalchat():
    chattext = word.replace('\c', ' ')
    chattext = chattext.lstrip()
    if chattext in chatbotlist:
            replay1 = chatbotlist.index(chattext)+1
            print("Bot message:",chatbotlist[replay1])
    else:
        print("Bot message: ??????????????? ????????????????????????")

try:
    print("Welcome to zxcv")
    while True:
        word = input('zxcv:')
        if word == "":
            None
        else:
            if word == "exit":
                break
            elif "\c" in word:
                normalchat()
            elif word in commandlist:
                commandAction()
            else:
                wordAction()

except KeyboardInterrupt:
    print('Exit')
