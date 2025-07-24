import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.e_type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity= [0,0]
        
    def update(self,tilemap, movement=(0,0)):
      frame_movement = (movement[0]+ self.velocity[0], movement[1] + self.velocity[1])
      
      
      self.pos[0] += frame_movement[0]
      self.pos[1] += frame_movement[1]
      self.velocity[1]+=min(5, self.velocity[1]+0.1)
      entity_rect=self.rect()
      for rect in tilemap.physics_rects_arount(self.pos):
          if entity_rect.colliderect(rect):
              if frame_movement[1] > 0:
                  self.pos[1] = rect.top - self.size[1]
                  self.velocity[1] = 0
      
      
    def render(self, surf):
        surf.blit(self.game.assets['player'],self.pos)
    
    
    def rect(self):
      return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])