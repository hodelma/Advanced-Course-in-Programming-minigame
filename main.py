# Pelissä on tarkoituksena kerätä kolikoita ja väistellä hirviöitä. Mikäli pelaaja osuu kolikkoon, pisteet nousevat.

# Jos pelaaja osuu hirviöön, pisteet nollaantuvat.

# Pelin ensisijainen tavoite on kerätä 20 kolikkoa osumatta hirviöihin. Tällöin pelaaja on läpäisee pelin ja näytölle 
# tulee voittojulistus!

# Aina kun kerää riittävän määrän kolikoita, pelin taustaväri vaihtuu.

# Haastavuutta tuo kohta, kun pelaaja saavuttaa 15 pistettä. Tällöin taustaväri muuttuu hirviöihin sulautuvaksi.

import pygame
import random

class Robotti:
    def __init__(self):
        self.robo = pygame.image.load("robo.png")
        self.x = 0
        self.y = 480 - self.robo.get_height()
        self.oikealle = False
        self.vasemmalle = False

    def piirra_robo(self,naytto):
        naytto.blit(self.robo,(self.x, self.y))

    def robotin_liike(self):
        if self.oikealle:
            if self.x + self.robo.get_width() <= 640:
                self.x += 2
        if self.vasemmalle:
            if self.x >= 0:
                self.x -= 2

    def get_width_robo(self):
        return self.robo.get_width()
    
    def get_height_robo(self):
        return self.robo.get_height()

class Kolikko:
    def __init__(self):
        self.kolikko = pygame.image.load("kolikko.png")
        self.x = random.randint(0, 590)
        self.y = random.randint(-840, -60)
        self.nopeus_y = 1

    def piirra_kolikko(self, naytto):
        naytto.blit(self.kolikko,(self.x, self.y))

    def kolikon_liike(self):
        self.y += self.nopeus_y

    def get_height_kolikko(self):
        return self.kolikko.get_height()
    
    def get_width_kolikko(self):
        return self.kolikko.get_width()

class Hirvio:
    def __init__(self):
        self.hirvio = pygame.image.load("hirvio.png")
        self.x = random.randint(0, 590)
        self.y = random.randint(-900, -60)
        self.nopeus_y = random.randint(1,3)

    def piirra_hirvio(self, naytto):
        naytto.blit(self.hirvio,(self.x, self.y))

    def hirvion_liike(self):
        self.y += self.nopeus_y
    
    def get_height_hirvio(self):
        return self.hirvio.get_height()

    def get_width_hirvio(self):
        return self.hirvio.get_width()

pygame.init()
naytto = pygame.display.set_mode((640, 480))
kello = pygame.time.Clock()

hirviot = []
kolikot = []
robotit = []

for i in range(7):
    hirviot.append(Hirvio())

for i in range(3):
    kolikot.append(Kolikko())

for i in range(1):
    robotit.append(Robotti())

pistemaara = 0

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                robot.vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                robot.oikealle = True

        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                robot.vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                robot.oikealle = False
            
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((100, 10, 255))

    if pistemaara >= 5:
        naytto.fill((100, 100, 255))
        
    if pistemaara >= 10:
        naytto.fill((90, 30, 100))

    if pistemaara >= 15:
        naytto.fill((10, 10, 10))

    if pistemaara == 20:
        naytto.fill((0, 0, 255))

    for robot in robotit:
        robot.piirra_robo(naytto)
        robot.robotin_liike()

    for hirvio in hirviot:
        hirvio.piirra_hirvio(naytto)
        hirvio.hirvion_liike()
        if pistemaara == 20:
            hirvio.y = -100
            hirvio.nopeus_y = 0

        if hirvio.y + hirvio.get_width_hirvio() >= 500:
            hirvio.x = random.randint(0, 590)
            hirvio.y = random.randint(-900, -60)

        if hirvio.y > robot.y - 60 and hirvio.x >= robot.x - 42 and hirvio.x <= (robot.x - 10 + robot.get_width_robo()):
            pistemaara = 0
            hirvio.x = random.randint(0, 590)
            hirvio.y = random.randint(-900, -60)

    for kolikko in kolikot:
        kolikko.piirra_kolikko(naytto)
        kolikko.kolikon_liike()
        if pistemaara == 20:
            kolikko.y = -100
            kolikko.nopeus_y = 0

        if kolikko.y + kolikko.get_width_kolikko() >= 500:
            kolikko.x = random.randint(0, 590)
            kolikko.y = random.randint(-600, -60)

        if kolikko.y > robot.y - 30 and kolikko.x >= robot.x - 30 and kolikko.x <= (robot.x + robot.get_width_robo()):
            pistemaara += 1
            kolikko.x = random.randint(0, 590)
            kolikko.y = random.randint(-600, -60)

    fontti = pygame.font.SysFont("Calibri", 25, bold = True)
    teksti = fontti.render("POINTS: " + str(pistemaara), True, (255, 0, 0))
    naytto.blit(teksti, (519, 450))

    if pistemaara == 20:
        fontti = pygame.font.SysFont("Impact", 80)
        teksti = fontti.render("YOU WIN!", True, (random.randint(0, 255) , random.randint(0, 255) , random.randint(0, 255)))
        naytto.blit(teksti, (170, 190))

    pygame.display.flip()
    kello.tick(120)
