'''f=open("world.txt","r")
data=f.read()
print(data)
f.close



s="hello world"
f=open("word.txt","w")
f.write(s)
f.close()

f=open("poem.txt","r")
data=f.read()

if ("twinkle" in data):
    print("twinkle is present")
else: 
      print("twinkle is not present")

f.close()


import random

def game():
    print("welcome to the number game")
    score =random.randint(1,100)
    with open("hiscore.txt") as f:
        hiscore=f.read()
    if  hiscore!="":hiscore=int(hiscore)
    else: hiscore=0

    print("your score is ",score)
    if score >hiscore:
        print("congratulations! you have the highest score")
        with open("hiscore.txt","w") as f:
            f.write(str(score))
            return



game()
'''


word="donkey"


        
    
    
