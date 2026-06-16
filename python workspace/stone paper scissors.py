
'''
rock=1
paper=0
scissors=-1
'''
import random

value = random.choice([-1, 0, 1])

computer=value
you=input("enter your choice: r for rock, p for paper, s for scissors: ")

youdict={"r":1,"p":0,"s":-1}
younum=youdict[you]

youdictreverse={1:"rock",0:"paper",-1:"scissors"}
print("computer choice is:",youdictreverse[computer])
print("your choice is: ",youdictreverse[younum])

if(you!="r" and you!="p" and you!="s"):
    print("invalid input")
    
else:

    if(computer==-1 and younum==1):
        print("you win")
    
    elif(computer==-1 and younum==0):
        print("you lose")


    elif(computer==1 and younum==-1):
        print("you lose")
    
    elif(computer==1 and younum==0):
        print("you win")


    elif(computer==0 and younum==1):
        print("you lose")
    
    elif(computer==0 and younum==-1):
        print("you win")


    else:
        print("its a tie")

