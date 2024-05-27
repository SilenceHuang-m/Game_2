import pygame
from Character import Pemain
import random
pygame.init()

width, height = 400, 700
layar = pygame.display.set_mode((width, height))
image = pygame.image.load("sprites/spaceship.png")
pygame.display.set_icon(image)
pygame.display.set_caption("Space Blazers")
music = pygame.mixer.music.load("sound/space1.wav")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

latar = pygame.transform.scale(pygame.image.load("sprites/space1.jpg"),(width, height))
awalkiri = pygame.image.load("sprites/left.png")
awalkanan = pygame.image.load("sprites/right.png")
awaltengah = pygame.image.load("sprites/spaceship.png")
font = pygame.font.Font("font/Pixeltype.ttf", 60)
font1 = pygame.font.Font("font/Pixeltype.ttf", 30)
font2 = pygame.font.Font("font/Pixeltype.ttf", 24)
font3 = pygame.font.Font("font/Pixeltype.ttf", 35)
judul = font.render("Space Survival", True, "Green")
masuk = font1.render("Press Enter to Play", True, "White")
createdbywho = font1.render("Created by", True, "White")
createdby = font1.render("Silence", True, "Green")
imageawal = pygame.image.load("sprites/asteroid.png")
versi = font2.render("Version 1.0.1", True, "red")

asteroid = pygame.image.load("sprites/asteroid1.png")
panjang_meteor = 31
tinggi_meteor = 70
min_distance = 30

def drawGame(waktu_game):
    layar.blit(latar, (0,0))
    skor = font3.render(f"Score : {round(waktu_game)}",True, "Green")
    layar.blit(skor,(20,20))
    spaceship.gambar(layar)
    for meteorit in meteor:
        layar.blit(asteroid, meteorit)
    pygame.display.update()

def aset():
    layar.blit(latar, (0,0))
    layar.blit(imageawal, (100, 60))
    layar.blit(judul, (65, 100))
    layar.blit(awalkiri, (40, 300))
    layar.blit(awalkanan, (298, 300))
    layar.blit(awaltengah,(140, 400))
    layar.blit(masuk, (115, 300))
    layar.blit(createdbywho, (120, 140))
    layar.blit(createdby, (223, 140))
    layar.blit(versi, (155, 350))
    pygame.display.update()

def reset_game():
    global spaceship, meteor, mulai, waktu_game, game_over, hitung_meteor, start_game
    spaceship = Pemain(30, 620, 40, 60)
    meteor = []
    mulai = pygame.time.get_ticks()
    waktu_game = 0
    game_over = False
    hitung_meteor = 0
    start_game = False

spaceship = Pemain(30, 620, 40, 60)
start_game = False
gameON = True
mulai = pygame.time.get_ticks()
waktu_game = 0
game_over = False
slot_meteor = 3000
hitung_meteor = 0
meteor = []

while gameON:
    hitung_meteor += clock.tick(60)
    waktu_game = (pygame.time.get_ticks() - mulai) / 1000

    if hitung_meteor > slot_meteor:
        for _ in range(4):
            meteorit_x = random.randint(0, width - panjang_meteor)
            meteorit_y = -tinggi_meteor
            meteor.append((meteorit_x, meteorit_y))
        hitung_meteor = 0

    if not game_over:
        for i in range(len(meteor)):
            meteor[i] = (meteor[i][0], meteor[i][1] + 5)

        for meteorit in meteor:
            if spaceship.x < meteorit[0] + panjang_meteor and spaceship.x + spaceship.width > meteorit[0] and spaceship.y < meteorit[1] + tinggi_meteor and spaceship.y + spaceship.height > meteorit[1]:
                fontkata = pygame.font.Font("font/Pixeltype.ttf", 80)
                kata = fontkata.render("Game Over", False, "Red")
                kata1 = font3.render(f"Score : {round(waktu_game)}", False, "Red")
                layar.blit(kata, (82, 300))
                layar.blit(kata1, (149, 350))
                pygame.display.update()
                game_over = True
                pygame.time.delay(2000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameON = False
        if event.type == pygame.KEYDOWN and game_over and event.key == pygame.K_RETURN:
            reset_game()

    if game_over:
        aset()
    else:
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and spaceship.x < width - spaceship.width - spaceship.vel:
            spaceship.x += spaceship.vel
            spaceship.right = True
            spaceship.left = False
        if key[pygame.K_a] and spaceship.x > spaceship.vel:
            spaceship.x -= spaceship.vel
            spaceship.left = True
            spaceship.right = False
        if key[pygame.K_w] and spaceship.y > spaceship.vel:
            spaceship.y -= spaceship.vel
        if key[pygame.K_s] and spaceship.y < height - spaceship.height - spaceship.vel:
            spaceship.y += spaceship.vel

        if key[pygame.K_RETURN]:
            start_game = True

        if start_game:
            drawGame(waktu_game)
        else:
            aset()

pygame.quit()
