cy=2023
def age(n):
   global cy
   while (n<=100):
        cy+=1
        n+=1
   return(cy)
name=input("enter a name:")
ag=int(input('Enter your age:'))
print ("Name:",name)
print("current year:",cy)
print("you will become 100 years old at the year:",age(ag))
