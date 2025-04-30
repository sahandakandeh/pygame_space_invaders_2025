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
pygame.display.set_caption("Space Invaders")
# 32. Adding a background image which is (800, 600) pixels, like the size of our game screen
# https://www.freepik.com/  (search colorful spaceship background)
background = pygame.image.load("background.png")
# 9. Set the icon of the game
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
# 59. Adding sounds and background music (later)
# https://github.com/attreyabhatt/Space-Invaders-Pygame/
# 1. Background.wav 2. laser.wav 3. explosion.wav
# put -1 to play the music in loop not just one time
mixer.music.load("background.wav")
mixer.music.play(-1)
# 9. Set the icon of the game window (set_icon) (32*32)
# https://www.flaticon.com/search?word=spaceship

# 10. Run

# 13. Adding player image into our space invaders screen (64*64)
# https://www.flaticon.com/search?word=enemy
playerImg = pygame.image.load("player.png")

# 14. Set the initial position of the image on the screen
playerX = 370
playerY = 480
# 19. Define the initial speed of the player
playerX_change = 0

# 23. Adding enemy image into our space invaders game (64*64) (add it later)
# https://www.flaticon.com/search?word=enemy
enemyImg = pygame.image.load("enemy.png")
'''
# 27. Use random module to set the enemy in a random position
enemyX = np.random.randint(0, 736)
enemyY = np.random.randint(50, 150)
enemyX_change =  3

# 30. We want enemy to move down 40 pixels when it hits the boundaries
enemyY_change = 40'''

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
    enemyX.append(np.random.randint(0, 736))
    enemyY.append(np.random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


# 34. Adding bullet image into our space invaders game (32*32) (add it later)
# https://www.flaticon.com/search?word=enemy
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
# 35. Set bullet state
bullet_state = "ready"
# ready = You can't see the bullet on the screen
# fire = The bullet is currently moving


# 52. Remove score and change its name
score_value = 0

# 54. Create font
# "freesansbold.ttf" is the only font inside pygame
# download further fonts from https://www.dafont.com/ and put them on the project directory
font = pygame.font.Font("freesansbold.ttf", 32)
# 55. Create text position
textX = 10
textY = 10
# 56 Create a function to put score_value inside game screen
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
# The 3rd argument of render is True to display score on the screem

# 63. Set game over text font
over_font = pygame.font.Font("freesansbold.ttf", 64)
# 64. Create game over function
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
# 44. Set initial bullet score.
#score = 0

# 15. Create a function to put player image in the screen.
def player(x, y):
    screen.blit(playerImg, (x, y))
    
# 51. Get back to enemy function and set it for multiple enemies.
# 24. Create a function to put enemy image in the screen.
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
# 36. Create a function to put bullet image in the screen.
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
class SpaceInvader(pygame.sprite.Sprite):
    # ... (تعریف کلاس SpaceInvader)

    def shoot(self):
        bullet = pygame.sprite.Sprite()
        bullet.image = pygame.Surface((5, 10))
        bullet.image.fill((255, 0, 0))
        bullet.rect = bullet.image.get_rect()
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.top
        all_sprites.add(bullet)
        bullets.add(bullet)
    
invaders = []
# 41.Define a function to set collision (distance function)
def isCollision(x1, x2, y1, y2):
    distance = np.sqrt(np.power(x1 - x2, 2) + np.power(y1 - y2, 2))
    if distance < 27:
        return True
    else:
        return False
# 5. Game loop
# (The game is running always and the window doesn't close down)
running = True
while running:
    # 11. RGB = Red, Green, Blue (fill the screen)
    # https://www.w3schools.com/colors/colors_converter.asp
    # https://www.rapidtables.com/convert/color/hex-to-rgb.html
    screen.fill((128, 0, 128))
    # 33. Background image
    screen.blit(background, (0, 0))
    # 17. movement mechanics in game development
    #playerX += 0.8
    #playerX += -0.1
    #playerY += 0.01

    # 6. event is anything that can happen inside the screen such as moving the mouse(event.get())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 7. Run (It's OK)

        #18. keyboard input controls and key pressed events
        # if keystroke is pressed, check weather it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # 20. set the speed of the player to the left
                playerX_change = -3
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                # 20. set the speed of the player to the right
                playerX_change = 3
                print("Right arrow is pressed")    
            # 37. Call fire bullet
            if event.key == pygame.K_SPACE:
                for i in invaders:
                    i.shoot()

                # 40. Let spaceship firing after the last bullet gets out of screen
                if bullet_state is "ready":
                   # 60. Set bullet sound
                   bullet_sound = mixer.Sound("laser.wav")
                   bullet_sound.play()
                   # 39. Get the current x coordinate of the player for bulletX
                   bulletX = playerX
                   fire_bullet(bulletX, bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
       


    # 21. Movement mechanics of the player
    playerX += playerX_change

    # 22. Checking for boundaries of spaceship, so it doesn't go out of screen.
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # 49. Copy collision from part 42 and paste it inside this for-loop
    # 28. Movement mechanics of the enemy
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
    # 48. Change enemy movement based on multiple enemies(Change 29 to multiple enemies)
        # 62. Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
               enemyY[j] = 2000    
            game_over_text()
            break
    # 29. Checking for boundaries of enemy, so it doesn't go out of screen.
    
        if enemyX[i] < 0:
            enemyX_change[i] = 3
        # 31. Increment enemyY by its speed
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i] = -3
        # 31. Increment enemyY by its speed
            enemyY[i] += enemyY_change[i]
        collision = isCollision(bulletX, enemyX[i], bulletY, enemyY[i])
    # 43. Set bullet and bullet state after collision is occurred
        if collision:
            # 61. Set collision sound
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()

            bulletY = 480
            bullet_state = "ready"
        # 45. Print score and reset the enemy.
            '''score += 1
            print(score)'''
            enemyX[i] = np.random.randint(0, 736)
            enemyY[i] = np.random.randint(50, 150)
            
            # 53 change score name in collisions
            score_value += 1
        # 50. Copy function call for enemy and set it for multiple enemies.
        enemy(enemyX[i], enemyY[i], i)
    # 38-2. Set bullet state in the boundaries
    if bulletY < 0:
       bulletY = 480
       bullet_state = "ready"

    #38-1. Fire bullet (run)
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        
    # 42. Call collision
    '''collision = isCollision(bulletX, enemyX, bulletY, enemyY)
    # 43. Set bullet and bullet state after collision is occurred
    if collision:
        bulletY = 480
        bullet_state = "ready"
        # 45. Print score and reset the enemy.
        score += 1
        print(score)
        enemyX = np.random.randint(0, 736)
        enemyY = np.random.randint(50, 150)'''
        
    # 25. Call enemy after filing the screen color otherwise it doesn't work
    #enemy(enemyX, enemyY)
    # 16. Call player after filing the screen color otherwise it doesn't work
    player(playerX, playerY)
    # 57. Call show_score
    show_score(textX, textY)
    # 12. display must be updated
    pygame.display.update()
    pygame.time.Clock().tick(60)

  











