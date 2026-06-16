'''s=input("enter a numberr:")
t=input("enter a numberr:")
u=input("enter a numberr:")
v=input("enter a numberr:")

if(s>=t and s>=u and s>=v):
    print("the greatest number is:",s)

elif(t>=s and t>=u and t>=v):
    print("the greatest number is:",t)

elif(u>=t and u>=s and u>=v):
    print("the greatest number is:",u)

else:
    print("the greatest number is:",v)



m1=int(input("enter marks in maths:"))
m2=int(input("enter marks in english:"))
m3=int(input("enter marks in chemistry:"))

total_percentage=((m1+m2+m3)/300)*100

print("your overall pecentage is:",total_percentage)

if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("you have passed")
else:
    print("you have failed,try again !")

if m1<33:
    print("you failed in maths")

if m2<33:
    print("you failed in engish")

if m3<33:
    print("you failed in chemistry")



p1="buy this"
p2="click this"
p3="subscibe this"
p4="make a lot of money"

message=input("paste message here:")

if(p1 or p2 or p3 or p4 in message ):
    print("this message is a spam")
else:
    print("this is a normal message")



p=input("enter your name:  ")

if len(p)>10:
    print("your name is too long")
else:
    print("your name is within the limit")


# i=1
# while (50>=i):
#     print(i)
#     i=i+1
# from math import sqrtcx
# print(sqrt(81))


# l=["deep","aksh","raj","atul"]

# i=0
# while i<len(l):
#     print(l[i])
#     i=i+1



# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(i*num)





l=["deep","aksh","raj","atul"]
for i in l:
    if i.startswith("d"):
        print(i)


i=1
num=int(input("enter the number:"))
while (i<11):
    print(i*num)
    i=i+1

for i in range(2,num):
    if (num%i==0):
        print("the number is not prime")   
        break 
    else:
        print("the number is prime")  


n=int(input("enter a number:"))
i=0
sum=0
while(i<=n):
    sum=sum+i
    i=i+1

print("the sum is:",sum)


n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
   fact=fact*i
print("the factorial is:",fact)


rows = 3

for i in range(3):
    print(" " * (2 - i) + "*" * (2*i + 1))
'''

for i in range(5):
    print(" "*(4-i)+"*"*(2*i+1))

for i in range(3):
    print("*"*(i+1))

