#1. AGE group categorization
age = int(input("ENTER AGE: "))
if(age < 13):
    print("child")
elif(age>=13 and age<=19):
    print("teenager")
elif(age > 19 and age <= 59):
    print("adult")        
else:
    print("senior")    
