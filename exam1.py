import csv
csvarray = []
with open("agenti.csv", newline='', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
    for row in spamreader:
        csvarray.append(row)
    for rinda in csvarray:
        print(rinda[0])
print(csvarray)
print(len(csvarray[0]))
print(csvarray[1])
