from time import sleep
from tkinter import *
from DFS import *
from BFS import *
from A_ import *


ch1=''
ch2=''
root = Tk()
root.geometry("800x500")



limit=0
a=0
d=0
b=0

lst = ['1', '2', '3', '8', '4', '5', '7', '0', '6']   

total_rows = 3
total_columns = 3

def number():
    try:
        global limit
        int(box_limit.get())
        limit=int(box_limit.get())
        answer.config(text="Votre limite est sauvgarder")
    except ValueError:
        answer.config(text="Entrer un numero valide")           





def execute_DFS():
    global limit  
    def itiration_DFS():
        global ch1
        global ch2
        global d
        if d<len(tracking)-1 :
         #button_itirations.config(relief=SUNKEN)
         #button_itirations.config(state=DISABLED)   
         d=d+1
         c=-1
         for i in range(3):
             for j in range(3):
                 e = Entry(root, width=10, fg='green',
                                font=('Arial',25,'bold'),justify='center')
                 e.grid(ipady=30)               
                 c=c+1  
                 e.grid(row=i, column=j)
                 e.insert(END, tracking[d][c])
        else:
            global ch2
            global ch1 
            ch1= "Number of puzzles treated "+str(len(tracking))
            num_dfs.config(text=ch1)
            button_itirations_DFS.config(state=DISABLED)
            if tracking[len(tracking)-1]==['1', '2', '3', '8', '0', '4', '7', '6', '5']:
                ch2=" goal reached"
                reach_dfs.config(text=ch2)
            else:
                ch2=" goal not reached"
                reach_dfs.config(text=ch2)




    puzzle_test = [1,2,3,8,4,5,7,0,6]
    puzzle=State(puzzle_test)
    goal=State([1,2,3,8,0,4,7,6,5])
    children=[]
    children.append(puzzle)
    p=Pile()
    tracking=DFS(puzzle,goal,limit,p,children)
    
    button_itirations_DFS= Button(root, text="Itirations DFS", command=itiration_DFS,state=NORMAL)
    button_itirations_DFS.place(x=600,y=200)
    
    

    
        
        
    







def execute_BFS():
    global limit  
    def itiration_BFS():
        
        global a
        if a<len(tracking)-1 :
         #button_itirations.config(relief=SUNKEN)
         #button_itirations.config(state=DISABLED)   
         a=a+1
         c=-1
         for i in range(3):
             for j in range(3):
                 e = Entry(root, width=10, fg='green',
                                font=('Arial',25,'bold'),justify='center')
                 e.grid(ipady=30)               
                 c=c+1  
                 e.grid(row=i, column=j)
                 e.insert(END, tracking[a][c])
        else:
            global ch2
            global ch1 
            ch1= "Number of puzzles treated "+str(len(tracking))
            num_bfs.config(text=ch1)
            button_itirations_BFS.config(state=DISABLED)
            if tracking[len(tracking)-1]==['1', '2', '3', '8', '0', '4', '7', '6', '5']:
                ch2=" goal reached"
                reach_bfs.config(text=ch2)
            else:
                ch2=" goal not reached"
                reach_bfs.config(text=ch2)

    puzzle_test = [1,2,3,8,4,5,7,0,6]
    puzzle=State(puzzle_test)
    goal=State([1,2,3,8,0,4,7,6,5])
    children=[]
    children.append(puzzle)
    f=File()
    tracking=BFS(puzzle,goal,limit,f,children)
    button_itirations_BFS= Button(root, text="Itirations BFS", command=itiration_BFS,state=NORMAL)
    button_itirations_BFS.place(x=600,y=250)
    


  

def execute_A():
    global limit  
    def itiration_A():
        
        global b
        if b<len(tracking)-1 :
         #button_itirations.config(relief=SUNKEN)
         #button_itirations.config(state=DISABLED)   
         b=b+1
         c=-1
         for i in range(3):
             for j in range(3):
                 e = Entry(root, width=10, fg='green',
                                font=('Arial',25,'bold'),justify='center')
                 e.grid(ipady=30)               
                 c=c+1  
                 e.grid(row=i, column=j)
                 e.insert(END, tracking[b][c])
        else:
            global ch2
            global ch1 
            ch1= "Number of puzzles treated "+str(len(tracking))
            num_A.config(text=ch1)
            button_itirations_A.config(state=DISABLED)
            if tracking[len(tracking)-1]==['1', '2', '3', '8', '0', '4', '7', '6', '5']:
                ch2=" goal reached"
                reach_A.config(text=ch2)
            else:
                ch2=" goal not reached"
                reach_A.config(text=ch2)

    puzzles=[]
    puzzles=[]
    puzzles_cost=[]
    goal=State([1,2,3,8,0,4,7,6,5])
    puzzle_test = [1,2,3,8,4,5,7,0,6]
    puzzle=State(puzzle_test)
    tracking=A_star(puzzle,goal,limit,puzzles,puzzles_cost)
    button_itirations_A= Button(root, text="Itirations A*", command=itiration_A,state=NORMAL)
    button_itirations_A.place(x=600,y=300)



def init():
    num_bfs.config(text='')
    num_dfs.config(text='')
    reach_bfs.config(text='')
    reach_dfs.config(text='')
    num_A.config(text='')
    reach_A.config(text='')
    global a
    global b
    global d
    c=-1
    a=0
    d=0
    b=0     
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=10, fg='green',
                               font=('Arial',25,'bold'),justify='center')
            e.grid(ipady=30)               
            c=c+1  
            e.grid(row=i, column=j)
            e.insert(END, lst[c])
         
                  




button_dfs= Button(root, text="Depth First Search", command=execute_DFS)

button_A= Button(root, text="A* Search", command=execute_A)
button_bfs= Button(root, text="Breadth First Search", command=execute_BFS)
button_init= Button(root, text="Initialize", command=init)


label= Label(root, text="Enter Limit")

box_limit= Entry(root)

button_limit= Button(root, text="submit limit", command=number)


num_dfs = Label(root, text='')
num_dfs.place(x=600,y=350)
reach_dfs = Label(root, text='')
reach_dfs.place(x=600,y=400)

num_bfs = Label(root, text='')
num_bfs.place(x=600,y=350)
reach_bfs = Label(root, text='')
reach_bfs.place(x=600,y=400)

num_A = Label(root, text='')
num_A.place(x=600,y=350)
reach_A = Label(root, text='')
reach_A.place(x=600,y=400)


answer= Label(root, text='')
answer.place(x=100,y=450)
button_init.place(x=600,y=150)
button_bfs.place(x=600, y=50)
button_dfs.place(x=600, y=100)
button_A.place(x=600, y=0)
button_limit.place(x=250, y=396)
label.place(x=100,y=370)
box_limit.place(x=100,y=400)





root.mainloop()