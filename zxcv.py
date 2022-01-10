indexlist = []
securelist = []
passcord = 1234
commandlist = [
    "exit", "showindex", "showcommand", "sumcalc", "addword", "clearall", "removeword", "entersecure", "say"
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
            calcx = input('X: ')
            calcx = int(calcx)
            calcy = input('Y: ')
            calcy = int(calcy)
            print(calcx+calcy)
        elif word == "addword":
            addword = input("Enter: ")
            indexlist.append(addword)
            print(addword, 'is available')
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

        else:
            print("I don't know this command")
        
def securearea():
    passok = input("Passcord: ")
    passok = int(passok)

    if passok == passcord:
        print("You are Admin")

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
                count+=1
                print(count)
                print(count)
        except KeyboardInterrupt:
            print('Exit')
    else:
        print("OK")



try:
    while True:
        word = input('Enter:')
        
        if word in indexlist:
            wordAction()
        elif word == "exit":
            break
        elif word in commandlist:
            commandAction()
        else:
            wordAction()

except KeyboardInterrupt:
    print('Exit')