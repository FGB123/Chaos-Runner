import pygame
from pygame import time
from pygame.locals import *
import pygame_menu
import random
import time

pygame.init()

def story2():
    screen = pygame.display.set_mode([800, 600])
    surface = pygame.Surface((800, 600)) 
    pygame.display.set_caption('Chaos run (Press space to continue)')
    bg = pygame.image.load("images/story3.png")
    running = True  
    time = 0
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        time += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg, (0, 0))
        pygame.display.flip()

def story1():
    screen = pygame.display.set_mode([800, 600])
    surface = pygame.Surface((800, 600)) 
    pygame.display.set_caption('Chaos run (Press space to continue)')
    bg = pygame.image.load("images/story2.png")
    running = True
    clock = pygame.time.Clock()
    time = 0  
    while running:
        clock.tick(60)
        time += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if time > 120:
                story2()

        screen.blit(bg, (0, 0))
        pygame.display.flip()

def story():
    screen = pygame.display.set_mode([800, 600])
    surface = pygame.Surface((800, 600)) 
    pygame.display.set_caption('Chaos run (Press space to continue)')
    bg = pygame.image.load("images/story1.png")
    running = True  
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            story1()


        screen.blit(bg, (0, 0))
        pygame.display.flip()

def won():
    surface = pygame.display.set_mode((800, 600))

    menu = pygame_menu.Menu('You destroyed precise city! People now finnaly can do what they want!', 800, 600,
                        theme=pygame_menu.themes.THEME_DARK)

    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)

def die():
    surface = pygame.display.set_mode((800, 600))

    menu = pygame_menu.Menu('You failed your mission!', 800, 600,
                        theme=pygame_menu.themes.THEME_DARK)

    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)


def game():

    px = 400
    py = 300
    health = 10

    trashx = 800
    trashspeed = 8

    playervar = [px, py, health]
    screen = pygame.display.set_mode([800, 600])
    surface = pygame.Surface((800, 600))

    GRAV = 0.4
    fallspeed = 0

    dead = pygame.mixer.Sound('images/dead.wav')


    bg = pygame.image.load("images/backgorund.png")
    pl = pygame.image.load("images/runner.jpg")
    pl = pygame.transform.scale(pl, (100, 80))

    trash = pygame.image.load("images/car.jpg")
    trash = pygame.transform.scale(trash, (70, 75))

    chaser = pygame.image.load("images/chaser.jpg")
    chaser = pygame.transform.scale(chaser, (120, 100))

    pygame.font.init()

    pygame.display.set_caption('Chaos run')

    jumpnum = 0

    clock = pygame.time.Clock()

    myfont = pygame.font.SysFont('arial', 30)

    chaos = 10

    timer = 0

    press = ""
    presschaos = False
    pressede = False

    running = True
    while running:
        clock.tick(60)

        timer += 1

        textsurface = myfont.render('Chaos-meter: ' + str(chaos) + '%', False, (0, 0, 0))
        textsurface1 = myfont.render(press, False, (0, 0, 0))

        keys = pygame.key.get_pressed()
        #if keys[pygame.K_a]:
        #    if playervar[0] - 4 > 0:
        #        playervar[0] -= 4
        #if keys[pygame.K_d]:
        #    if playervar[0] + 4 < 800:
        #        playervar[0] += 4
        if keys[pygame.K_SPACE]:
            if jumpnum < 6:
                playervar[1] -= 6
                jumpnum += 0
            if jumpnum >= 6:
                jumpnum = 0
        if keys[pygame.K_e]:
            if presschaos:
                chaos += random.randint(1, 7)
                presschaos = False
                pressede = True

        if keys[pygame.K_h]:
            input("")

        if keys[pygame.K_ESCAPE]:
            running = False

        if trashx > -10:
            trashx -= trashspeed
        else:
            trashx = 800
            trashspeed = random.randint(6, 12)


        if playervar[1] < 450:
            playervar[1] +=  fallspeed
            fallspeed += GRAV

        if playervar[1] > 450:
            fallspeed = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if timer >= 340:
            presschaos = True
            press = "PRESS E!"
            if timer >= 400 or pressede:
                timer = 0
                presschaos = False
                pressede = False
                press = ""

        if chaos >= 100:
            won()
            running = False

        if trashx > 460 and trashx < 470:
            print("HHHHHHHHHHHHHHHHHH")
            if playervar[1] > 415:
                try:
                    dead.stop()
                except:
                    pass
                dead.play()
                time.sleep(1)
                die()
                running = False

        #if trashx == 408:
        #    print(str(playervar[0] - trashx))
        #    if playervar[0] - trashx < -10:
        #        die()

        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))

        pygame.draw.line(screen, (0, 0, 0), (0, 590), (799, 590), 4)

        #pygame.draw.circle(screen, (0, 0, 255), (playervar[0], playervar[1]), 15)
        screen.blit(pl, (playervar[0], playervar[1]))
        screen.blit(trash, (trashx, 475))
        screen.blit(chaser, (50, 456))
        screen.blit(textsurface,(20,20))
        screen.blit(textsurface1,(20,45))

        pygame.display.flip()
        print(str(playervar[1]))
        

surface = pygame.display.set_mode((800, 600))

menu = pygame_menu.Menu('Chaos Runner', 800, 600,
                       theme=pygame_menu.themes.THEME_DARK)

menu.add.button('Play', game)
menu.add.button('Story', story)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)

pygame.quit() 