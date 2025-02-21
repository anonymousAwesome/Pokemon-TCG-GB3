import pygame
import random

pygame.init()

clock = pygame.time.Clock()

WIDTH, HEIGHT = 640, 576
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
PADDLE_SPEED = 10
OPP_PADDLE_SPEED=PADDLE_SPEED/2
BALL_SPEED = 14
WHITE = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
GOAL_LINE_WIDTH = 2

'''
# Sounds
bounce_paddle = pygame.mixer.Sound("bounce_paddle.wav")
bounce_opponent = pygame.mixer.Sound("bounce_opponent.wav")
bounce_wall = pygame.mixer.Sound("bounce_wall.wav")
score_player = pygame.mixer.Sound("score_player.wav")
score_opponent = pygame.mixer.Sound("score_opponent.wav")
'''

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

player_paddle = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

def reset_ball(direction):
    angle = random.uniform(-0.2, 0.2)
    return [BALL_SPEED * direction, BALL_SPEED * angle]

ball_speed = reset_ball(1)

running = True
player_score = opponent_score = 0

score_timer = 0
ball_direction = 1

while running:
    screen.fill(DARK_GREEN)

    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED


    if opponent_paddle.centery < ball.centery:
        opponent_paddle.y += OPP_PADDLE_SPEED
    if opponent_paddle.centery > ball.centery:
        opponent_paddle.y -= OPP_PADDLE_SPEED

    if opponent_paddle.top < 0:
        opponent_paddle.top = 0
    if opponent_paddle.bottom > HEIGHT:
        opponent_paddle.bottom = HEIGHT


    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        if ball.top <= 0:
            ball.top = 0
        if ball.bottom >= HEIGHT:
            ball.bottom = HEIGHT
        ball_speed[1] *= -1
        #bounce_wall.play()

    if ball.colliderect(player_paddle) and ball_speed[0] < 0:
        offset = (ball.centery - player_paddle.centery) / (PADDLE_HEIGHT)
        ball_speed = [BALL_SPEED * (1 - abs(offset)), BALL_SPEED * offset]
        #bounce_paddle.play()

    if ball.colliderect(opponent_paddle) and ball_speed[0] > 0:
        offset = (ball.centery - opponent_paddle.centery) / (PADDLE_HEIGHT)
        ball_speed = [-BALL_SPEED * (1 - abs(offset)), BALL_SPEED * offset]
        #bounce_opponent.play()

    if ball.left <= 0:
        opponent_score += 1
        score_timer = pygame.time.get_ticks()
        ball_speed = [0, 0]
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_direction = -1

    if ball.right >= WIDTH:
        player_score += 1
        score_timer = pygame.time.get_ticks()
        ball_speed = [0, 0]
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_direction = 1

    if score_timer and pygame.time.get_ticks() - score_timer > 500:
        ball_speed = reset_ball(ball_direction)
        score_timer = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
