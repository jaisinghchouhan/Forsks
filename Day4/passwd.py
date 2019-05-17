uname={}
with open("passwd","rt") as f1:
    lines=f1.readlines()
    for line in lines:
        row=line.split(":")
        if row[0]=="#":
            pass
        
        uname[row[0]]=row[2]
    #print(uname)
    nlist=list(sorted(uname))
    for word in nlist:
        print(word,uname[word])            
            