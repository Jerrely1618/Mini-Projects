import pygame
import numpy as np
from time import sleep
import random

pygame.init()

class Triangle():
    def __init__(self):
        self.screen = pygame.display.set_mode((600,600))
        pygame.display.set_caption("Sierpi")
        self.vertices = [[295,5],[5,595],[595,595]]
        # np.random.randint(100,500,(3,2))

        
    def run(self):
        self.screen.fill((255,255,255))
        for i,point in enumerate(self.vertices):
            pygame.draw.circle(self.screen,'black',point,1)
        initial = (200,200)
        pygame.draw.circle(self.screen,'black',initial,1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            randomVertex= self.vertices[random.randint(0,2)]
            xNew = (randomVertex[0] + initial[0]) / 2
            yNew = (randomVertex[1] + initial[1]) / 2
            initial = (xNew,yNew)
            pygame.draw.circle(self.screen,'black',initial,1)
            # sleep(0.1)
            pygame.display.update()
    
if __name__ == "__main__":
    sierpi = Triangle()
    sierpi.run()
    