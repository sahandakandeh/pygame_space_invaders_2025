# 0. Set Working directory
import os
os.chdir("e:/Artin_sahand/Space_Invaders")
# 1. Import pygame
import pygame
# 26. import numpy to use random modul
import numpy as np

# 3Add background sound (later)
# 58. Import mixer to load and repeat a music(later)
from pygame import mixer
# 2. Initialize pygame(otherwise your code is not going to work)
pygame.init()

# 3. Create the game screen (set_mode)
screen = pygame.display.set_mode((800, 600))
# 4. Run (It's hanging)

# Changing the title, logo and background color
# 8. Set the title of game window (set_caption)
pygame.display.set_caption("Space_Invaders")
# 32. Adding a background image which is (800, 600) pixels, like the size of our game screen
# https://www.freepik.com/  (search colorful spaceship background)
background = pygame.image.load("background.png")

# 59. Adding sounds and background music (later)
# https://github.com/attreyabhatt/Space-Invaders-Pygame/
# 1. Background.wav 2. laser.wav 3. explosion.wav
# put -1 to play the music in loop not just one time
mixer.music.load("background.wav")
mixer.music.play(-1)

# 9. Set the icon of the game window (set_icon) (32*32)
# https://www.flaticon.com/search?word=spaceship
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
# 10. Run

# 13. Adding player image into our space invaders screen (64*64)
# https://www.flaticon.com/search?word=enemy
playerImg = pygame.image.load("player.png")

# 14. Set the initial position of the image on the screen
playerX = 370
playerY = 480

# 19. Define the initial speed of the player
playerX_change = 0

# 46. Create multiple enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
# 47. Create for-loop to set the number of enemies
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(np.random.randint(0 , 736))
    enemyY.append(np.random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# 34. Adding bullet image into our space invaders game (32*32) (add it later)
# https://www.flaticon.com/search?word=enemy
bulletImg = pygame.image.load("bullet.png")
bullets = [] # List to store multiple bullets
bulletY_change = 5

# 52. Remove score and change its name
score_value = 0
# 54. Create font
font = pygame.font.Font("freesansbold.ttf", 32)
# 55. Create text position
textX = 10
textY = 10
# 56 Create a function to put score_value inside game screen
def show_score(x, y):
    score = font.render("score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# 63. Set game over text font
over_font = pygame.font.Font("freesansbold.ttf", 64)
# 64. Create game over function
def game_over_text():
    over_text = over_font.render("GAME OVER" , True , (255 , 255, 255))
    screen.blit(over_text, (200, 250))

# 15. Create a function to put player image in the screen.
def player(x, y):
    screen.blit(playerImg, (x, y))
# 51. Get back to enemy function and set it for multiple enemies.
# 24. Create a function to put enemy image in the screen.
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# 36. Create a function to put bullet image in the screen.
def fire_bullet(x , y):
    bullet_sound = mixer.Sound("laser.wav")
    bullet_sound.play()
    bullets.append({"x": x + 16, "y": y + 10})

# 41.Define a function to set collision (distance function)
def iscollision(x1 , x2 , y1 , y2):
    distance = np.sqrt(np.power(x1 - x2 , 2) + np.power(y1 - y2, 2))
    if distance < 27:
        return True
    else:
        return False

# Game loop
running = True
# Add a variable to track if the spacebar is held down
spacebar_pressed = False
# Add a counter to control the firing rate
fire_rate_counter = 0
fire_rate = 5 # Fire every 5 frames

while running:
    screen.fill((128, 0, 128))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                spacebar_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_SPACE:
                spacebar_pressed = False

    # Movement mechanics of the player
    playerX += playerX_change

    # Checking for boundaries of spaceship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Handle rapid fire
    if spacebar_pressed and fire_rate_counter % fire_rate == 0:
        fire_bullet(playerX, playerY)
    fire_rate_counter += 1

    # Move and draw bullets
    bullets_to_remove = []
    for bullet in bullets:
        bullet["y"] -= bulletY_change
        screen.blit(bulletImg, (bullet["x"], bullet["y"]))
        if bullet["y"] < 0:
            bullets_to_remove.append(bullet)

    # Remove bullets that are off-screen
    for bullet in bullets_to_remove:
        bullets.remove(bullet)

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        if enemyX[i] < 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        # Check for collisions with bullets
        bullets_to_remove_enemy = []
        for bullet in bullets:
            collision = iscollision(bullet["x"], enemyX[i], bullet["y"], enemyY[i])
            if collision:
                xplosion_sound = mixer.Sound("explosion.wav")
                xplosion_sound.play()
                bullets_to_remove_enemy.append(bullet)
                score_value += 1
                enemyX[i] = np.random.randint(0 , 736)
                enemyY[i] = np.random.randint(50 , 150)
                break # Break inner loop since enemy is destroyed

        # Remove collided bullets
        for bullet in bullets_to_remove_enemy:
            bullets.remove(bullet)

        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()