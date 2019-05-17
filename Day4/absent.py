with open("absentee.txt","wt") as ab:
    counter=25
    while True:
        if counter==0:
            break
        else:
            name=input("enter the name of students")
            ab.write(name+"\n")
            counter=counter-1
            if not name:
                break
with open("absentee.txt","rt") as ab:
    ab.seek(0,0)
    for item in ab.readlines():
        print(item)