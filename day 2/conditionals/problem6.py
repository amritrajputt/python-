#leap year
# year = int(input("enter year : "))

#1st method
# if(year % 4 ==0 and year % 100 != 0):
#     print("leap year")
# elif(year % 400 == 0):
#     print("leap year")    
# else :
#     print("not a leap year")    

# cleaner method

year = int(input("enter year : "))
if(year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")    