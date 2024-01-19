import os

class SingleFoodSearchProblem:
     def __init__(self, filename):
          self.maze = self.read_maze(filename)
          self.initial_state = self.get_initial_state()
          self.goal_state = self.get_goal_state()

     def read_maze(self, filename):
          with open(filename, 'r') as f:
               maze = [line.strip() for line in f]
          return maze

     def display_maze(self, curr_state):
          
          os.system('cls')
          for i in range(len(self.maze)):
            row = ''
            for j in range(len(self.maze[i])):
                if (i, j) == curr_state:
                    row += 'P'
                elif self.maze[i][j] == '.':
                    row += '.'
                else:
                    row += self.maze[i][j]
            print(row)
          input("Press Enter to continue...")

     def get_initial_state(self) -> tuple:
          for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'P':
                    return (i, j)
          return None

     def get_goal_state(self) -> tuple:
          for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == '.':
                    return (i, j)
          return None

     def get_successor(self, curr_state):
          successors = []
          x, y = curr_state
          if x > 0 and self.maze[x-1][y] != '%':
               successors.append(('N', 1, (x-1, y)))
          if x < len(self.maze) - 1 and self.maze[x+1][y] != '%':
               successors.append(('S', 1, (x+1, y)))
          if y > 0 and self.maze[x][y-1] != '%':
               successors.append(('W', 1, (x, y-1)))
          if y < len(self.maze[0]) - 1 and self.maze[x][y+1] != '%':
               successors.append(('E', 1, (x, y+1)))
          return successors

     def isGoal(self, curr_state):
          if curr_state == self.goal_state: return True
          return False

     def path_cost(self, action):
          return action + 1

     def animate(self, actions):
          curr_state = self.initial_state
          self.display_maze(curr_state)
          for action in actions:
               if action == 'N':
                    curr_state = (curr_state[0]-1, curr_state[1])
               elif action == 'S':
                    curr_state = (curr_state[0]+1, curr_state[1])
               elif action == 'W':
                    curr_state = (curr_state[0], curr_state[1]-1)
               elif action == 'E':
                    curr_state = (curr_state[0], curr_state[1]+1)
               elif action == 'Stop':
                   return
               self.display_maze(curr_state)


class MultiFoodSearchProblem:
     def __init__(self, filename):
          self.maze = self.read_maze(filename)
          self.initial_state = self.get_initial_state()
          self.goal_state = self.get_goal_state()

     def read_maze(self, filename):
          with open(filename, 'r') as f:
               maze = [line.strip() for line in f]
          return maze

     def display_maze(self, curr_state):
          
          os.system('cls')
          for x in range(len(self.maze)):
            row = ''
            for y in range(len(self.maze[x])):
                if (x, y) == curr_state:
                    row += 'P'
                elif self.maze[x][y] == '.':
                    row += '.'
                else:
                    row += self.maze[x][y]
            print(row)
          input("Press Enter to continue...")

     def get_initial_state(self) -> tuple:
          for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'P':
                    return (i, j)
          return None

     def get_goal_state(self) -> list:
          goal_state = []
          for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == '.':
                    goal_state.append((i, j))
          return goal_state

     def get_successor(self, curr_state):
          successors = []
          x, y = curr_state
          if x > 0 and self.maze[x-1][y] != '%':
               successors.append(('N', 1, (x-1, y)))
          if x < len(self.maze) - 1 and self.maze[x+1][y] != '%':
               successors.append(('S', 1, (x+1, y)))
          if y > 0 and self.maze[x][y-1] != '%':
               successors.append(('W', 1, (x, y-1)))
          if y < len(self.maze[0]) - 1 and self.maze[x][y+1] != '%':
               successors.append(('E', 1, (x, y+1)))
          return successors

     def isGoal(self, curr_state):
          if curr_state == self.goal_state: return True
          return False
     def  is_wall(self, state):
         x, y = state
         return self.maze[x][y] == "%"
     
     def path_cost(self, action):
          return action + 1

     def animate(self, actions):
          curr_state = self.initial_state
          self.display_maze(curr_state)
          for action in actions:
               if action == 'N':
                    curr_state = (curr_state[0]-1, curr_state[1])
               elif action == 'S':
                    curr_state = (curr_state[0]+1, curr_state[1])
               elif action == 'W':
                    curr_state = (curr_state[0], curr_state[1]-1)
               elif action == 'E':
                    curr_state = (curr_state[0], curr_state[1]+1)
               elif action == 'Stop':
                   return
               self.display_maze(curr_state)