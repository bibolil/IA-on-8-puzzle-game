from state import State 
from puzzle import Board
import time

def comparaison(puzzle,puzzles):
        test=False
        for x in puzzles:
            if (puzzle==x):
                test=True
        return test

def heureustic(puzzle,goal):
    n=0
    liste1=puzzle.transform()
    liste2=goal.transform()
    for i in range(len(liste1)):
        if (liste1[i]!=liste2[i]):
            n+=1
    return n


def generate_child_for_A(puzzle,puzzles,puzzles_cost,depth):
    t1,t2,t3,t4=False,False,False,False
    
    if (puzzle.up() and not(comparaison(puzzle.up(),puzzles))):
        y=puzzle.up()
        puzzles.append(y)
        puzzles_cost.append(heureustic(y,goal)+depth)
        t1=True
        

    if (puzzle.down() and not(comparaison(puzzle.down(),puzzles))):
        y=puzzle.down()
        puzzles.append(y)
        puzzles_cost.append(heureustic(y,goal)+depth)
        t2=True
        
    if (puzzle.right() and not(comparaison(puzzle.right(),puzzles))):
        y=puzzle.right()
        puzzles.append(y)
        puzzles_cost.append(heureustic(y,goal)+depth)
        t3=True
        

    if (puzzle.left() and not(comparaison(puzzle.left(),puzzles))):
        y=puzzle.left()
        puzzles.append(y)
        puzzles_cost.append(heureustic(y,goal)+depth)
        t4=True
        

    if(t1 or t2 or t3 or t4):
        depth+=1     
    return depth



def A_star(puzzle,goal,maxdepth,puzzles,puzzles_cost): 
    start_time = time.time()
    depth=0
    puzzles.append(puzzle)
    puzzles_cost.append(heureustic(puzzle,goal)+depth)
    newlist=State()
    newlist=puzzle
    tracking=[]
    if(newlist==goal):
        tracking.append(newlist.transform())
        print(newlist)
    else:
        while(goal!=newlist and len(puzzles)!=0):
            
          i=puzzles_cost.index(min(puzzles_cost)) 
          newlist=puzzles[i]
          puzzles.pop(i)
          puzzles_cost.pop(i)

          tracking.append(newlist.transform())
          print(newlist)

          if(newlist==goal):
                print("Number of puzzles treated",len(tracking))
                print("goal reached")
                print("--- %s seconds ---" % (time.time() - start_time))
                break

          if(depth!=maxdepth):
             depth=generate_child_for_A(newlist,puzzles,puzzles_cost,depth)
          
          
          if(len(puzzles)==0):
              print("Number of puzzles treated",len(tracking))
              print("goal not reached")
              print("--- %s seconds ---" % (time.time() - start_time))
        return tracking







puzzles=[]
puzzles=[]
puzzles_cost=[]
goal=State([1,2,3,8,0,4,7,6,5])
puzzle_test = [1,2,3,8,4,5,7,0,6]
puzzle=State(puzzle_test)
tracking=A_star(puzzle,goal,50,puzzles,puzzles_cost)

