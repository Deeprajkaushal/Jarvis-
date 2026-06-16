'''def kallu(he):
    print("kalllu suare he", he)

    return("hehe")

kallu("bahutbada")
kallu(64)




def greatest():
    if u > b:
        return u
    else:
        return b
    
u=int(input("enter a number:"))
b=int(input("enter a number:"))
print("the greatest number is:", greatest())



def dtof(c):
    f=(c*9/5)+32
    return f

c=int(input("enter the temperature in celsius:"))
print("the temperature in fahrenheit is:", dtof(c))
'''

def summ(a):
    if a==1:
        return 1
    return summ(a-1)+a

print("the sum is",summ(3))

def pattern(n):
    if n==0:
        return 
    print("*" * n)
    pattern(n-1)

pattern(9)