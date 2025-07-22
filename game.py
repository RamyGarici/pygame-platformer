import pygame
import sys
from entities import PhysicsEntity
from tilemap import Tilemap
from utils import load_image,load_images


class Game:

    def __init__(self):
        

        pygame.init()
        pygame.display.set_caption("Platformer Game")

        self.screen = pygame.display.set_mode((640,480))
        self.display= pygame.Surface((320,240))
        self.clock=pygame.time.Clock()
        self.assets={
            'player': load_image('entities/player.png'),
            'grass': load_images('tiles/grass'),
            'stone': load_images('tiles/stone'),
            'large_decor': load_images('tiles/large_decor'),
            'decor': load_images('tiles/decor')
        
            
        }
       
    
        # self.img_pos=[160,260]
        self.movement=[False,False]
        # self.collision_area=pygame.Rect(50,50,300,50)
        self.player= PhysicsEntity(self, 'player', (50, 50), (50, 50))
        self.tilemap = Tilemap(self)
    
    def run(self):
        while True:
            self.display.fill((14,219,248))
            self.tilemap.render(self.display)
            
            self.player.update((self.movement[1]-self.movement[0],0))
            self.player.render(self.display)
            self.tilemap.render(self.display)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                        
            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()))
            pygame.display.update()
            self.clock.tick(60)
            
            
            
Game().run()