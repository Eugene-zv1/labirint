#hello
from pygame import *
mixer.init()
font.init()
font1 = font.SysFont('Arial',70)
win = font1.render('ТЫ выйграл',True,(255,100,0))
lose = font1.render('ТЫ проиграл',True,(0,100,230))
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
window = display.set_mode((700,500))
display.set_caption('Погоня')

background = transform.scale(image.load('background.jpg'),(700,500))
clock = time.Clock()
FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self,filename,w,h,speed,x,y):
            super().__init__()
            self.image = transform.scale(image.load(filename),(w,h))
            self.speed = speed
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
    def reset(self):
            window.blit(self.image, (self.rect.x , self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0 :
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 450 :
            self.rect.y += 10
        if keys_pressed[K_a] and self.rect.x > 0 :
            self.rect.x -= 10
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += 10   
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        speed = 2
        if self.rect.x <= 140:
            self.direction = 'right'
        if self.rect.x >= 700-85:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class  Wall(sprite.Sprite):
    def __init__(self,w,h,color,x,y):
        super().__init__()
        self.image = Surface((w,h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image ,( self.rect.x , self.rect.y))
wall1 = Wall(650,20,(0,20,250),100,300)
wall2 = Wall(450,20,(0,20,250),0,160)
wall3 = Wall(20,30,(0,20,250),300,160)
wall4 = Wall(20,50,(0,20,250),390,260)
wall5 = Wall(150,20,(0,20,250),620,160)
wall6 = Wall(20,30,(0,20,250),130,160)
wall7 = Wall(20,50,(0,20,250),215,260)

walls = sprite.Group()
walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7)

player = Player('hero.png',65,65,10,50,400)
cyborg = Enemy('cyborg.png',65,65,10,500,400)
treasure = GameSprite('treasure.png',65,65,10,500,100)
finish = False
while game:
    if finish != True:
        window.blit(background,(0,0))
        if sprite.collide_rect(cyborg,player):
            window.blit(lose,(200,200))
            finish = True
            kick.play()
            
        if sprite.collide_rect(player,treasure):
            window.blit(win,(200,200))
            finish = True
            money.play()
        if len(sprite.spritecollide(player,walls,False))> 0 :
            player.rect.x = 50
            player.rect.y = 400
        
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        player.reset()
        player.update()
        cyborg.reset()
        cyborg.update()
        treasure.reset()
    for e in event.get():
            if e.type == QUIT:
                    game = False
    display.update()
    clock.tick(FPS)
        
