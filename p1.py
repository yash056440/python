num = int(input("Enter number:"))

for row in range(1,num+1):
   
    for col in range(num-row):
        print(" ", end="")
    for col in range(0,row):
        print("*", end="")
    
    print(" ")




