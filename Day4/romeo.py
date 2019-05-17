dict1={}
with open("romeo.txt","rt") as f1:
    for line in f1.readlines():
        list1=line.split()
        for word in list1:
            if  word in dict1:
                dict1[word]=dict1[word]+1
            else:
                dict1[word]=1
    print(dict1)  
    