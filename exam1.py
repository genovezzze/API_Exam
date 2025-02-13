import csv
csvarray = []
with open ('agenti.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    #print(spamreader)
    for row in spamreader:
        csvarray.append(row)
    # csvarray
    #print(csvarray)
   # for rinda in csvarray:
   #     print(rinda[0])
#print(csvarray)
#print(len(csvarray[0]))
#print(csvarray[1][1])
def filtretIestades(masivs):
    iestades=[]
    for rinda in masivs:
        if rinda[0]=="Valsts iestādes" or rinda[0]=="Izglitības iestāde":
            #print(rinda)
            print(f"{rinda[0]} - {rinda[1]}, atrodas {rinda[2]}")
            iestades.append(rinda)
    return iestades
#filtretIestades(csvarray)
   
def tikaiRiga(masivs):
    for rinda in masivs:
        adrese=rinda[2]
        if "Riga," in rinda[2]:
            print(rinda[2])
tikaiRiga(csvarray)
def kartotPecNosaukuma(masivs):
    return sorted(masivs, key=lambda rinda:rinda[1])
sakartots=kartotPecNosaukuma(csvarray)
for rinda in sakartots:
    print(rinda)
