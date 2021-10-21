from tinydb import TinyDB, Query, where
from crmDjango.Back.user import User
from crmDjango.Back.alphabet import Alphabet
import json

class  Controller(object):

    
    usersDb = TinyDB('crmDjango//usersDb.json')
    userQuery = Query()
    users = []
    charList = []
        

    def __init__():
        Controller.dbToUsers()


    def dbToUsers():
        Controller.users.clear()
        res = Controller.usersDb.all()
        for item in res:
            firstname = item.get("firstname")
            lastname = item.get("lastname")
            email = item.get("email")
            address = item.get("address")
            phone = item.get("phone")
            user = User(firstname, lastname, email, address, phone)
            Controller.users.append(user)


    def getUsers():
        return Controller.users
        
    def getUser(firstname, lastname):
        Controller.usersDb.search((Controller.userQuery.firstname == firstname) & (Controller.userQuery.lastname == lastname))
        Controller.dbToUsers()

    def addUser(firstname, lastname, email, address, phone):
        Controller.usersDb.insert({'firstname':firstname, 'lastname':lastname, 'email':email, 'address':address, 'phone':phone})
        Controller.dbToUsers()

    def removeUser(firstname, lastname):
        Controller.usersDb.remove((Controller.userQuery.firstname == firstname) & (Controller.userQuery.lastname == lastname))
        Controller.dbToUsers()

    def isUser(firstname, lastname):
        if len(Controller.usersDb.search((Controller.userQuery.firstname == firstname) & (Controller.userQuery.lastname == lastname))) > 0:
            return True
        else:
            return False

    def sortByChar(c):
        d = c.upper()
        pat=Alphabet.get(d)
        usersRes=[]
        for i in range(len(pat)):
            usersTemp = []
            for j in range(len(Controller.users)):
                if(Controller.users[j].getLastName()[0].lower() == pat[i]):
                    usersTemp.append(Controller.users[j])
            sorted(usersTemp, key=lambda x: x.getLastName()) 
            for x in range(len(usersTemp)):
                usersRes.append(usersTemp[x])

        for w in range(len(usersRes)):
            print("lastname:",usersRes[w].getLastName())

        Controller.users = usersRes       
        return usersRes
    
    def getCharList():
        return Controller.charList

    def getCharUsersList():
        Controller.dbToUsers()
        charList=[]
        
        for i in range(len(Controller.users)):
            have = False
            for j in range(len(charList)):
                if(Controller.users[i].getLastName()[0]==charList[j]):
                    have = True
            if have==False:
                charList.append(Controller.users[i].getLastName()[0].upper())
                
        charList.sort()
        Controller.charList = charList
        return charList

