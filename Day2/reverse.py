def reverse(s): 
  nstr = "" 
  for i in s: 
    nstr = i + nstr
  return nstr
  
str1=input("enter an string")
  
print ("The original string  is : ",str1) 
  
print ("The reversed string is : ",reverse(str1)) 