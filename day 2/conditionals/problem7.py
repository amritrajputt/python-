animal = input("which animal: ")
age = int(input("enter age: "))

if(animal == 'dog'):
    if(age < 2):
        print("puppy food")
    else:     
        print("adult food")
elif(animal == 'cat'):
        if(age > 5):
             print("senior cat food")
        else:     
             print("junior cat food")     