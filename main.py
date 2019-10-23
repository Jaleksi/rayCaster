import pygame
import math
from random import randint

import intersecter

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("varjot")
clock = pygame.time.Clock()

black, white = [0, 0, 0], [255, 255, 255]



def inbut():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            gameLoop() # Enter = new blocks

class Este:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def drawEste(self):
        self.startPos = [self.x1, self.y1]
        self.endPos = [self.x2, self.y2]
        pygame.draw.line(screen, white, self.startPos, self.endPos, 3)



class Ray:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def endPoint(self): # Säteen asento hiireen nähden
        return [int(self.x+600 * math.sin(self.angle * math.pi / 180)),
                        int(self.y+600 * math.cos(self.angle * math.pi / 180))]
    
    def drawRay(self, esteet):
        self.x, self.y = pygame.mouse.get_pos()
        self.startPos = [self.x, self.y]
        self.endPos = self.endPoint()
        self.closest = 999999 # Lähimmän halkaisupisteen etäisyys

        for este in esteet:
            # Jos este halkaisee säteen
            if intersecter.intersects(self.startPos, self.endPos, este.startPos, este.endPos):
                possibleNewEnd = intersecter.intersectPoint(self.startPos, self.endPos,
                                este.startPos, este.endPos)
                # Etäisyys halkaisupisteeseen
                tmp = intersecter.pointDistance(self.startPos, possibleNewEnd)
                # Talletetaan lähin halkaisupiste
                if tmp < self.closest:
                    self.closest = tmp
                    self.endPos = possibleNewEnd
            

        pygame.draw.line(screen, white, self.startPos, self.endPos, 1)


def drawInterSect(ray, este):
    rs = ray.startPos
    re = ray.endPos
    es = este.startPos
    ee = este.endPos

    intersex = intersecter.intersectPoint(rs, re, es, ee)
    # Vältetään jakaminen nollalla
    if intersex == 0:
        pass
    else:
        pygame.draw.circle(screen, (0, 255, 0), intersex, 5)


def gameLoop():
    rays = [Ray(200, 200, i*5) for i in range(1,73)]
    # Esteet random-sijainteihin ruudulle
    esteet = [Este(randint(0,400), randint(0,400),
            randint(0,400), randint(0,400)) for _ in range(6)]
    while 1:
        inbut()
        screen.fill(black)
        for este in esteet:
            este.drawEste()
        for ray in rays:
            ray.drawRay(esteet)
        clock.tick(20)
        pygame.display.flip()

if __name__ == "__main__":
    gameLoop()
