import json

def checkIp(ip_list):
    for i in ip_list:
        if not i.isdigit():
            print(".".join(ip_list), "is invalid IP")
            break
        elif int(i)>255 or int(i)<0:
            print(".".join(ip_list), "is invalid IP")
            break
        
file_new = open("dataFile.json")

data = json.load(file_new)

for i in data["ipaddr"]:
    ip_list = i.split(".")
    if len(ip_list)!=4:
        print(".".join(ip_list), "is invalid IP")
    else:
        checkIp(ip_list)