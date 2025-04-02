import pygame
import random
import key_mappings

class Context:

    def reset_ball(self,direction):
        angle = random.uniform(-0.2, 0.2)
        return [self.const_ball_speed * direction, self.const_ball_speed * angle]

    def __init__(self,screen,phase_handler):
        self.phase_handler=phase_handler
        self.width, self.height = 640, 576
        self.ball_size = 20
        self.paddle_width,self.paddle_height = 10, 80
        self.paddle_speed = 10
        self.opp_paddle_speed=3.5
        self.const_ball_speed= 14
        self.white = (0, 255, 0)
        self.dark_green = (0, 100, 0)
        self.goal_line_width = 2
        self.screen=screen
        self.event_list=[]

        '''
        # Sounds
        bounce_paddle = pygame.mixer.Sound("bounce_paddle.wav")
        bounce_opponent = pygame.mixer.Sound("bounce_opponent.wav")
        bounce_wall = pygame.mixer.Sound("bounce_wall.wav")
        score_player = pygame.mixer.Sound("score_player.wav")
        score_opponent = pygame.mixer.Sound("score_opponent.wav")
        '''

        self.player_paddle = pygame.Rect(20, self.height // 2 - self.paddle_height // 2, self.paddle_width, self.paddle_height)
        self.opponent_paddle = pygame.Rect(self.width - 30, self.height // 2 - self.paddle_height // 2, self.paddle_width, self.paddle_height)
        self.ball = pygame.Rect(self.width // 2 - self.ball_size // 2, self.height // 2 - self.ball_size // 2, self.ball_size, self.ball_size)


        self.ball_speed = self.reset_ball(1)

        self.running = True
        self.player_score = self.opponent_score = 0

        self.score_timer = 0
        self.ball_direction = 1

    def update(self, event_list):
        self.screen.fill(self.dark_green)

        pygame.draw.rect(self.screen, self.white, self.player_paddle)
        pygame.draw.rect(self.screen, self.white, self.opponent_paddle)
        pygame.draw.ellipse(self.screen, self.white, self.ball)

        self.event_list[:]=event_list
        for event in self.event_list:
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[key_mappings.up_key] and self.player_paddle.top > 0:
            self.player_paddle.y -= self.paddle_speed
        if keys[key_mappings.down_key] and self.player_paddle.bottom < self.height:
            self.player_paddle.y += self.paddle_speed
        if keys[key_mappings.cancel_key]:
            self.phase_handler.set_game_phase("overworld")

        if self.opponent_paddle.centery < self.ball.centery:
            self.opponent_paddle.y += self.opp_paddle_speed
        if self.opponent_paddle.centery > self.ball.centery:
            self.opponent_paddle.y -= self.opp_paddle_speed

        if self.opponent_paddle.top < 0:
            self.opponent_paddle.top = 0
        if self.opponent_paddle.bottom > self.height:
            self.opponent_paddle.bottom = self.height


        self.ball.x += self.ball_speed[0]
        self.ball.y += self.ball_speed[1]

        if self.ball.top <= 0 or self.ball.bottom >= self.height:
            if self.ball.top <= 0:
                self.ball.top = 0
            if self.ball.bottom >= self.height:
                self.ball.bottom = self.height
            self.ball_speed[1] *= -1
            #bounce_wall.play()

        if self.ball.colliderect(self.player_paddle) and self.ball_speed[0] < 0:
            offset = (self.ball.centery - self.player_paddle.centery) / (self.paddle_height)
            if 0>offset>-0.3:
                offset=-0.3
            if 0.3>offset>0:
                offset=0.3
            self.ball_speed = [self.const_ball_speed * (1 - abs(offset)), self.const_ball_speed * offset]
            #bounce_paddle.play()

        if self.ball.colliderect(self.opponent_paddle) and self.ball_speed[0] > 0:
            offset = (self.ball.centery - self.opponent_paddle.centery) / (self.paddle_height)
            self.ball_speed = [-self.const_ball_speed * (1 - abs(offset)), self.const_ball_speed * offset]
            #bounce_opponent.play()

        if self.ball.left <= 0:
            self.opponent_score += 1
            self.score_timer = pygame.time.get_ticks()
            self.ball_speed = [0, 0]
            self.ball.x, self.ball.y = self.width // 2 - self.ball_size // 2, self.height // 2 - self.ball_size // 2
            self.ball_direction = -1

        if self.ball.right >= self.width:
            self.player_score += 1
            self.score_timer = pygame.time.get_ticks()
            self.ball_speed = [0, 0]
            self.ball.x, self.ball.y = self.width // 2 - self.ball_size // 2, self.height // 2 - self.ball_size // 2
            self.ball_direction = 1

        if self.score_timer and pygame.time.get_ticks() - self.score_timer > 500:
            self.ball_speed = self.reset_ball(self.ball_direction)
            self.score_timer = 0

