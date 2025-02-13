import csv
csvarray = []
with open ('agenti.csv', newline="", encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    #print(spamreader)
    for row in spamreader:
        csvarray.append(row)
    #print(csvarray)
   # for rinda in csvarray:
   #     print(rinda[0])
#print(csvarray)
#print(len(csvarray[0]))
#print(csvarray[1][1])

def filtretIestades(array):
    for rinda in masivs:
        if rinda[0]=="Valsts iestādes" or rinda[0]=="Izglitības iestāde":
            print(rinda)
            print(f"{rinda[0]}, {rinda[2]}")
#filtretIestades(csvarray)

def tikaiRiga(masivs):
    for rinda in masivs:
        if "Riga," in rinda[2]:
            print(rinda[2])

tikaiRiga(csvarray)
