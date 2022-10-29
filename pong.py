#prototype and unoptimized code, will implement more accurate physics system with acceleration and seperate files for graphics and functions

import pygame, sys, random

# constants
WIDTH = 1280
HEIGHT = 800
SCREEN_AREA = pygame.Rect(0, 0, WIDTH, HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
numbers = [1, -1]

# initialisation
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280,800))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
font = pygame.font.Font('Pixeltype.ttf', 70)
font2 = pygame.font.Font('Pixeltype.ttf', 30)
paddleSound = pygame.mixer.Sound('paddle.mp3')
wallSound = pygame.mixer.Sound('wall.mp3')
scoreSound = pygame.mixer.Sound('score.mp3')
pygame.mixer.music.set_volume(0.3)

# variables and bools
right_paddle_x_pos = 1200
right_paddle_y_pos = 350
left_paddle_x_pos = 50
left_paddle_y_pos = 350
right_paddle = pygame.Rect(right_paddle_x_pos, right_paddle_y_pos, 10, 50)
left_paddle = pygame.Rect(left_paddle_x_pos , left_paddle_y_pos, 10, 50)
ball_x_pos = 630
ball_y_pos = 350
ball = pygame.Rect(ball_x_pos, ball_y_pos, 15, 15)
right_paddle_movement_y = 0
left_paddle_movement_y = 0
ball_direction_x = random.choice(numbers)
ball_direction_y = random.choice(numbers)
ball_direction = (ball_direction_x, ball_direction_y)
done = True
right_score_value = 0
left_score_value = 0
tutorialDone = False

#graphics
right_player_score_surface_0 = font.render('0', True, 'White')
right_player_score_rectangle_0 = right_player_score_surface_0.get_rect(center = (850,50))
left_player_score_surface_0 = font.render('0', True, 'White')
left_player_score_rectangle_0 = left_player_score_surface_0.get_rect(center = (400,50))

right_player_score_surface_1 = font.render('1', True, 'White')
right_player_score_rectangle_1 = right_player_score_surface_1.get_rect(center = (850,50))
left_player_score_surface_1 = font.render('1', True, 'White')
left_player_score_rectangle_1 = left_player_score_surface_1.get_rect(center = (400,50))

right_player_score_surface_2 = font.render('2', True, 'White')
right_player_score_rectangle_2 = right_player_score_surface_2.get_rect(center = (850,50))
left_player_score_surface_2 = font.render('2', True, 'White')
left_player_score_rectangle_2 = left_player_score_surface_2.get_rect(center = (400,50))

right_player_score_surface_3 = font.render('3', True, 'White')
right_player_score_rectangle_3 = right_player_score_surface_3.get_rect(center = (850,50))
left_player_score_surface_3 = font.render('3', True, 'White')
left_player_score_rectangle_3 = left_player_score_surface_3.get_rect(center = (400,50))

right_player_score_surface_4 = font.render('4', True, 'White')
right_player_score_rectangle_4 = right_player_score_surface_4.get_rect(center = (850,50))
left_player_score_surface_4 = font.render('4', True, 'White')
left_player_score_rectangle_4 = left_player_score_surface_4.get_rect(center = (400,50))

right_player_score_surface_5 = font.render('5', True, 'White')
right_player_score_rectangle_5 = right_player_score_surface_5.get_rect(center = (850,50))
left_player_score_surface_5 = font.render('5', True, 'White')
left_player_score_rectangle_5 = left_player_score_surface_5.get_rect(center = (400,50))

right_player_score_surface_6 = font.render('6', True, 'White')
right_player_score_rectangle_6 = right_player_score_surface_6.get_rect(center = (850,50))
left_player_score_surface_6 = font.render('6', True, 'White')
left_player_score_rectangle_6 = left_player_score_surface_6.get_rect(center = (400,50))

right_player_score_surface_7 = font.render('7', True, 'White')
right_player_score_rectangle_7 = right_player_score_surface_7.get_rect(center = (850,50))
left_player_score_surface_7 = font.render('7', True, 'White')
left_player_score_rectangle_7 = left_player_score_surface_7.get_rect(center = (400,50))

right_player_score_surface_8 = font.render('8', True, 'White')
right_player_score_rectangle_8 = right_player_score_surface_8.get_rect(center = (850,50))
left_player_score_surface_8 = font.render('8', True, 'White')
left_player_score_rectangle_8 = left_player_score_surface_8.get_rect(center = (400,50))

right_player_score_surface_9 = font.render('9', True, 'White')
right_player_score_rectangle_9 = right_player_score_surface_9.get_rect(center = (850,50))
left_player_score_surface_9 = font.render('9', True, 'White')
left_player_score_rectangle_9 = left_player_score_surface_9.get_rect(center = (400,50))

right_player_score_surface_10 = font.render('10', True, 'White')
right_player_score_rectangle_10 = right_player_score_surface_10.get_rect(center = (850,50))
left_player_score_surface_10 = font.render('10', True, 'White')
left_player_score_rectangle_10 = left_player_score_surface_10.get_rect(center = (400,50))

black_square_right = pygame.Rect(800, 10, 70, 70)
black_square_left = pygame.Rect(350, 10 ,70,70)

score_event_x_pos = 630
score_event_y_pos = 400

right_score_event_surface = font.render('Right player scored !', True, 'White')
right_score_event_rectangle = right_score_event_surface.get_rect(center = (score_event_x_pos,score_event_y_pos))
left_score_event_surface = font.render('Left player scored !', True, 'White')
left_score_event_rectangle = left_score_event_surface.get_rect(center = (score_event_x_pos,score_event_y_pos))
right_win_event_surface = font.render('Right player won !', True, 'White')
right_win_event_rectangle = right_win_event_surface.get_rect(center = (score_event_x_pos,score_event_y_pos))
left_win_event_surface = font.render('Left player won !', True, 'White')
left_win_event_rectangle = left_win_event_surface.get_rect(center = (score_event_x_pos,score_event_y_pos))

enter_prompt_surface = font.render('Press Enter to start', True, 'White')
enter_prompt_rectangle = enter_prompt_surface.get_rect(center = (600,600))
left_tutorial_surface1 = font.render('Left player :', True, 'White')
left_tutorial_rectangle1 = left_tutorial_surface1.get_rect(center = (250, 200))
left_tutorial_surface2 = font2.render('Press Z to move upwards and S to move downwards', True, 'White')
left_tutorial_rectangle2 = left_tutorial_surface2.get_rect(center = (260, 300))
right_tutorial_surface1 = font.render('Right player :', True, 'White')
right_tutorial_rectangle1 = right_tutorial_surface1.get_rect(center = (1000, 200))
right_tutorial_surface2 = font2.render('Press P to move upwards and M to move downwards', True, 'White')
right_tutorial_rectangle2 = right_tutorial_surface2.get_rect(center = (1000, 300))


def tutorial(): 
    global keyz, tutorialDone
    screen.blit(enter_prompt_surface, enter_prompt_rectangle)
    screen.blit(left_tutorial_surface1,left_tutorial_rectangle1)
    screen.blit(left_tutorial_surface2,left_tutorial_rectangle2)
    screen.blit(right_tutorial_surface1,right_tutorial_rectangle1)
    screen.blit(right_tutorial_surface2,right_tutorial_rectangle2)
    pygame.display.flip()
    keyz = pygame.key.get_pressed()
    if keyz[pygame.K_RETURN] :
        tutorialDone = True
        

#game loop
while done :
    
    for event in pygame.event.get():

        #closing window and keys detection
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            start_time = pygame.time.get_ticks()
            left_paddle_movement_y = -3
        elif keys[pygame.K_s]:
            left_paddle_movement_y = 3
        else:
            left_paddle_movement_y = 0
        if keys[pygame.K_p] :
            right_paddle_movement_y = -3
        elif keys[pygame.K_m]:
            right_paddle_movement_y = 3
        else :
            right_paddle_movement_y = 0

    #tutorial, kind of (just explains the controls but it's serviceable)
    if tutorialDone == False :
        tutorial()
    else :
        # paddles movement 
        left_paddle.move_ip(0, left_paddle_movement_y)
        left_paddle.clamp_ip(SCREEN_AREA)
        right_paddle.move_ip(0, right_paddle_movement_y)
        right_paddle.clamp_ip(SCREEN_AREA)

        # ball movement
        ball.move_ip(ball_direction)

        #score detection
        if ball.right == WIDTH :
            scoreSound.play()
            left_score_value += 1
            print(left_score_value)
            if left_score_value == 10 :
                screen.blit(left_win_event_surface, left_win_event_rectangle)
            else :
                screen.blit(left_score_event_surface, left_score_event_rectangle)

            pygame.draw.rect(screen, BLACK, black_square_left)
            pygame.display.flip()
            pygame.time.delay(3000)
            ball_direction = (0, 0)
            screen.fill(BLACK)
            ball.move_ip(-630,0)
            ball_direction = (1, random.choice(numbers))
            pygame.display.flip()
        if ball.left == 0:
            scoreSound.play()
            right_score_value += 1
            print(right_score_value)
            if right_score_value == 10 :
                screen.blit(right_win_event_surface, right_win_event_rectangle)
            else :
                screen.blit(right_score_event_surface, right_score_event_rectangle)
        
            pygame.draw.rect(screen, BLACK, black_square_right)
            pygame.display.flip()
            pygame.time.delay(3000)
            ball_direction = (0, 0)
            screen.fill(BLACK)
            ball.move_ip(630, 0)
            ball_direction = (-1, random.choice(numbers))
            pygame.display.flip()
        if ball.top == 0 or ball.bottom == HEIGHT :
            wallSound.play()
            ball_direction = ball_direction[0], -ball_direction[1]
        if right_paddle.colliderect(ball) :
            paddleSound.play()
            if right_paddle_movement_y > 0:
                ball_direction = -ball_direction[1], ball_direction[1]
            else :
                ball_direction = -ball_direction[1], ball_direction[0]
        if left_paddle.colliderect(ball) :
            paddleSound.play()
            if left_paddle_movement_y > 0:
                ball_direction = -ball_direction[1], ball_direction[1]
            else :
                ball_direction = -ball_direction[1], ball_direction[0]
    
        ball.clamp_ip(SCREEN_AREA)
    
        # screen update
        screen.fill(BLACK)
        match right_score_value :
            case 0 :
                screen.blit(right_player_score_surface_0,right_player_score_rectangle_0)
            case 1 :
                screen.blit(right_player_score_surface_1,right_player_score_rectangle_1)
            case 2 :
                screen.blit(right_player_score_surface_2,right_player_score_rectangle_2)
            case 3 :
                screen.blit(right_player_score_surface_3,right_player_score_rectangle_3)
            case 4 :
                screen.blit(right_player_score_surface_4,right_player_score_rectangle_4)
            case 5 :
                screen.blit(right_player_score_surface_5,right_player_score_rectangle_5)
            case 6 :
                screen.blit(right_player_score_surface_6,right_player_score_rectangle_6)
            case 7 :
                screen.blit(right_player_score_surface_7,right_player_score_rectangle_7)
            case 8 :
                screen.blit(right_player_score_surface_8,right_player_score_rectangle_8)
            case 9 :
                screen.blit(right_player_score_surface_9,right_player_score_rectangle_9)
            case 10 :
                screen.blit(right_player_score_surface_10,right_player_score_rectangle_10)
                right_score_value = 0
                left_score_value = 0

        match left_score_value :
            case 0 :
                screen.blit(left_player_score_surface_0,left_player_score_rectangle_0)
            case 1 :
                screen.blit(left_player_score_surface_1,left_player_score_rectangle_1)
            case 2 :
                screen.blit(left_player_score_surface_2,left_player_score_rectangle_2)
            case 3 :
                screen.blit(left_player_score_surface_3,left_player_score_rectangle_3)
            case 4 :
                screen.blit(left_player_score_surface_4,left_player_score_rectangle_4)
            case 5 :
                screen.blit(left_player_score_surface_5,left_player_score_rectangle_5)
            case 6 :
                screen.blit(left_player_score_surface_6,left_player_score_rectangle_6)
            case 7 :
                screen.blit(left_player_score_surface_7,left_player_score_rectangle_7)
            case 8 :
                screen.blit(left_player_score_surface_8,left_player_score_rectangle_8)
            case 9 :
                screen.blit(left_player_score_surface_9,left_player_score_rectangle_9)
            case 10 :
                screen.blit(left_player_score_surface_10,left_player_score_rectangle_10)
                right_score_value = 0
                left_score_value = 0
    
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.rect(screen, WHITE, ball)
        pygame.display.flip()
        clock.tick(120)