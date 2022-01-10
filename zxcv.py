import webbrowser

indexlist = []
securelist = []
passcord = 1234
zxcvversion = "0.1.0"
commandlist = [
    "exit", "showindex", "showcommand", "sumcalc", "addword", "clearall", "removeword", "entersecure", "say", "chatbot", "zxcv --version", "openwebsite", "getindexnumber"
]
chatbotlist = [
    "hello", "hi!",
    "hey siri", "What????????"
]

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
            removeword = input('Enter: ')
            if removeword in indexlist:
                clearqu = input('Y/n: ')
                if clearqu == "Y":
                    indexlist.remove(removeword)
                    print("Success!")
                else:
                    print("OK")
            else:
                print(removeword, 'is not in index')
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
        elif word == "getindexnumber":
            getindexnumber()

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

def securearea():
    securemessage = "None"
    passok = input("Passcord: ")
    passok = int(passok)
    if passok == passcord:
        print("You are Admin")
        while True:
            secureword = input('Secure: ')
            if secureword == "exit":
                break
            elif secureword == "addmessage":
                securemessage = input('EnterMessage: ')
                print("Success")
            elif secureword == "showmessage":
                print(securemessage)
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

def changepasscord():
    nowpasscord = input("Current Passcord: ")
    nowpasscord = int(nowpasscord)
    if nowpasscord == passcord:
        newpasscord = input("New Passcord: ")
        newpasscord2 = input("Confirm")
    else:
        print("Current Passcord is incorrect")


def chatbot():
    print("Welcome to chat bot!")
    while True:
        talk = input('Enter message: ')
        talk = talk.lower()
        if talk == "exit":
            break
        elif talk in chatbotlist:
            replay1 = chatbotlist.index(talk)+1
            print(chatbotlist[replay1])
        else:
            print("すみません よくわかりません")


def getindexnumber():
    print("indexlst")
    print(indexlist)
    getword = input('Word: ')
    if getword in indexlist:
        print(indexlist.index(getword))
        print(indexlist.index(getword))
    else:
        print(getword,"is not added to index")


try:
    print("Welcome to zxcv")
    while True:
        word = input('zxcv:')
        if word == "":
            None
        else:
            if word == "exit":
                break
            elif word in commandlist:
                commandAction()
            else:
                wordAction()

except KeyboardInterrupt:
    print('Exit')
