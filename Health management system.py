def getdate():
    import datetime
    return datetime.datetime.now()
def log():
    print("select a person which you log: ")
    print("1 Chaitany")
    print("2 Homdas")
    print("3 Pranay")
    h=int(input())
    if(h==1):
        print("which you wants to log for Chaitany")
        print("1 for food-receipe,2for exercise")
        logn=int(input())
        if(logn==1):
            menu=str(input("Enter food name:"))
            with open("chaitany-food-receipe.txt","a") as fchaitany:
                fchaitany.write(str([str(getdate())]) + ":" + menu + "\n")
                print("food entered successfully")
                fchaitany.close()
        if(logn==2):
            exercise=input("Enter exercise name: ")
            with open("chaitany-exercise.txt","a") as fchaitany:
                fchaitany.write(str([str(getdate())]) + ":" + exercise + "\n")
                print("exercised entered successfully")
                fchaitany.close()
        
        #else:
            #print("enter right choice")
    if(h==2):
        print("which you wants to log for Homdas")
        print("1 for food-receipe,2for exercise")
        logn=int(input())
        if(logn==1):
            menu=input("Enter food name:")
            with open("Homdas-food-receipe.txt","a") as fhomdas:
                fhomdas.write(str([str(getdate())]) + ":" + menu + "\n")
                print("food entered successfully")
                fhomdas.close()
        if(logn==2):
            exercise=input("Enter exercise name:")
            with open("Homdas-exercise.txt","a") as fhomdas:
                fhomdas.write(str([str(getdate())]) + ":" + exercise + "\n")
                print("exercise entered successfully")
                fhomdas.close()
        
        #else:
            #print("face some type of problem")
    if(h==3):
        print("which you wants to log for pranay")
        print("1 for food-receipe,2for exercise")
        logn=int(input())
        if(logn==1):
            menu=input("Enter food name:")
            with open("pranay-food-receipe.txt","a") as fpranay:
                fpranay.write(str([str(getdate())])+":"+menu+"\n")
                print("food entered successfully")
                fpranay.close()
        if(logn==2):
            exercise=input("Enter exercise name:")
            with open("pranay-exercise.txt","a") as fpranay:
                fpranay.write(str([str(getdate())])+":"+exercise+"\n")
                print("exercise entered successfully")
                fpranay.close()
        
        #else:
            #print("face some type of problem")
def retrive():
    print("select a person which you retrive: ")
    print("1 Chaitany")
    print("2 Homdas")
    print("3 Pranay")
    s=int(input())
    if(s==1):
        print("which you wants to retrive for Chaitany")
        print("1 for food-receipe,2for exercise")
        val=int(input())
        if(val==1):
            #ssb=input(" ")
            with open("chaitany-food-receipe.txt","r") as fchaitany:
                print(fchaitany.read())
        if(val==2):
            #ssb=input(" ")
            with open("chaitany-exercise.txt","r") as fchaitany:
                print(fchaitany.read())
        
        else:
            print("face some type of problem")
    if(s==2):
        print("which you wants to retrive for Homdas")
        print("1 for food-receipe,2for exercise")
        logn=int(input())
        if(logn==1):
            #ssb=input(" ")
            with open("Homdas-food-receipe.txt","r") as fhomdas:
                print(fhomdas.read())
        elif(logn==2):
            #ssb=input(" ")
            with open("Homdas-exercise.txt","r") as fhomdas:
                print(fhomdas.read())
        
        else:
            print("face some type of problem")
    if(s==3):
        print("which you wants to retrive for pranay")
        print("1 for food-receipe,2for exercise")
        gana=int(input())
        if(gana==1):
            #ssb=input(" ")
            with open("pranay-food-receipe.txt","r") as fpranay:
                print(fpranay.read())
        elif(gana==2):
            #ssb=input(" ")
            with open("pranay-exercise.txt","r") as fpranay:
                print(fpranay.read())
        
        else:
            print("face some type of problem")
print("1 for logg,2 for retrieve")
user=int(input())

if(user==1):
    log()
elif(user==2):
    retrive()
else:
    print("error")
# code created by pranay gaynar!!!!!
    
        
    
    
    

    



