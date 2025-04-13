from pygame import *
from time import sleep
class GameSplite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,peremannai1, peremannai2,direction = None):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(peremannai1,peremannai2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'down'
    def reset(self):
        main_win.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSplite):
    def update(self):
        global a
        global b
        global v
        if len(sprite_list2) >=1:
            b = -5
        if len(sprite_list1) >= 1:
            b = 5
        if self.rect.x < 0:
            a = 5
        if self.rect.x > 720:
            a = -5
        if self.rect.y < 0:
            v = -2
        if self.rect.y > 520:
            v = -1
        self.rect.x +=a
        self.rect.y +=b
class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height,speed):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wight = wall_width
        self.height = wall_height
        self.image = Surface((self.wight,self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.speed = speed
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -=self.speed
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x +=self.speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -=self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 650:
            self.rect.x +=self.speed
    def draw_wall(self):
        main_win.blit(self.image,(self.rect.x,self.rect.y))
hero1 = Player('1.png', 350,419,10,80,80)
win_wight = 800
win_hight = 600
main_win = display.set_mode((win_wight, win_hight))
display.set_caption('pygame window')
background = transform.scale(image.load('galaxy.jpg'),(800,600))
clock = time.Clock()
game = True
finish = False
FPS = 60
monster = sprite.Group()
Ctena = sprite.Group()
font.init()
font1 = font.SysFont('Arial',40)
win = font1.render('Победил 1 игрок', True,(255,0,0))
lose = font1.render('Победил 2 игрок', True,(0,255,0))
a = 5
b = 5
c = 100
v = 0
f = 0
k = 0
l = 0
ctena = Wall(255,255,255,350,500,150,20,7)
ctena1 = Wall(255,255,255,350,100,150,20,7)
Ctena.add(ctena)
monster.add(ctena1)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        sprite_list1 = sprite.spritecollide(hero1,monster,False)
        sprite_list2 = sprite.spritecollide(hero1,Ctena,False)
        main_win.blit(background,(0,0))
        chet = font1.render('Счет'+str(k)+':'+str(l), False,(255,255,255))
        main_win.blit(chet,(50,100))
        hero1.update()
        hero1.reset()
        ctena.update()
        ctena1.update1()
        Ctena.draw(main_win)
        monster.draw(main_win)
        if v == -1:
            main_win.blit(win,(300,300))
            finish = True
            l+=1
            
        if v == -2:
            main_win.blit(lose,(300,300))
            finish = True
            k+=1
    else:
        sleep(2)
        v = 0
        f = 0
        a = 5
        b = 5
        c = 100
        finish = False
        hero1 = Player('1.png', 350,420,10,80,80)
        for i in monster:
            i.kill()
        for i in Ctena:
            i.kill()
        ctena1 = Wall(255,255,255,350,100,150,20,7)
        monster.add(ctena1)
        ctena = Wall(255,255,255,350,500,150,20,7)
        Ctena.add(ctena)
    display.update()
    clock.tick(FPS)