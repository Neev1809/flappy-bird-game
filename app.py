import pygame
import random
pygame.init()
screen_width = 400
screen_height = 600
blue = (135, 206, 235)
yellow = (255, 222, 33)
black = (0, 0, 0)
green = (0, 191, 0)
white = (255, 255, 255)
font = pygame.font.SysFont(None, 30)
fps = 60
GameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
def screen_text(text, colour, x, y):
    text_screen = font.render(text, True, colour)
    GameWindow.blit(text_screen, [x, y])
def home_screen():
    home = True
    while home:
        GameWindow.fill(blue)
        screen_text("FLAPPY BIRD", black, 120, 200)
        screen_text("Press SPACE to Start", black, 105, 250)
        screen_text("Press Q to Quit", black, 120, 280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    home = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        pygame.display.update()
        clock.tick(fps)
def gameloop():
    game_over = False
    game_exit = False
    bird_size = 20
    bird_x = (screen_width // 2 // bird_size) * bird_size
    bird_y = (screen_height // 2 // bird_size) * bird_size
    bird_rect = pygame.Rect(bird_x, bird_y, bird_size, bird_size)
    pipe_x = 350
    pipe_y = random.randint(100, 400)
    pipe_top_rect = pygame.Rect(pipe_x, 0, 30, pipe_y)
    pipe_bottom_rect = pygame.Rect(pipe_x, pipe_y + 90, 30, screen_height - (pipe_y + 90))
    velocity_x = 0
    velocity_y = 0
    pipe_velocity = -2
    jump = -8
    gravity = 0.5
    score = 0
    while not game_exit:
        if game_over:
            GameWindow.fill(blue)
            screen_text("Game Over! Press Enter to continue", black, 25, 282)
            screen_text("Score: " + str(score*10), black, 160, 320)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        velocity_y = jump
            if bird_y <= 0 or bird_y >= screen_height:
                game_over = True
            if pipe_x < -30:
                pipe_x = 400
                pipe_y = random.randint(100, 400)
                pipe_top_rect.height = pipe_y
                pipe_bottom_rect.y = pipe_y + 90
                pipe_bottom_rect.height = screen_height - (pipe_y + 90)
                score += 1
            if bird_rect.colliderect(pipe_top_rect) or bird_rect.colliderect(pipe_bottom_rect):
                game_over = True
            pipe_x += pipe_velocity
            bird_x += velocity_x
            velocity_y += gravity
            bird_y += velocity_y
            bird_rect.x = bird_x
            bird_rect.y = bird_y
            pipe_top_rect.x = pipe_x
            pipe_bottom_rect.x = pipe_x
            GameWindow.fill(blue)
            screen_text("Score: " + str(score*10), white, 160, 5)
            pygame.draw.rect(GameWindow, yellow, bird_rect)
            pygame.draw.rect(GameWindow, green, pipe_top_rect)
            pygame.draw.rect(GameWindow, green, pipe_bottom_rect)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
while True:
    home_screen()
    gameloop()
