from state import State 
from puzzle import Board                             
from pila import Pile
import time

def comparaison(puzzle,children):
        test=False
        for x in children:
            if (puzzle==x):
                test=True
        return test


def generate_child_for_DFS(puzzle,children,p,depth,childrennum):
    t1,t2,t3,t4=False,False,False,False
    childrennum=0
    if (puzzle.up() and not(comparaison(puzzle.up(),children))):
        y=puzzle.up()
        children.append(y)
        p.empiler(y)
        t1=True
        childrennum+=1

    if (puzzle.down() and not(comparaison(puzzle.down(),children))):
        y=puzzle.down()
        children.append(y)
        p.empiler(y)
        t2=True
        childrennum+=1 

    if (puzzle.right() and not(comparaison(puzzle.right(),children))):
        y=puzzle.right()
        children.append(y)
        p.empiler(y)
        t3=True
        childrennum+=1

    if (puzzle.left() and not(comparaison(puzzle.left(),children))):
        y=puzzle.left()
        children.append(y)
        p.empiler(y)
        t4=True
        childrennum+=1

    if(t1 or t2 or t3 or t4):
        depth+=1     
    return depth,childrennum
   

def DFS(puzzle,goal,maxdepth,p,children): 
    depth=1
    p.empiler(puzzle)
    newlist=State()
    newlist=puzzle
    tracking=[]
    if(newlist==goal):
        tracking.append(newlist.transform())
        print(newlist)
    else:
        while(goal!=newlist and not p.estVide()):
          childrennum=0
          newlist=p.depiler()
          tracking.append(newlist.transform())
          print(newlist)
          if(newlist==goal):
                print("Number of puzzles treated",len(tracking))
                print("goal reached")
                break

          depth,childrennum=generate_child_for_DFS(newlist,children,p,depth,childrennum)
          
          if(depth==maxdepth):
              depth=depth-1
              test=False
              while(childrennum>0 and test==False and not p.estVide()):
                 newlist=p.depiler()
                 childrennum-=1
                 print(newlist)
                 if(goal==newlist):
                     test=True
          if(p.estVide() and test==False):
              print("Number of puzzles treated",len(tracking))
              print("goal not reached")

        
        return tracking

puzzle_test = [1,2,3,8,4,5,7,0,6]
puzzle=State(puzzle_test)
goal=State([1,2,3,8,0,4,7,6,5])
children=[]
children.append(puzzle)
p=Pile()


tracking=DFS(puzzle,goal,50,p,children)

print(tracking[len(tracking)-1])
   
