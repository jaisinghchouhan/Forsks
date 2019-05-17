list1=[[34587,'Learning Python', 'Mark Lutz' ,4,40.95],
    [98762,'Programming Python', 'Mark Lutz',5,56.80],
    [77226,'Head First Python', 'Paul Barry',3,32.95],
    [88112 ,'Einführung in Python3', 'Bernd Klein',3,24.99]]
list2=list(map(lambda x:x[0],list1))
print(list2)
list3=[product[3]*product[4] if product[3]*product[4] >100 else product[3]*product[4]+10 for product in list1]
print(list(zip(list2,list3)))



