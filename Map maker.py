import pygame
import os

pygame.init()
window = pygame.display.set_mode([500, 500])
floor = pygame.transform.scale(pygame.image.load(os.path.realpath("floor.png")), [50, 50])
wall = pygame.transform.scale(pygame.image.load(os.path.realpath("wall.png")), [50, 50])
corner = pygame.transform.scale(pygame.image.load(os.path.realpath("corner.png")), [50, 50])

room = [
    [2, 1, 1, 1, 1, 1, 1, 1, 1, [2, 1]],
    [[1, 3], 0, 0, 0, 0, 0, 0, 0, 0, [1, 1]],
    [[1, 3], 0, 0, 0, 0, 0, 0, 0, 0, [1, 1]],
    [[1, 3], 0, 0, 0, 0, 0, 0, 0, 0, [1, 1]],
    [[1, 3], 0, 0, 0, 0, 0, 0, 0, 0, [1, 1]],
    [[1, 3], 0, 0, 0, 0, 0, 0, 0, 0, [1, 1]],
    [[1, 3], 0, 0, 0, 0, 0, 0, 0, 0, [1, 1]],
    [[1, 3], 0, 0, 0, 0, 0, 0, 0, 0, [1, 1]],
    [[1, 3], 0, 0, 0, 0, 0, 0, 0, 0, [1, 1]],
    [[2, 3], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [2, 2]],
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))
    
    for x in range(10):
        for y in range(10):
            if type(room[y][x]) is int:
                if room[y][x] == 0:
                    window.blit(floor, [x * 50, y * 50])
                elif room[y][x] == 1:
                    window.blit(wall, [x * 50, y * 50])
                elif room[y][x] == 2:
                    window.blit(corner, [x * 50, y * 50])
            else:
                if room[y][x][0] == 1:
                    window.blit(pygame.transform.rotate(wall, room[y][x][1] * -90), [x * 50, y * 50])
                elif room[y][x][0] == 2:
                    window.blit(pygame.transform.rotate(corner, room[y][x][1] * -90), [x * 50, y * 50]) 

    pygame.display.flip()
    pygame.image.save(window, "screenshot.png")
    running = False

pygame.quit()
