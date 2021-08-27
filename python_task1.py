import random
no_of_overs =int(input("ENTER THE NUMBER OF OVERS U WANT TO PLAY : "))
comp_score=random.randint(0,36)
print('COMPUTER HAS SCORE = ' ,comp_score)


print("YOUR TARGET IS =",comp_score+1)

your_runs=0


for i in range(1,no_of_overs+1):
    for j in range(1,7):

         your_no=int(input("ENTER NUMBERS TO BAT ="))
         if your_no > 6:
                print("YOU CAN NOT SCORE MORE THAN 6 RUNS")
         else:
             comp_no=random.randint(0,6)
             print( "COMUTER'S NUMBER IS = " ,comp_no)
             print("TOTAL RUNS =" ,your_runs+your_no )
          
            

             if comp_no==your_no:
                 print("out")
                 break
             else:
                 your_runs=your_runs+your_no
             

             if your_runs>comp_score:
                 break

if your_runs>comp_score:
                print("YOU WON THE MATCH")
        elif:
            print("MATCH DRAW")
else:
                print("COMPUTER WINS BETTER LUCK NEXT TIME!!!")
        



       







