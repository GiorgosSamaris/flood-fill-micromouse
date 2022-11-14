import numpy as np
import matplotlib.pyplot as plt

MAZE_WIDTH = 8
MAZE_HEIGHT = 8

class Cell:
    def __init__(self, x, y) -> None:
        self.visited 
        self.x = x
        self.y = y
        self.wall_n = True
        self.wall_w = True
        self.wall_s = True
        self.wall_e = True

#Class for generating a random maze
class MazeGenerator:
    def __init__(self) -> None:

        #Create maze
        maze = []
        for i in range(0,MAZE_WIDTH-1):
            for j in range(0,MAZE_HEIGHT-1):
                cl = Cell(i, j)
                maze.append(cl)

        #Set goal cells

        g_indx = ((MAZE_WIDTH // 2) -1)*((MAZE_HEIGHT // 2) -1)            #    ________
        goal_cell = maze[g_indx]                                           #    |                                                
        goal_cell.wall_w = False                                           #    |  G1   
        goal_cell.wall_s = False                                           #    |     


        g_indx = (MAZE_WIDTH // 2)*((MAZE_HEIGHT // 2) -1)                 #    ________
        goal_cell = maze[g_indx]                                           #            |                                         
        goal_cell.wall_e = False                                           #       G2   |
        goal_cell.wall_s = False                                           #            |


        g_indx = ((MAZE_WIDTH // 2) -1)*(MAZE_HEIGHT // 2)                 #    |
        goal_cell = maze[g_indx]                                           #    |  G3                                             
        goal_cell.wall_n = False                                           #    |  
        goal_cell.wall_w = False                                           #    |________  


        g_indx = (MAZE_WIDTH // 2)*(MAZE_HEIGHT // 2)                      #            |
        goal_cell = maze[g_indx]                                           #       G4   |                                        
        goal_cell.wall_e = False                                           #            |
        goal_cell.wall_n = False                                           #    ________|     


        