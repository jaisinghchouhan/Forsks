def ADD(list1):
    
    b  = sum(list1)
    return b

def Mul(list2):
    b=0
    
    for i in list2:
        b += i * (i+1)
        print(b)
        
    return b

list1=[ 5,2,6,2,3]
a=ADD(list1)
print("sum is " ,a)

c=Mul(list1)
print("mul is " ,c)

list1.sort()
print("largest is ",list1[-1])
print("smallest is ",list1[0])