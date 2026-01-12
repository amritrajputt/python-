# movie ticket price based on age

age = int(input("ENTER AGE: "))
day = input("ENTER DAY: ")
price = 12 if (age >=18) else 8

if(day == 'wednesday'):
        price-=2
print(price)
