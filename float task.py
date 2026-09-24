#Convert a float to an integer with an inbuilt function in Python
temp = 56.8926
temp =round(temp)
print(temp)
#Convert the float below to give the results as follows to 56.89 
temp1 = 56.8926 
temp1 =round(temp1,2)
print(temp1)
#Convert the float below to give the results as follows to 56.893 
temp2 = 56.8926
temp2 =round(temp2,3)
print(temp2) 
#Convert the float below to give the results as follows  to 8.926 
temp3=56.8926
temp3s= str(temp3)
ex = temp3s[3] + "." + temp3s[4:]
print(float(ex))
#NB: Use string  slice & concatenation, but have result as float 


my_float= 5678.4567
my_float= str(my_float)
my_float=my_float[:4]
my_float = my_float[0]+ "." + my_float[1:]
print(my_float)

my_float = 5678.4567
my_float= str(my_float)
my_float=my_float[5:]
my_float = my_float[:3]+ "." + my_float[3]
print(my_float)

