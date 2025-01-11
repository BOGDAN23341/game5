
import pygame
pygame.init()

import random

class Player():  # клас для створення шаблону персонажа
    def __init__(self, x, y, width, height, image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect()  # "межі" персонажа
        self.rect.x = x  # координати по ширині
        self.rect.y = y  # координати по висоті
        self.width = width  # ширина
        self.height = height  # висота

    def move(self):
        keys = pygame.key.get_pressed()  # зберігаємо всі можливі натиснуті клавіші в список keys
        if keys[pygame.K_a]:  # якщо натиснута клавіша "стрілка ліворуч"
            self.rect.x -= 5  # змінюємо координати гравця по x на -2
        if keys[pygame.K_d]:  # якщо натиснута клавіша "стрілка праворуч"
            self.rect.x += 5  # змінюємо координати гравця по x на +2
        if keys[pygame.K_w]:  # якщо натиснута клавіша "стрілка вверх"
            self.rect.y -= 5  # змінюємо координати гравця по y на -2
        if keys[pygame.K_s]:  # якщо натиснута клавіша "стрілка вниз"
            self.rect.y += 5  # змінюємо координати гравця по y на +2

# створення головного вікна
window = pygame.display.set_mode((500, 500))

# Завантаження зображення фону 
background_image = pygame.image.load('background.png') 
background_image = pygame.transform.scale(background_image, (500, 500))

# створення персонажа
player = Player(100, 100, 50, 50, 'helper.png')
portal = Player(2500, 2500, 100,100,'portal.png')
moneta = Player(1000,1000,30,30,"moneta.png")   
moneta2 = Player(1000,1000,30,30,"moneta.png")   
moneta3 = Player(1000,1000,30,30,"moneta.png")   
moneta4 = Player(1000,1000,30,30,"moneta.png")   
moneta5 = Player(1000,1000,30,30,"moneta.png")   
moneta6 = Player(1000,1000,30,30,"moneta.png")   
moneta7 = Player(1000,1000,30,30,"moneta.png")   
moneta8 = Player(1000,1000,30,30,"moneta.png")   

boss = Player(1000,1000, 100,30,"boss.png")      
bullets = []       
bullets_color = (255,0,0)
# Створення ялинок
# Ялинки для лівої частини (trees_left)
# Ялинки для центральної частини (trees_center)
trees_center = [
    Player(30, 50, 100, 100, 'tree.png'),
    Player(120, 100, 100, 100, 'tree.png'),
    Player(200, 150, 100, 100, 'tree.png'),
    Player(250, 200, 100, 100, 'tree.png'),
    Player(80, 250, 100, 100, 'tree.png'),
    Player(180, 300, 100, 100, 'tree.png'),
    Player(300, 70, 100, 100, 'tree.png'),
    Player(350, 150, 100, 100, 'tree.png'),
    Player(400, 180, 100, 100, 'tree.png'),  # нова ялинка
    Player(450, 220, 100, 100, 'tree.png'),  # нова ялинка
    Player(500, 260, 100, 100, 'tree.png'),  # нова ялинка
    Player(100, 320, 100, 100, 'tree.png'),  # нова ялинка
    Player(230, 270, 100, 100, 'tree.png'),  # нова ялинка
    Player(350, 300, 100, 100, 'tree.png'),  # нова ялинка
    Player(450, 100, 100, 100, 'tree.png')   # нова ялинка
]



# Ялинки для центральної частини (trees_center)
# Ялинки для центральної частини (trees_center) - розміщення ялинок, щоб створити вигляд лісу

    


# Ялинки для лівої частини (trees_left)
trees_left = [
    Player(50, 50, 100, 100, 'tree.png'),
    Player(150, 120, 100, 100, 'tree.png'),
    Player(200, 180, 100, 100, 'tree.png'),
    Player(100, 250, 100, 100, 'tree.png'),
    Player(300, 320, 100, 100, 'tree.png'),
    Player(400, 350, 100, 100, 'tree.png'),
    Player(450, 180, 100, 100, 'tree.png'),
    Player(500, 270, 100, 100, 'tree.png'),
    Player(350, 400, 100, 100, 'tree.png'),
    Player(450, 320, 100, 100, 'tree.png')
]

# Ялинки для правої частини (trees_right)
trees_right = [
    Player(350, 50, 100, 100, 'tree.png'),
    Player(400, 100, 100, 100, 'tree.png'),
    Player(450, 150, 100, 100, 'tree.png'),
    Player(500, 200, 100, 100, 'tree.png'),
    Player(300, 250, 100, 100, 'tree.png'),
    Player(550, 100, 100, 100, 'tree.png'),
    Player(600, 180, 100, 100, 'tree.png'),
    Player(650, 220, 100, 100, 'tree.png'),
    Player(450, 350, 100, 100, 'tree.png'),
    Player(500, 400, 100, 100, 'tree.png')
]

# Ялинки для верхньої частини (trees_up)
trees_up = [
    Player(100, 50, 100, 100, 'tree.png'),
    Player(200, 100, 100, 100, 'tree.png'),
    Player(250, 150, 100, 100, 'tree.png'),
    Player(150, 200, 100, 100, 'tree.png'),
    Player(300, 200, 100, 100, 'tree.png'),
    Player(350, 70, 100, 100, 'tree.png'),
    Player(400, 120, 100, 100, 'tree.png'),
    Player(450, 150, 100, 100, 'tree.png'),
    Player(500, 180, 100, 100, 'tree.png'),
    Player(550, 200, 100, 100, 'tree.png'),
    Player(50, 50, 100, 100, 'tree.png'),
    Player(150, 120, 100, 100, 'tree.png'),
    Player(250, 200, 100, 100, 'tree.png'),
    Player(350, 280, 100, 100, 'tree.png'),
    Player(450, 360, 100, 100, 'tree.png'),
]

# Ялинки для нижньої частини (trees_down)
trees_down = [
    Player(100, 400, 100, 100, 'tree.png'),
    Player(200, 420, 100, 100, 'tree.png'),
    Player(300, 440, 100, 100, 'tree.png'),
    Player(400, 420, 100, 100, 'tree.png'),
    Player(500, 440, 100, 100, 'tree.png'),
    Player(600, 400, 100, 100, 'tree.png'),
    Player(700, 420, 100, 100, 'tree.png'),
    Player(800, 440, 100, 100, 'tree.png'),
    Player(650, 460, 100, 100, 'tree.png'),
    Player(750, 460, 100, 100, 'tree.png'),
    
  
]


level = "center"

# кольори
white = (255, 255, 255)
black = (0, 0, 0)

# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()
count = 0
count2 = 0
moneta_collect = False
moneta2_collect = False
moneta3_collect = False
moneta4_collect = False

moneta5_collect = False
moneta6_collect = False
moneta7_collect = False
moneta8_collect = False
# головний цикл гри
game = True
while game:
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    # відображення фону
    window.blit(background_image, (0, 0))
    
        
    if player.rect.colliderect(moneta.rect):
        moneta_collect = True
        moneta.rect.x = 2000
        count += 1
    if player.rect.colliderect(moneta2.rect):
        moneta2_collect = True
        moneta2.rect.x = 2000
        count += 1
    if player.rect.colliderect(moneta3.rect):
        moneta3_collect = True
        moneta3.rect.x = 2000
        count += 1
    if player.rect.colliderect(moneta4.rect):
        moneta4_collect = True
        moneta4.rect.x = 2000
        count += 1
    window.blit(player.image, (player.rect.x, player.rect.y)) 
    # відображення рівнів
    if level == 'center':
        # відображення ялинок
        for tree in trees_center :
            window.blit(tree.image, (tree.rect.x, tree.rect.y))  
        if count >= 4:
            portal.rect.x, portal.rect.y = 250,250  
            window.blit(portal.image, (portal.rect.x, portal.rect.y))  
    if level == 'left':
        for tree in trees_left: 
            window.blit(tree.image, (tree.rect.x, tree.rect.y))
        window.blit(moneta4.image, (moneta4.rect.x, moneta4.rect.y))
    if level == 'right':
        for tree in trees_right:  
            window.blit(tree.image, (tree.rect.x, tree.rect.y))
        window.blit(moneta2.image, (moneta2.rect.x, moneta2.rect.y))
    if level == 'up':
        for tree in trees_up:   
            window.blit(tree.image, (tree.rect.x, tree.rect.y))
        window.blit(moneta.image, (moneta.rect.x, moneta.rect.y))
    if level == 'down':
        for tree in trees_down:   
            window.blit(tree.image, (tree.rect.x, tree.rect.y))   
        window.blit(moneta3.image, (moneta3.rect.x, moneta3.rect.y))   
    
    if level == 'final':
        # генерація пуль боса
        if len(bullets) < 40:
            if random.randint(0,100) < 10:
                x = 252
                y = 220
                bullets.append(pygame.Rect(x,y,20,20))  
        
        for d in bullets:
            if d == bullets[0]:
                d.x +=2
                d.y +=2
            elif d == bullets[1]:
                d.y +=2
            elif d == bullets[2]:
                d.y +=2
                d.x -=2
            elif d == bullets[3]:
                d.x -=2
            elif d == bullets[4]:
                d.x -=2
                d.y -=2
            elif d == bullets[5]:
                d.y -=2
            elif d == bullets[6]:
                d.x -=2
                d.y -=2
            elif d == bullets[7]:
                d.x +=2
                d.x +=2
            elif d == bullets[8]:
                d.x +=2
                d.y +=2
                d.y -=2
            elif d == bullets[9]:
                d.y +=2
                d.x -=2
                d.y +=2
                d.x +=2
                d.x -=2
            elif d == bullets[10]:
                d.y +=2
                d.y +=2
                d.y +=2
            elif d == bullets[11]:
                d.y +=2
            elif d == bullets[12]:
                d.y +=2
                d.x -=2
            elif d == bullets[13]:
                d.x -=2
            elif d == bullets[14]:
                d.x -=2
                d.y -=2
            elif d == bullets[15]:
                d.y -=2
            elif d == bullets[16]:
                d.x -=2
                d.y -=2
            elif d == bullets[17]:
                d.x +=2
                d.x +=2
            elif d == bullets[18]:
                d.x +=2
                d.y +=2
                d.y -=2
            elif d == bullets[19]:
                d.y +=2
                d.x -=2
                d.y +=2
                d.x +=2
                d.x -=2
            elif d == bullets[20]:
                d.y +=2
                d.y +=2
                d.y +=2
            
            if d.x > 700 or d.x < -700 or d.y > 700 or d.y < -700:
                d.x = 252
                d.y = 220

        window.blit(boss.image, (boss.rect.x, boss.rect.y))   
        #================================================================
        window.blit(moneta5.image, (moneta5.rect.x, moneta5.rect.y))
        window.blit(moneta6.image, (moneta6.rect.x, moneta6.rect.y))
        window.blit(moneta7.image, (moneta7.rect.x, moneta7.rect.y))
        window.blit(moneta8.image, (moneta8.rect.x, moneta8.rect.y))
        
        for d in bullets:
            if player.rect.colliderect(d):
                game = False
        

        for b in bullets:
            pygame.draw.rect(window,bullets_color,b)
            
        if player.rect.colliderect(moneta5.rect):
            moneta5_collect = True
            moneta5.rect.x = 2000
            count2 += 1
        if player.rect.colliderect(moneta6.rect):
            moneta6_collect = True
            moneta6.rect.x = 2000
            count2 += 1
        if player.rect.colliderect(moneta7.rect):
            moneta7_collect = True
            moneta7.rect.x = 2000
            count2 += 1
        if player.rect.colliderect(moneta8.rect):
            moneta8_collect = True
            moneta8.rect.x = 2000
            count2 += 1
        if count2 >= 4:
            game = False
             
            
               
    # Перехід між рівнями
    if level == 'center' and player.rect.x < -50:
        level = 'left'
        player.rect.x = 500
        if not moneta4_collect:
            moneta4.rect.x=100
            moneta4.rect.y=100
    if level == 'left' and player.rect.x > 500:
        level = 'center'
        player.rect.x = -50

    if level == 'center' and player.rect.x > 500:
        level = 'right'
        player.rect.x = -50
        if not moneta2_collect:
            moneta2.rect.x=100
            moneta2.rect.y=100
    if level == 'right' and player.rect.x < -50:
        level = 'center'
        player.rect.x = 500
    if level == 'center' and player.rect.y < -50:
        level = 'up'
        player.rect.y = 500
        if not moneta_collect:
            moneta.rect.x=100
            moneta.rect.y=100
    if level == 'up' and player.rect.y > 500:
        level = 'center'
        player.rect.y = -50
    if level == 'center' and player.rect.y > 500:
        level = 'down'
        player.rect.y = -50
        if not moneta3_collect:
            moneta3.rect.x=100
            moneta3.rect.y=100
    if level == 'down' and player.rect.y < -50:
        level = 'center'
        player.rect.y = 500
        
    # відображення персонажа
    if player.rect.colliderect(portal.rect):
        level = "final" 
        player.rect.x = 10 
        player.rect.x = 10 
        portal.rect.x = 1000
        portal.rect.y = 1000
        moneta5.rect.x = 100
        moneta5.rect.y = 100
        moneta6.rect.x = 350
        moneta6.rect.y = 350
        moneta7.rect.x = 200
        moneta7.rect.y = 200
        moneta8.rect.x = 310
        moneta8.rect.y = 310

    
    
    if player.rect.colliderect(moneta5.rect):
        moneta5.rect.x = 2000  # переміщаємо монету за межі екрану
        count += 1
    if player.rect.colliderect(moneta6.rect):
        moneta6.rect.x = 2000
        count += 1
    if player.rect.colliderect(moneta7.rect):
        moneta7.rect.x = 2000
        count += 1
    if player.rect.colliderect(moneta8.rect):
        moneta8.rect.x = 2000
        count += 1
    
    
    player.move()

    # задання частоти кадрів та оновлення екрану
    clock.tick(30)
    pygame.display.update()

pygame.quit() 