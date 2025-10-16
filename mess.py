logoff = False
blocked = [[False,False,False]]
friends = [["Ross","Bob","Anders"]]
sentMessage = [[[],[],[]]]
recievedMessage = [[["Are we stil on for saturday?"],["Are you doing alright"],["I didn't do the homework, please let me copy"]]]

#List containing existing account and new account info
username = ["Adrian"]
age = ["16"]
password = ["pizza123"]


while logoff == False:
    print("\n********************************************************")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    validateChoice = False
    while validateChoice == False:
        try:
            task = int(input("Please Choose a number: "))
            if task < 4 and task > 0:
                validateChoice = True
            else:
                print("Invalid Input")
        except:
            print("Invalid Input")

    if task == 1:
        newName = input("Type in the username for your new account: ")
        validAge = False
        while validAge == False:
            try:
                newAge = int(input("Type in your current age for your new account: "))
                if newAge <= 0 or newAge > 120:
                    print("Invalid Age\n")
                else:
                    validAge = True
            except:
                print("Invalid Input")
        newPassword = input("Type in the password for your new account: ")
        username.append(newName)
        age.append(newAge)
        password.append(newPassword)
        blocked.append([])
        friends.append([])
        sentMessage.append([[]])
        recievedMessage.append([[]]) #JUST IN CASE
        print("\nConfirmed, returning to Main Menu...\n")
    
    if task == 2:
        validAccount = False
        while validAccount == False:
            try:
                print("\nType in the number for the account you'd like to manage: ")
                count = 1
                for i in range(len(username)):
                    print(str(count) + ". " + str(username[i]))
                    count += 1
                whichAccount = int(input())
                if whichAccount > len(username) or whichAccount <= 0:
                    print("Invalid Account")
                else:
                    validAccount = True 
                    whichAccount -= 1
                    print("\nConfirmed\n")
            except:
                print("Invalid Account")

        goback = False
        while goback == False:
            chosenOption = False
            while chosenOption == False:
                try:
                    print("")
                    print("1. Edit my details")
                    print("2. Add a friend")
                    print("3. View all my friends")
                    print("4. View all my messages")
                    print("5. Block/Unblock Friends")
                    print("6. <- Go back ")
                    whichManage = int(input("Please Choose a number: "))
                    if whichManage >= 1 and whichManage <= 6:
                        chosenOption = True
                    else:
                        print("Invalid Input")
                except:
                    print("Invalid Input")

            if whichManage == 6: 
                goback = True

            elif whichManage == 1: #changing details
                print("\nHere are your current details:\n","Username:",username[whichAccount],"\nAge:",age[whichAccount],"\nPassword:",password[whichAccount])
                newName = input("\nType in the new username for your account: ")
                validAge = False
                while validAge == False:
                    try:
                        newAge = int(input("Type in the new age for your account: "))
                        if newAge <= 0 or newAge > 120:
                            print("Invalid Age\n")
                        else:
                            validAge = True
                    except:
                        print("Invalid Input\n")
                newPassword = input("Type in the new password for your account: ")
                username[whichAccount] = newName
                age[whichAccount] = newAge
                password[whichAccount] = newPassword
                print("\nConfirmed, returning to Account Management Menu...\n")

            elif whichManage == 2: #adding friends
                newFriend = input("\nType in the username of the friend you want to add: ")
                friends.append([]) #prevents index error
                sentMessage.append([[]])
                temp = sentMessage[whichAccount]
                temp.append([])
                sentMessage[whichAccount] = temp
                recievedMessage.append([[]]) 
                temp = recievedMessage[whichAccount]
                temp.append([])
                recievedMessage[whichAccount] = temp 
                blocked.append([])
                blockedFriends = blocked[whichAccount]
                blockedFriends.append(False)
                blocked[whichAccount] = blockedFriends
                addedFriends = friends[whichAccount]
                addedFriends.append(newFriend)
                friends[whichAccount] = addedFriends 
                print("\nConfirmed, returning to Account Management Menu...\n")
            
            elif whichManage == 3: 
                print("\nHere are your list of friends: \n")
                if len(friends[whichAccount]) == 0:
                    print("\nYou have no friends, returning to Account Management Menu...\n")
                else:
                    count = 1
                    for i in range(len(friends[whichAccount])):
                        print(str(count) + ". " + str(friends[whichAccount][i]))
                        count += 1
                print("")
                exitFriends = "a" #placeholder to reset input
                exitFriends = input("Type in x to return to Account Management Menu (<---) ")
                returntoMM = False
                while returntoMM == False:
                    if exitFriends == "x":
                        returntoMM = True
                        print("\nConfirmed, returning to Account Management Menu...\n")
                    else:
                        print("Invalid Input")
                        exitFriends = input()

            elif whichManage == 4: #messaging system
                finishedchat = True
                if len(friends[whichAccount]) == 0: #checks if they have friends
                    print("\nYou don't have any friends, returning to Account Management Menu...\n")
                else:
                    validFriend = False
                    while validFriend == False: #Lets them type in the friend they would like to message
                        try:
                            print("\nType in the number for the friend you would like to message:\n(Type [0] to exit to Account Management Menu)") #CHANGE THIS AREA SO THEY CAN EXIT
                            count = 1
                            for i in range(len(friends[whichAccount])):
                                print(str(count) + ". " + str(friends[whichAccount][i]))
                                count += 1
                            chatFriend = int(input())
                            if chatFriend == 0:
                                print("\nConfirmed\n")
                                validFriend = True
                            elif chatFriend >= 1 and chatFriend <= len(friends[whichAccount]) and blocked[whichAccount][(chatFriend-1)] == False:
                                validFriend = True
                                print("\nConfirmed\n")
                                chatFriend -= 1 
                                finishedchat = False 
#u need to somehow add a specific recievedmessage and sent message position 
                            else:
                                print("Invalid Input or the person you are trying to message is blocked\n")
                        except:
                            print("Invalid Input\n")

                    while finishedchat == False:
                        print("(\nType in [*exit] to return to the Account Management Menu (<--)\n")    
                        print(friends[whichAccount][chatFriend])
                        print("********************************************************\n")

                        if len(recievedMessage[whichAccount][chatFriend]) == 0: #prints out all the messages people have sent you
                            print("You have no messages\n")
                        else: 
                            for i in range(len(recievedMessage[whichAccount][chatFriend])):
                                print(str(friends[whichAccount][chatFriend]) + ": " + str(recievedMessage[whichAccount][chatFriend][i]))

                        if len(sentMessage[whichAccount][chatFriend]) == 0: #prints out all the messages you have sent them 
                            placeholder = 3 #essentially do nothing and not print an empty list
                        else: 
                            for i in range(len(sentMessage[whichAccount][chatFriend])):
                                print("You: " + str(sentMessage[whichAccount][chatFriend][i]))
                        print("")
                        sendtext = input("Type in what you want to send... ")
                        if sendtext == "*exit":
                            finishedchat = True
                            print("\nConfirmed, returning to Account Management Menu...\n")
                        else:
                            addtoOGtext = sentMessage[whichAccount][chatFriend]
                            addtoOGtext.append(sendtext)
                            sentMessage[whichAccount][chatFriend] = addtoOGtext
            
            elif whichManage == 5:
                print("Type in x to return to Account Management Menu (<---) \n")
                print("Here are your list of friends: ")
                if len(friends[whichAccount]) == 0:
                    print("\nYou have no friends\n")
                else:
                    count = 1
                    for i in range(len(friends[whichAccount])):
                        print(str(count) + ". " + str(friends[whichAccount][i]))
                        count += 1
                    doneBlocked = False
                    while doneBlocked == False:
                        try:
                            numBlocked = int(input("Type in the number of the user you want to block or [0] to return to Account Management Menu\n"))
                            if numBlocked == 0:
                                doneBlocked = True
                            elif int(numBlocked) >= 1 and numBlocked <= len(friends[whichAccount]):
                                numBlocked -= 1 #fixes index
                                if blocked[whichAccount][numBlocked] == False:
                                    blocked[whichAccount][numBlocked] = True
                                    print("\nThe user has been blocked\n")
                                else:
                                    blocked[whichAccount][numBlocked] = False
                                    print("\nThe user has been unblocked\n")
                            else:
                                print("Invalid Input\n")
                        except:
                            print("Invalid Input")

    if task == 3:
        print("Successfully logged off")
        logoff = True
