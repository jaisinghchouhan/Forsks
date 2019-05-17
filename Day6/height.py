from functools import reduce 
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
height_total = 0
height_count = 0
list1=list(filter(lambda x:'height' in x,people))
print(list1)
list2=list(map(lambda x:x['height'],list1))
print(list2)
height_total=reduce(lambda h,w:h+w,list2)
height_count=len(list2)
print("average = ",height_total / height_count)