list1 = input("Enter the item :").split(",")
list2 = input("enter the price").split(",")
list3=["13","14","17","18","19"]
d1 = dict(zip(list1,list2))
list4=list(d1.values())
a=len(list4)
sum=0
for i in range(0,a):
    if list4[i] not in list3:
        sum=sum+int(list4[i])
    else:
        continue
print(sum)
