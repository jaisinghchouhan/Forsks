import csv
with open("zoo.csv","rt") as f1:
    #print(f1.readlines())

dit1={}
with open("zoo.csv","rt") as f2:
    csv_reader = csv.reader(f2)
    for row in csv_reader:
        if row[0] in dic1:
            dic1[row[0]]=dic1[row[0]]+1
        else:
            dic1[row[0]]=1
    print(dic1)
        
add=0
with open("zoo.csv","rt") as f2:
    csv_reader = csv.reader(f2)
    next(csv_reader)
    for row in csv_reader:
        add=add+int(row[2])
    print(add)