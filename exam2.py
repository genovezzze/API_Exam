import requests

#1. Izveido pieprasījumu uz doto API. 
atbilde= requests.get("https://restcountries.com/v3.1/all")

#2. Pārbaudi, vai no servera ir saņemta korekta atbilde. 
#print(atbilde.status_code)
#TODO
if (atbilde.status_code!=200):
    print("Kaut kas nav pareizi!!!")

#3. Iegūsti un izvadi visu valstu vispārpieņemtos nosaukumus (“name” → “common”). 

atbildeDict=json.loads(atbilde.text)
print(len(atbildeDict))
print(atbildeDict)
