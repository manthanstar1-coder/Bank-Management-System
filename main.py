from pathlib import Path
import json
import random
import string
import datetime
import bcrypt
import mysql.connector
from tabulate import tabulate

# New User Data
class userInfo:
    def Name(self):
        name = input("Full Name: ").upper()
        return name
    
    def dob(self):
        print("Date of Birth")
        self.day = int(input("Day: "))
        self.month = int(input("Month (in numeric): "))
        self.year = int(input("Year: "))
        return f"{self.day}/{self.month}/{self.year}"

    def Age(self):
        diff = datetime.datetime.now() - datetime.datetime(self.year, self.month, self.day)
        age =  diff.days // 365
        return age
    
    def Gender(self):
        while 1:
            gender = input("Gender (M/F): ")
            if gender.lower() == 'm':
                return "MALE"
            elif gender.lower() == 'f':
                return "FEMALE"
            else:
                print("Invalid input.")
                
    
    
    def Email(self):
        email = input("Email: ")
        return email
    
    
    
    def Pin(self):
        pin = input("Create 4-digit pin: ")
        if not (pin.isdigit() and len(pin) == 4):
            print("PIN must be exactly 4 digits")
            return self.Pin()
        
        print("-------------------------------------------------")
        
        hPin = bcrypt.hashpw(pin.encode('utf-8'), bcrypt.gensalt()) # Hash PIN
        return hPin.decode('utf-8')
      
    

# Bank Class
class Bank:
    
    database = 'data.json'
    data = []    
    
    def __init__(self):
        self.loadDatabase()
        
        
    # Read Database and create dummy data
    def loadDatabase(self):
        try:
            if Path(Bank.database).exists():
                with open(Bank.database) as fs:
                    Bank.data = json.loads(fs.read())
                    
            else:
                print("No such database exist")

        except Exception as err:
            print(f"An exception ocurred as {err}")
        
    
    ## Update Database
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
            
    @classmethod
    def __accountGenerate(cls):
        accgen = random.choices(string.digits, k = 15)
        random.shuffle(accgen)
        return "".join(accgen)
    
    
    # Open New Account
    def creatAcc(self):
        
        # Call userInfo in object newUser
        newUser = userInfo()
        
        info = {
            'Name' : newUser.Name(),
            'DOB' : newUser.dob(),
            'Age' : newUser.Age(),
            'Gender' : newUser.Gender(),
            'Email' : newUser.Email(),
            'Account No.' : Bank.__accountGenerate(),
            'PIN' : newUser.Pin(),
            'Balance': 0
        }
        
        
        #Check age > = 18 and pin has 4 digits
        if info['Age'] < 18:
            print("You can't open account")
            print("-------------------------------------------------")
            
        else:
            print(("Account has been created successfully").upper())
            print("-------------------------------------------------")
            
            for i in info:
                print(f"{i} : {info[i]}")
                        
            print("-------------------------------------------------")
            print(("*Note down your account number").upper())
                        
            Bank.data.append(info)
            Bank.__update()
            
    # Deposit money
    def moneyDeposit(self):
        try:
            accNum = input("Enter Account Number: ")
            pin = input("Enter PIN: ")
            
            userData = [i for i in Bank.data if i['Account No.'] == accNum and bcrypt.checkpw(pin.encode('utf-8'), i['PIN'].encode('utf8'))]
            if userData == False:
                print("User data not found")
                print("-------------------------------------------------")

            else:
                amt = int(input("Enter Amount: "))
                print("-------------------------------------------------")
                
                if amt > 0:
                    userData[0]['Balance'] += amt
                    Bank.__update()
                    print(("Deposited successfully").upper())
                    print(f"Total Balance: {userData[0]['Balance']}")
                    print("-------------------------------------------------")
                    
        except Exception as err:
            print(f"An exception Ocurred as {err}")
            
    # Whidhrow money       
    def moneyWithdraw(self):
        try:
            accNum = input("Enter Account Number: ")
            pin = input("Enter PIN: ")
            
            userData = [i for i in Bank.data if i['Account No.'] == accNum and bcrypt.checkpw(pin.encode('utf-8'), i['PIN'].encode('utf8'))]
            if userData == False:
                print("User data not found")
                print("-------------------------------------------------")

            else:
                amt = int(input("Enter Amount: "))
                print("-------------------------------------------------")
                
                if userData[0]['Balance'] < amt:
                    print(("insufficient balance").upper())

                else:
                    userData[0]['Balance'] -= amt
                    Bank.__update()
                    print(("Whidhrew successfully").upper())
                    print(f"Total Balance: {userData[0]['Balance']}")
                    print("-------------------------------------------------")
                    
        except Exception as err:
            print(f"An exception Ocurred as {err}")
            print("-------------------------------------------------")
            
    
    # Show user Details
    def showDetails(self):
        accNum = input("Enter Account Number: ")
        pin = input("Enter PIN: ")
        print("-------------------------------------------------")
        
        userData = [i for i in Bank.data if i['Account No.'] == accNum and bcrypt.checkpw(pin.encode('utf-8'), i['PIN'].encode('utf8'))]
        
        if userData == False:
            print("Account Doesn't Exist")
            print("-------------------------------------------------")
            
        else:
            print("=====================Details=====================")
            for i in userData[0]:
                print(f"{i} : {userData[0][i]}")
                
            print("-------------------------------------------------")
        
    
    # Update User Update
    def userUpdate(self):
        accNum = input("Enter Account Number: ")
        pin = input("Enter PIN: ")
                
        userData = [i for i in Bank.data if i['Account No.'] == accNum and bcrypt.checkpw(pin.encode('utf-8'), i['PIN'].encode('utf8'))]
        
        if userData == False:
            print("Account Doesn't Exist")
            print("-------------------------------------------------")
            
        else:
            print(("You can't change the age, account number, balance").upper())
            print("-------------------------------------------------")
            
            updateUser = userInfo()
            updateInfo = {
                "Name" : updateUser.Name(),
                "Email" : updateUser.Email(),
                "PIN" : updateUser.Pin()
            }
            
            if updateInfo["Name"] == "":
                updateInfo["Name"] = userData[0]["Name"]
            if updateInfo["Email"] == "":
                updateInfo["Email"] = userData[0]["Email"]
            if updateInfo["PIN"] == "":
                updateInfo["PIN"] = userData[0]["PIN"]
                
            updateInfo["DOB"] = userData[0]["DOB"]
            updateInfo["Age"] = userData[0]["Age"]
            updateInfo["Gender"] = userData[0]["Gender"]
            updateInfo["Account No."] = userData[0]["Account No."]
            updateInfo["Balance"] = userData[0]["Balance"]
            
            # if type(updateInfo["PIN"]) == str:
            #     updateInfo["PIN"] = int(updateInfo["PIN"])
            
            for i in updateInfo:
                if updateInfo[i] == userData[0][i]:
                    continue
                else:
                    userData[0][i] = updateInfo[i]
                    
            Bank.__update()
            print(("Update successfully").upper())
            print("------------------------------------------------")
            
            print(("================Updated Details=================").upper())
            for i in userData[0]:
                print(f"{i} : {userData[0][i]}")
                
            print("------------------------------------------------")
            
    # Close user Account
    def closeAccount(self):
        accNum = input("Enter Account Number: ")
        pin = input("Enter PIN: ")
                        
        userData = [i for i in Bank.data if i['Account No.'] == accNum and bcrypt.checkpw(pin.encode('utf-8'), i['PIN'].encode('utf8'))]
        
        if userData == False:
            print("Account Doesn't Exist")
            print("-------------------------------------------------")
                        
        else:
            for i in userData[0]:
                print(f"{i} : {userData[0][i]}")
                
            print("-------------------------------------------------")
            conf = input("Do you want to close account (y): ")
            if conf.lower() == 'y':
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                
                print(("Account closed successfully").upper())
                print("-------------------------------------------------")
                
                Bank.__update()
            else:
                return

               
# Call Bank class in user object
user = Bank()

while 1:
    print("1. Open Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Passbook")
    print("5. Update Details")
    print("6. Close Account")
    print("0. Exit")
    print("------------------------------------------------")

    opt = int(input("Enter your response: "))
    print("------------------------------------------------")

    if opt == 1:
        user.creatAcc()
        
    elif opt == 2:
        user.moneyDeposit()
        
    elif opt == 3:
        user.moneyWithdraw()
        
    elif opt == 4:
        user.showDetails()
        
    elif opt == 5:
        user.userUpdate()
        
    elif opt == 6:
        user.closeAccount()
        
    elif opt == 0:
        break
    
    else:
        print(("Invalid Input").upper())