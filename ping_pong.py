from pygame import *
# from random import randint
# from time import time as timer
window = display.set_mode((700, 500))
display.set_caption("Пинг понг")
window.fill((255,255,255))
# background = transform.scale(image.load("galaxy.jpg"), (700, 500))

speed_x = 3
speed_y = 3
# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire_sound = mixer.Sound('fire.ogg')
# #wingame = mixer.Sound('')
# #kick = mixer.Sound('')
class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y, player_speed,size_x, size_y):
          super().__init__()
          self.image = transform.scale(image.load(player_image), (size_x, size_y))
          self.speed = player_speed
          self.rect = self.image.get_rect()
          self.rect.x = player_x
          self.rect.y = player_y
     def reset(self):
          window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
     def update(self):
          keys_pressed = key.get_pressed()
          if keys_pressed[K_UP] and self.rect.y > 5:
               self.rect.y -= self.speed
          if keys_pressed[K_DOWN] and self.rect.y < 635 :
               self.rect.y += self.speed
     # def fire(self):
     #      bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, 15) 
     #      bullets.add(bullet) 
# lost = 0
# class Enemy(GameSprite):
#     direction = "left"
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.x = randint(50,700)
#             self.rect.y = 0
#             lost = lost + 1
# class Asteroid(GameSprite):
#     direction = "left"
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y > 500:
#             self.rect.x = randint(50,700)
#             self.rect.y = 0
# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y -= self.speed
#         if self.rect.y < 0:
#             self.kill()

            
# bullets = sprite.Group()       
# monsters = sprite.Group()
# asteroids = sprite.Group()


# for i in range(6):
#     monster = Enemy('ufo.png',randint(50,450),-40,randint(1,5),100,70)
#     monsters.add(monster)
# for i in range(3):
#     asteroid = Asteroid('asteroid.png',randint(50,450),-40,randint(1,5),100,100 )
#     asteroids.add(asteroid)

# font.init()
# font1 = font.SysFont('Arial', 24)
# win = font1.render("YOU WIN", 1,(255,255,255))
# lose = font1.render("YOU LOSE", 1,(255,255,255))
# sprites_list = sprite.groupcollide( 
# monsters, bullets, True, True 
# )
win_height = 500
clock = time.Clock()
FPS = 60
player = Player('platform.png', 5, 370, 10, 130, 130)
ball = GameSprite('ball.png', 5, 370, 10, 100, 100)
# score = 0
    
finish = False
game = True
# max_lost = 5
# life = 3
# life_color = (255,255,255)
# num_fire = 0 
# rel_time = False 
while game:
  
     for e in event.get():
          if e.type == QUIT:
               game = False
#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 fire_sound.play()
#                 player.fire()
#                 rel_time = False 
#         elif e.type == KEYDOWN: 
#             if e.key == K_SPACE: 
#                     if num_fire < 5 and rel_time == False: 
#                         num_fire = num_fire + 1 
#                         fire_sound.play() 
#                         player.fire() 
#                     if num_fire >= 5 and rel_time == False: 
#                         last_time = timer() 
#                         rel_time = True 
     if finish != True:
          window.fill((255,255,255))
          ball.rect.x += speed_x
          ball.rect.y += speed_y
          if ball.rect.y > win_height-50 or ball.rect.y < 0:
               speed_y *= -1
#         text = font1.render("Счёт: " + str(score), 1, (255,255,255))
#         text_lose = font1.render("Пропущено:" + str(lost), 1,(255,255,255))
        
#         window.blit(background,(0, 0))
#         window.blit(text_lose,(10,50))
          #window.blit(ball)
#         monsters.draw(window)   
#         bullets.draw(window) 
#         asteroids.draw(window)  
          #ball.draw(window)  

#         bullets.update()     
#         monsters.update()
#         asteroids.update()
          player.update()
          ball.update()
 
          ball.reset()
          player.reset()

#         if rel_time == True: 
#             now_time = timer() 

#             if now_time - last_time < 3: 
#                 reload = font1.render('Wait, reload...', 1, (150, 0, 0)) 
#                 window.blit(reload, (260, 460)) 
#             else: 
#                 num_fire = 0 
#                 rel_time = False 
        

#         collides = sprite.groupcollide(monsters, bullets, True, True)
#         for c in collides:
#             score = score + 1
#             monster = Enemy('ufo.png',randint(50,450),-40,randint(1,5),100,70)
#             monsters.add(monster)
            

#         if sprite.spritecollide(player, monsters, False) or lost >= 6:
#             finish = True
#             life -= 1
            
        
#         if score >= 101:
#             finish = True
#             window.blit(win, (200,200))

#         if life == 3: 
#             life_color = (0, 150, 0) 
#         if life == 2: 
#             life_color = (150, 150, 0) 
#         if life == 1: 
#             life_color = (150, 0, 0) 
#             window.blit(lose, (200,200)) 
            
#         text_life = font1.render(str (life), 1, life_color) 
#         window.blit(text_life, (650, 10)) 
#     else:
#         finish = False 
#         score = 0 
#         lost = 0 
        
#         for b in bullets: 
#             b.kill() 
#         for m in monsters: 
#             m.kill() 
#         for a in asteroids: 
#             a.kill() 
#         time.delay (1000) 
#         for i in range(1, 6): 
#             monster = Enemy('ufo.png',randint(50,450),-40,randint(1,5),100,70)
#             monsters.add(monster) 
#         for i in range(3):
#             asteroid = Asteroid('asteroid.png',randint(50,450),-40,randint(1,5),100,100)
#             asteroids.add(asteroid)
        
     display.update()

     clock.tick(FPS)