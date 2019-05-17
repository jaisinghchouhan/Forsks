filename=input("enter a file name")
with open(filename,"rt") as f1:
    list=f1.readlines()
    print(list[-1])