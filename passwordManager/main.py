import json

USER = "nimish"
PASSWORD = "nimish"

def Master_login():
    print("=======MASTER LOGIN========")
    user = input("please enter the username: ")
    passw = input("please enter the password: ")
    if user == USER and passw == PASSWORD:
        runCode()
    else:
        print("wrong credentials")

def add():
    vault = {}
    website = input("please enter the name of the website : ")
    username = input("please enter the username : ")
    password = input("please enter the password : ")
    # vault[website]=[username,password]
    with open('vault.json','r+') as file:
            mydict=json.load(file)
            if website in mydict :
                print("credentials already preset do you wish to override ?")
                cho =input("Please type 'over' to overwrite")
                if cho.lower().strip()=='over':
                    print("over-writing")
                    mydict[website]=[username,password]
                    file.seek(0)
                    file.truncate()
                    json.dump(mydict, file, indent=4)
                else:
                    print("overwriting failed as over not typed correctly ")
            else:
                mydict[website]=[username,password]
                file.seek(0)
                file.truncate()
                json.dump(mydict,file,indent=4)


    print("details successfully added ")


def view():
    website = input("please enter the website whose password you want to view")
    with open('vault.json','r') as file:
        mydict=json.load(file)
        if len(mydict)!=0:
            if website in mydict.keys():
                print("{====CREDENTIALS FOUND====}")
                print(f"USERNAME: {mydict[website][0]}")
                print(f"PASSWORD: {mydict[website][1]}")
            else:
                print("sorry not such credentials found")
        else:
            print("YOUR VAULT IS EMPTY PLEASE ADD SOME DATA FIRST")
    file.close()


def delete():
    website = input("please enter the website whose credentials you want to DELETE")

    with open('vault.json', 'r+') as file:
        mydict = json.load(file)
        if len(mydict) != 0:
            if website in mydict.keys():
                print("{====CREDENTIALS FOUND==== }")
                delt = input('PLEASE TYPE "delete" to delete the entry ')
                if delt.lower().strip() == "delete":
                    mydict.pop(website)
                    print("DELETED SUCCESSFULLY")
                    file.seek(0)
                    file.truncate()
                    json.dump(mydict, file, indent=4)
                else :
                    print("Not deleted as delete was not correctly typed")

                # json.dump(mydict,file,indent = 4)
            else:
                print("sorry not such credentials found")
    file.close()


    #
def runCode():
    while True:
        print("\n=====MENU=====\n1. ADD PASSWORD\n2.VIEW PASSWORDS\n3.DELETE \n4. EXIT\n")
        ch = (input("please enter your choice {1,2,3,4} : "))

        if ch == '1':
            add()
        elif ch == '2':
            view()
        elif ch == '3':
            delete()
        elif ch== '4' :
            print("exiting the password vault ")
            break
        else:
            print("wrong choice")

Master_login()