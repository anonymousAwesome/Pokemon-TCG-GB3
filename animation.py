import os
import pygame

'''
The animation module was created late in overworld development, so it
doesn't handle player and NPC animations.
'''

class AnimationManager:
    def __init__(self):
        self.active_animations = []
    
    def add_animation(self, animation):
        self.active_animations.append(animation)
    
    def update(self):
        for animation in self.active_animations[:]:
            animation.update()
            if animation.is_complete:
                self.active_animations.remove(animation)
    
    def draw(self):
        for animation in self.active_animations:
            animation.draw()

    def cancel_all_animations(self):
        self.active_animations=[]


class RudimentarySprite:
    def __init__(self,inner_context):
        image_location=os.path.join("assets","medals","Psychic_icon_SwSh.png")
        image=pygame.image.load(image_location).convert_alpha()
        self.image=image
        self.is_complete=False
        self.inner_context=inner_context
        self.x=0
        self.y=0
        self.lifetime=60
    
    def update(self):
        self.x+=1
        self.y+=1
        self.lifetime-=1
        if not self.lifetime:
            self.is_complete=True

    def check_is_done(self):
        return self.is_complete
        
    def draw(self):
        self.inner_context.screen.blit(self.image, (self.x,self.y))

'''
Below this point is all Deepseek code. I'm only keeping it for reference;
it will almost certainly deleted once the animations are all in place.
'''

class SpriteAnimation:
    def __init__(self, sprite, frames, duration, loop=False):
        self.sprite = sprite
        self.frames = frames  # List of surfaces/images
        self.duration = duration
        self.loop = loop
        self.current_time = 0
        self.current_frame = 0
    
    def update(self, dt):
        self.current_time += dt
        progress = min(self.current_time / self.duration, 1.0)
        
        if self.loop:
            progress = progress % 1.0
        
        self.current_frame = int(progress * (len(self.frames) - 1))
        
        # Update sprite image
        self.sprite.image = self.frames[self.current_frame]
    
    def is_complete(self):
        return not self.loop and self.current_time >= self.duration
    
    def draw(self, screen):
        # Sprite handles its own drawing
        pass
        
class ScreenFadeAnimation:
    def __init__(self, duration, start_alpha, end_alpha, color=(0, 0, 0)):
        self.duration = duration
        self.start_alpha = start_alpha
        self.end_alpha = end_alpha
        self.color = color
        self.current_time = 0
        self.overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def update(self, dt):
        self.current_time += dt
        progress = min(self.current_time / self.duration, 1.0)
        alpha = self.start_alpha + (self.end_alpha - self.start_alpha) * progress
        self.overlay.set_alpha(alpha)
    
    def is_complete(self):
        return self.current_time >= self.duration
    
    def draw(self, screen):
        screen.blit(self.overlay, (0, 0))

class CameraAnimation:
    def __init__(self, camera, start_pos, end_pos, duration, easing_func=None):
        self.camera = camera
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.duration = duration
        self.easing_func = easing_func or (lambda x: x)  # Linear by default
        self.current_time = 0
    
    def update(self, dt):
        self.current_time += dt
        progress = min(self.current_time / self.duration, 1.0)
        eased_progress = self.easing_func(progress)
        
        x = self.start_pos[0] + (self.end_pos[0] - self.start_pos[0]) * eased_progress
        y = self.start_pos[1] + (self.end_pos[1] - self.start_pos[1]) * eased_progress
        
        self.camera.set_position((x, y))
    
    def is_complete(self):
        return self.current_time >= self.duration
    
    def draw(self, screen):
        pass

