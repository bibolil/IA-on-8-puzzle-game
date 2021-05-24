from state import State 
from puzzle import Board                             
from fila import File
import time

def comparaison(puzzle,children):
        test=False
        for x in children:
            if (puzzle==x):
                test=True
        return test


def generate_child_for_BFS(puzzle,children,f,depth):
    t1,t2,t3,t4=False,False,False,False
    
    if (puzzle.up() and not(comparaison(puzzle.up(),children))):
        y=puzzle.up()
        children.append(y)
        f.enfiler(y)
        t1=True
        

    if (puzzle.down() and not(comparaison(puzzle.down(),children))):
        y=puzzle.down()
        children.append(y)
        f.enfiler(y)
        t2=True
        
    if (puzzle.right() and not(comparaison(puzzle.right(),children))):
        y=puzzle.right()
        children.append(y)
        f.enfiler(y)
        t3=True
        

    if (puzzle.left() and not(comparaison(puzzle.left(),children))):
        y=puzzle.left()
        children.append(y)
        f.enfiler(y)
        t4=True
        

    if(t1 or t2 or t3 or t4):
        depth+=1     
    return depth
   

def BFS(puzzle,goal,maxdepth,f,children): 
    start_time = time.time()
    depth=1
    f.enfiler(puzzle)
    newlist=State()
    newlist=puzzle
    tracking=[]
    if(newlist==goal):
        tracking.append(newlist.transform())
        print(newlist)
    else:
        while(goal!=newlist and not f.estVide()):
          newlist=f.defiler()
          tracking.append(newlist.transform())
          print(newlist)
          if(newlist==goal):
                print("Number of puzzles treated",len(tracking))
                print("goal reached")
                print("--- %s seconds ---" % (time.time() - start_time))
                break

          if(depth!=maxdepth):
             depth=generate_child_for_BFS(newlist,children,f,depth)
          
          
          if(f.estVide()):
              print("Number of puzzles treated",len(tracking))
              print("goal not reached")
              print("--- %s seconds ---" % (time.time() - start_time))
        return tracking


#puzzle_test = [1,2,3,8,4,5,7,0,6]
#puzzle=State(puzzle_test)
#goal=State([1,2,3,8,0,4,7,6,5])
#children=[]
#children.append(puzzle)
#f=File()
#tracking=BFS(puzzle,goal,100,f,children)