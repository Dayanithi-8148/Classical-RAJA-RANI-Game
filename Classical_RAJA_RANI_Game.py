from random import shuffle

print("\n\n--------------------  Welcome to Raja,Rani,Thirudan,Police  --------------------\n\n")

#character=input("Enter Character name : ").lower()
characters=["Raja","Rani","Mandhiri","Police","Thirudan"]  #character.split(" ") 
players=input("Enter Players Name : ").lower()
player=players.split(" ")
shuffle(player)
print("\n\n--------------------------------------------------------------------------------\n\n")
line="\n--------------------------------------------------------------------------------\n"
space="                              "

score=[]

def find(a):
    count=0
    for i in player:
        if(i==a):
            break
        else:
            count+=1
    return count

size=len(characters)-1

i=0
j=1
for i in range(size):
    while(True):            
        print(space,player[0],"is ",characters[i])
        print("Find ",characters[j]," : ",end=" ")
        a1=input().lower()
        if (player[1]==a1):
            print(space,characters[j]," found")
            score.append(player[0])
            del(player[0])
            print(line)
            i+=1
            j+=1
            break
        else:
            temp=player[0]
            f=find(a1)
            player[0]=a1
            player[f]=temp
score.append(player[0])

print("------------------------------ Score Board -------------------------------------\n")
print(space,score[0],"= 10000")
print(space,score[1],"= 5000")
print(space,score[2],"= 3000")
print(space,score[3],"= 1000")
print(space,score[4],"= 0")
print("\n--------------------------------------------------------------------------------")
