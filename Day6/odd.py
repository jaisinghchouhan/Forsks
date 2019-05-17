from functools import reduce 
list1=[1,2,3,4,5]
list2= list(filter(lambda x: (x % 2 != 0), list1))
print(list1) 
product=reduce(lambda h,w:h*w,list2)
print(product)