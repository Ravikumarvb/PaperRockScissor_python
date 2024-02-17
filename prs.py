import random
print("***************************************")
print("*     * Paper * Rock *  *Scissor*     *")
print("***************************************")
print("Lets start the game!!....")
point=0
ai=0
hs=0
cs=0
ma=0
while(True):
    if(ma>56):
        print("########################")
        print("Total Match:",ma)
        print("Human score",hs)
        print("AI score",cs)
    if(hs>cs):
        print("Congrats You Won")
    elif(cs>hs):
        print("AI Won....better luck next time")
    else:
        print("Match draw")
        print("########################")
        break
   c=input("Choose paper->p  rock->r  scissor->s Stop->stop: ")
   if(c=="p"):
       print("paper")
       point=10+random.randint(1,3)
       match point:
         case 11:
           ma=(ma+1)
           print("Human: paper", "AI:rock")
           print("Match: ",ma,"Human score:",hs,"AI score:",cs)
           print("Human: win","AI: lost")
           print("--------------------")
         case 12:
           ma=(ma+1)
           cs=(cs+1)
           print("Human: paper", "AI: scissor")
           print("Match: ",ma,"Human score:",hs,"AI score:",cs)
           print("Human: lost","AI: won")
           print("--------------------")
         case 13:
           ma=(ma+1)
           hs=(hs+1)
           cs=(cs+1)
           print("Human: paper", "AI: paper")
           print("Match: ",ma,"Human score:",hs,"AI score:",cs)
           print("match draw")
           print("---------------------")
   elif(c=="r"):
       print("rock")
       point=20+random.randint(1,3)
       match point:
         case 21:
           print("Human: rock", "AI: scissor")
           print("Match: ",ma,"Human score:",hs,"AI score:",cs)
           print("Human: win","AI: lost")
           print("--------------------")
         case 22:
           print("Human: rock", "AI: paper")
           print("Match: ",ma,"Human score:",hs,"AI score:",cs)
           print("Human: lost","AI: won")
           print("--------------------")
         case 23:
           print("Human: rock", "AI: rock")
           print("Match: ",ma,"Human score:",hs,"AI score:",cs)
           print("match draw")
           print("---------------------")
   elif(c=="s"):
       print("scissor")
       point=30+random.randint(1,3)
       match point:
         case 31:
           print("Human: scissor", "AI: paper")
           print("Match: ",ma,"Human score:",hs,"AI score:",cs)
           print("Human: win","AI: lost")
           print("--------------------")
         case 32:
           print("Human: scissor", "AI: rock")
           print("Match: ",ma,"Human score:",hs,"AI score:",cs)
           print("Human: lost","AI: won")
           print("--------------------")
         case 33:
           print("Human: scissor", "AI: scissor")
           print("Match: ",ma,"Human score:",hs,"AI score:",cs)
           print("match draw")
           print("---------------------")
   elif(c=="stop"):
       break
print("Program End")