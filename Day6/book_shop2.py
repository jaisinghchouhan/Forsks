list1= [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
list2=list(map(lambda x:x[0],list1))
print(list2)
list3=[product[1][1]*product[1][2]+product[2][1]*product[2][2]+product[3][1]*product[3][2] 
        if len(product)==4 else product[1][1]*product[1][2]+product[2][1]*product[2][2]  for product in list1]
print(list(zip(list2,list3)))