#Create your own shooter

from pygame import *

speed = 10
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
rocket = Player("rocket.png",100,500,1,100,70)

window = display.set_mode((500, 700))
display.set_caption("shooter")
background = transform.scale(image.load("galaxy.jpg"), (500, 700))


#parameters of the image sprite
run = True
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

finish = False

while run:
    while not finish:
        for e in event.get():
            if e.type == QUIT:
                run = False
                finish = Truem
        window.blit(background,(0, 0))
        rocket.reset()
        rocket.update()
        display.update()
        clock.tick(FPS)

