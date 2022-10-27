import pygame
from pygame.locals import *

running = True
playing = True
pygame.init()
display = pygame.display.set_mode((1200,900))
screen = pygame.Surface((800,600))
scaled_screen = pygame.Surface((1200,900))
clock = pygame.time.Clock()
pygame.display.set_caption("FactoPy")

resources = {
    "miner": pygame.image.load("assets/miner.png")
}

def get_tile_pos(mouse_pos):
    return (mouse_pos[0]-(mouse_pos[0]%50),mouse_pos[1]-(mouse_pos[1]%50))

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))

    rect_pos = get_tile_pos((pygame.mouse.get_pos()[0]/1.5,pygame.mouse.get_pos()[1]/1.5))
    #pygame.draw.rect(screen,(255,255,255),(rect_pos[0],rect_pos[1],50,50))
    screen.blit(resources["miner"],rect_pos)
    
    pygame.transform.scale(screen,(1200,900),scaled_screen)
    display.blit(scaled_screen,(0,0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()