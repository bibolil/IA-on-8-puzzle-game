from puzzle import Board
import string
class State:
    
    def __init__(self, initial_state=[]):
        self.current = Board(initial_state)

    def __eq__(self, other): 
        return self.current == other.current

   

    

    def __str__(self):
        return str(self.current)

    def __hash__(self):
        return hash(str(self))
    
    def transform(self):
        x=str(self)
        lista=[]
        for i in range(len(x)):
            if (x[i].isdigit()):
                lista.append(x[i])
        return lista    

    def up(self):
        up = self.current.up()
        if up is not False:
            return State(up)
        else:
            return False

    def down(self):
        down = self.current.down()
        if down is not False:
            return State(down)
        else:
            return False

    def left(self):
        left = self.current.left()
        if left is not False:
            return State(left)
        else:
            return False

    def right(self):
        right = self.current.right()
        if right is not False:
            return State(right)
        else:
            return False

    def generate(self):
        succ = []

        up = self.current.up()
        if up != False:
            succ.append(State(up))


        down = self.current.down()
        if down != False:
            succ.append(State(down))


        left = self.current.left()
        if left != False:
            succ.append(State(left))


        right = self.current.right()
        if right != False:
            succ.append(State(right))

        return succ