from fringes import Queue, Stack, PriorityQueue
from problems import SingleFoodSearchProblem, MultiFoodSearchProblem
import os
import math

def get_path(src, dst, parents) -> list:
    path = []
    x = dst
    while x != - 1:
        path.append(x)
        x = parents[x]
    path.reverse()
    return path

def get_direction(path):
    direction = []
    for i in range(len(path) - 1):
        x_diff = path[i+1][0] - path[i][0]
        y_diff = path[i+1][1] - path[i][1]
        if x_diff == 1:
            direction.append('S')
        elif x_diff == -1:
            direction.append('N')
        elif y_diff == 1:
            direction.append('E')
        elif y_diff == -1:
            direction.append('W')
    direction.append('Stop')
    return direction


def bfs(problem) -> list:
    src = problem.initial_state
    dst = problem.goal_state
    if isinstance(problem, SingleFoodSearchProblem):#Case: SingleFoodSearchProblem
        if src == dst:
            expanded = []
            path = [src]
            return expanded, path
        
        path = []
        parents = dict()
        parents[src] = -1
        frontier = Queue()
        frontier.enqueue(src)
        expanded = []
        while not frontier.is_empty():
            cur = frontier.dequeue()
            expanded.append(cur)
            successors = problem.get_successor(cur)
            for (d, w, address) in successors:
                if address not in expanded and not frontier.contain(address):
                        if (address == dst):
                            parents[address] = cur
                            path = get_path(address, dst, parents)
                            direction = get_direction(path)
                            return direction
                        parents[address] = cur
                        frontier.enqueue(address)
    elif isinstance(problem, MultiFoodSearchProblem):  # Case: MultiFoodSearchProblem
        path_all = []
        path = []
        frontier = Queue()
        frontier.enqueue(src)
        parents = dict()
        parents[src] = -1
        expanded = []
        while not frontier.is_empty():
            cur = frontier.dequeue()
            expanded.append(cur)
            successors = problem.get_successor(cur)
            for d, w, successor in successors:
                if successor not in expanded and not frontier.contain(successor):
                    if(successor in dst):
                        dst.remove(successor)
                        parents[successor] = cur
                        path = get_path(src, successor, parents)
                        path_all += path
                        if(len(dst) == 0):
                            
                            path = []
                            for item in path_all:
                                path.append(item)
                            # print(path)
                            direction = get_direction(path_all)
                            return direction
                        else:
                            src = successor
                            path = []
                            expanded = []
                            frontier = Queue()
                            frontier.enqueue(src)
                            parents = dict()
                            parents[src] = -1
                            break
                    parents[successor] = cur
                    frontier.enqueue(successor)
        return []

def dfs(problem) -> list:
    src = problem.initial_state
    dst = problem.goal_state
    if isinstance(problem, SingleFoodSearchProblem):#Case: SingleFoodSearchProblem
        if src == dst:
            expanded = []
            path = [src]
            return expanded, path
        
        path = []
        parents = dict()
        parents[src] = -1
        frontier = Stack()
        frontier.push(src)
        expanded = []
        while not frontier.is_empty():
            cur = frontier.pop()
            expanded.append(cur)
            successors = problem.get_successor(cur)
            for (d, w, address) in successors:
                if address not in expanded and not frontier.contain(address):
                        if (address == dst):
                            parents[address] = cur
                            path = get_path(address, dst, parents)
                            direction = get_direction(path)
                            return direction
                        parents[address] = cur
                        frontier.push(address)
    elif isinstance(problem, MultiFoodSearchProblem):  # Case: MultiFoodSearchProblem
        path_all = []
        path = []
        frontier = Stack()
        frontier.push(src)
        parents = dict()
        parents[src] = -1
        expanded = []
        while not frontier.is_empty():
            cur = frontier.pop()
            expanded.append(cur)
            successors = problem.get_successor(cur)
            for d, w, successor in successors:
                if successor not in expanded and not frontier.contain(successor):
                    if(successor in dst):
                        dst.remove(successor)
                        parents[successor] = cur
                        path = get_path(src, successor, parents)
                        path_all += path
                        if(len(dst) == 0):
                            
                            path = []
                            for item in path_all:
                                path.append(item)
                            # print(path)
                            direction = get_direction(path_all)
                            return direction
                        else:
                            src = successor
                            path = []
                            expanded = []
                            frontier = Stack()
                            frontier.push(src)
                            parents = dict()
                            parents[src] = -1
                            break
                    parents[successor] = cur
                    frontier.push(successor)
        return []
        

def ucs(problem) -> list:
    src = problem.initial_state
    dst = problem.goal_state
    if isinstance(problem, SingleFoodSearchProblem):#Case: SingleFoodSearchProblem
        if src == dst:
            expanded = []
            path = [src]
            return expanded, path
        
        path = []
        parents = dict()
        parents[src] = -1
        frontier = PriorityQueue()
        frontier.push(src, 0)
        expanded = []
        while not frontier.is_empty():
            cur, cost = frontier.pop()
            expanded.append(cur)
            successors = problem.get_successor(cur)
            for (d, w, address) in successors:
                if address not in expanded and not frontier.contain(address):
                        if (address == dst):
                            parents[address] = cur
                            path = get_path(address, dst, parents)
                            direction = get_direction(path)
                            return direction
                        parents[address] = cur
                        frontier.push(address, cost + w)
    elif isinstance(problem, MultiFoodSearchProblem):  # Case: MultiFoodSearchProblem
        path_all = []
        path = []
        frontier = PriorityQueue()
        frontier.push(src, 0)
        parents = dict()
        parents[src] = -1
        expanded = []
        while not frontier.is_empty():
            cur, cost = frontier.pop()
            expanded.append(cur)
            successors = problem.get_successor(cur)
            for d, w, successor in successors:
                if successor not in expanded and not frontier.contain(successor):
                    if(successor in dst):
                        dst.remove(successor)
                        parents[successor] = cur
                        path = get_path(src, successor, parents)
                        path_all += path
                        if(len(dst) == 0):
                            
                            path = []
                            for item in path_all:
                                path.append(item)
                            # print(path)
                            direction = get_direction(path_all)
                            return direction
                        else:
                            src = successor
                            path = []
                            expanded = []
                            frontier = PriorityQueue()
                            frontier.push(src, 0)
                            parents = dict()
                            parents[src] = -1
                            break
                    parents[successor] = cur
                    frontier.push(successor, cost + w)
        return []

def manhattan(state):
    current, goal_state = state
    
    x_diff = abs(current[0] - goal_state[0])
    y_diff = abs(current[1] - goal_state[1])
    return float(x_diff + y_diff)

def euclidean(state):
    current, goal_state = state
    x_diff = current[0] - goal_state[0]
    y_diff = current[1] - goal_state[1]
    return int(math.sqrt(x_diff**2 + y_diff**2))

def multi_foods(state):
    current, goal_states = state
    distances = [abs(current[0]-goal[0]) + abs(current[1]- goal[1]) for goal in goal_states]
    min_distance = min(distances) if distances else 0
    return min_distance

def astar(problem, fn_heuristic) -> list:
    src = problem.initial_state
    dst = problem.goal_state
    if isinstance(problem, SingleFoodSearchProblem):#Case: SingleFoodSearchProblem
        if src == dst:
            expanded = []
            path = [src]
            return expanded, path
        
        path = []
        parents = dict()
        parents[src] = -1
        frontier = PriorityQueue()
        frontier.push(src, fn_heuristic((src, dst)))
        expanded = []
        while not frontier.is_empty():
            cur, cost = frontier.pop()
            expanded.append(cur)
            successors = problem.get_successor(cur)
            for (d, w, address) in successors:
                if address not in expanded and not frontier.contain(address):
                        if (address == dst):
                            parents[address] = cur
                            path = get_path(address, dst, parents)
                            direction = get_direction(path)
                            return direction
                        parents[address] = cur
                        frontier.push( address, cost + w + fn_heuristic((address, dst)))
    elif isinstance(problem, MultiFoodSearchProblem):  # Case: MultiFoodSearchProblem
        path_all = []
        path = []
        frontier = PriorityQueue()
        frontier.push( src, fn_heuristic((src, dst)) )
        parents = dict()
        parents[src] = -1
        expanded = []
        while not frontier.is_empty():
            cur, cost = frontier.pop()
            expanded.append(cur)
            successors = problem.get_successor(cur)
            for d, w, address in successors:
                if address not in expanded and not frontier.contain(address):
                    if(address in dst):
                        dst.remove(address)
                        parents[address] = cur
                        path = get_path(src, address, parents)
                        path_all += path
                        if(len(dst) == 0):
                            
                            path = []
                            for item in path_all:
                                path.append(item)
                            # print(path)
                            direction = get_direction(path_all)
                            return direction
                        else:
                            src = address
                            path = []
                            expanded = []
                            frontier = PriorityQueue()
                            frontier.push(src, fn_heuristic((src, dst)))
                            parents = dict()
                            parents[src] = -1
                            break
                    parents[address] = cur
                    frontier.push(address, cost + w + fn_heuristic((address, dst)))
        return []
    
def gbfs(problem, fn_heuristic) -> list:
    src = problem.initial_state
    dst = problem.goal_state
    if isinstance(problem, SingleFoodSearchProblem):#Case: SingleFoodSearchProblem
        if src == dst:
            expanded = []
            path = [src]
            return expanded, path
        
        path = []
        parents = dict()
        parents[src] = -1
        frontier = PriorityQueue()
        frontier.push(src, fn_heuristic((src, dst)))
        expanded = []
        while not frontier.is_empty():
            cur, cost = frontier.pop()
            expanded.append(cur)
            successors = problem.get_successor(cur)
            for (d, w, address) in successors:
                if address not in expanded and not frontier.contain(address):
                        if (address == dst):
                            parents[address] = cur
                            path = get_path(address, dst, parents)
                            direction = get_direction(path)
                            return direction
                        parents[address] = cur
                        frontier.push( address, fn_heuristic((address, dst)))
    elif isinstance(problem, MultiFoodSearchProblem):  # Case: MultiFoodSearchProblem
        path_all = []
        path = []
        frontier = PriorityQueue()
        frontier.push( src, fn_heuristic((src, dst)) )
        parents = dict()
        parents[src] = -1
        expanded = []
        while not frontier.is_empty():
            cur, cost = frontier.pop()
            expanded.append(cur)
            successors = problem.get_successor(cur)
            for d, w, address in successors:
                if address not in expanded and not frontier.contain(address):
                    if(address in dst):
                        dst.remove(address)
                        parents[address] = cur
                        path = get_path(src, address, parents)
                        path_all += path
                        if(len(dst) == 0):
                            
                            path = []
                            for item in path_all:
                                path.append(item)
                            # print(path)
                            direction = get_direction(path_all)
                            return direction
                        else:
                            src = address
                            path = []
                            expanded = []
                            frontier = PriorityQueue()
                            frontier.push(src, fn_heuristic((src, dst)))
                            parents = dict()
                            parents[src] = -1
                            break
                    parents[address] = cur
                    frontier.push(address, fn_heuristic((address, dst)))
        return []
    
