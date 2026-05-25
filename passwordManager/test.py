import json

password= {
    "website": ["username","password"]

}

with open("vault.json",'r') as file :
    data = json.load(file)
    print(data)


    # json.dump(password,file)