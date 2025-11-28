#Create your own shooter

from pygame import *
from random import randint
speed = 10
lost = 0
score = 0
font.init()
style = font.Font(None, 36)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed =  player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += speed
    def fire(self):
        bullet = Bullet("Capture.PNG",self.rect.centerx,self.rect.top,5,10,10)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if(self.rect.y >= 700):
            lost += 1 
            self.rect.y = 0
            self.rect.x = randint(0,500)
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
rocket = Player("Flamethrower.webp",100,500,1,100,70)
enemies = sprite.Group()
bullets = sprite.Group()
for i in range(0,6):
    enemy = Enemy("StriderSkibidi.webp",randint(0,500),0,randint(1,3),70,70)
    enemies.add(enemy)
window = display.set_mode((500, 700))
display.set_caption("shooter")
background = transform.scale(image.load("hahha.PNG"), (500, 700))


#parameters of the image sprite
run = True
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    while not finish:
        for e in event.get():
            if e.type == QUIT:
                run = False
                finish = True
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    rocket.fire()

        window.blit(background,(0, 0))
        rocket.reset()
        rocket.update()
        enemies.draw(window)
        enemies.update()
        bullets.draw(window)
        bullets.update()
        collides = sprite.groupcollide(enemies,bullets,True,False)
        for collide in collides:
            score += 1
            enemy = Enemy("StriderSkibidi.webp",randint(0,500),0,randint(1,3),70,70)
            enemies.add(enemy)

        text_lose = style.render(
            "Missed:" + str(lost), 1,(255,255,255)
        )
        window.blit(text_lose,(10,20))
        text_score = style.render(
            "score:" + str(score), 1,(255,255,255)
        )
        window.blit(text_score,(10,40))
        if sprite.spritecollide(rocket,enemies,False) or lost >= 10:
            finish = True
            text_fail = style.render(
            "You lose hahaha >:)", 1,(255,0,0)
        )
            window.blit(text_fail,(300,300))
        if score >= 100:
            finish = True
            text_win = style.render(
            "You win but you is noob because it's easy >:(" , 1,(0,0,255)
        )
            window.blit(text_win,(300,300))

        display.update()
        clock.tick(FPS)
    display.update()
    clock.tick(FPS)

