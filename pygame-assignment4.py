import pygame
import random

def check_collision (player, walls): #to make it easier to check collision without printing it everytime
    """
    -------------------------------------------------------
    Checks whether the player collides with any of the maze walls.
    -------------------------------------------------------
    Parameters:
       player - the rectangle representing the player (pygame.Rect)
       walls - a list of rectangles representing the maze walls (list)
    Returns:
       collision - True if the player collides with a wall,
                   False otherwise (bool)
    -------------------------------------------------------
    """
    #MAIN function:
    #
    for wall in walls:
        if player.colliderect(wall): #to see if it collides with the wall
            return True #a collision happened
    return False

def check_bounds(rect_object, max_width, max_height): #make it easier to be sure that the player is in the screen
    """
        -------------------------------------------------------
        Keeps the player inside the screen
        -------------------------------------------------------
        Parameters:
            rect_object - the rectangle object whose position is being checked (pygame.Rect)
            max_width - the maximum width boundary (screen width).
            max_height - the maximum height boundary
        Returns:
            None, it modifies the rect_object directly
        -------------------------------------------------------
    """
    #MAIN function
#horizontal bounds
    if rect_object.left < 0: #to check if the player.x position is getting so close to the edge that is gonna get out the screen
        rect_object.left = 0 #to rearrange the rectangle at x=0 (the edge)
    if rect_object.right > max_width: #check if it's gonna pass the max_width (800)
        rect_object.right = max_width #to make it impossible to get out the screen
# Vertical Bounds 
    if rect_object.top < 0: #check if the top of the player is getting closer to the top edge
        rect_object.top = 0 #to stop the player from getting out the screen
    if rect_object.bottom > max_height: #to check if it collides with the max_height (600)
        rect_object.bottom = max_height #to set the boundary

def handle_player_movement(keys, player, speed, walls):
    """
    -------------------------------------------------------
    Processes keyboard input to move the player rectangle directly and 
    handles wall collisions.
    -------------------------------------------------------
    Parameters:
       keys - the dictionary/list of pressed keys from pygame (scancode wrapper)
       player - the rectangle representing the player (pygame.Rect)
       speed - the movement speed value (int)
       walls - a list of rectangles representing the maze walls (list)
    Returns:
       None, it modifies the player rectangle directly
    -------------------------------------------------------
    """
   # Move left
    if keys[pygame.K_LEFT]:
        player.x -= speed
        if check_collision(player, walls) == True:
            while check_collision(player, walls) == True:
                player.x += 1 # Undo movement on collision

    # Move right
    if keys[pygame.K_RIGHT]:
        player.x += speed
        if check_collision(player, walls) == True:
            while check_collision(player, walls) == True:
                player.x -= 1  # Undo movement on collision

    # Move up
    if keys[pygame.K_UP]:
        player.y -= speed
        if check_collision(player, walls) == True:
            while check_collision(player, walls) == True:
                player.y += 1  # Undo movement on collision

    # Move down
    if keys[pygame.K_DOWN]:
        player.y += speed
        if check_collision(player, walls) == True:
            while check_collision(player, walls) == True:
                player.y -= 1  # Undo movement on collision
    


pygame.init()
pygame.font.init()

# Set screen resolution
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500  

# Set up colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
PLAYER_COLOR = (64, 47, 174)
RED = (249, 75, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
PURPLE = (150, 0, 150) 
ORANGE = (255, 128, 0)  
YELLOW = (255, 255, 0)
GOLD = (225, 215, 0)
BROWN = (165, 42, 42)
DARK_GREEN = (34, 139, 34)
LIGHT_GREEN = (193, 255, 214)

#for level 2:
stars = [
    pygame.Rect(180, 20, 15, 15),
    pygame.Rect(350, 260, 15, 15),
    pygame.Rect(640, 100, 15, 15)
]


# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Set up the player
player_size = 25
player_x = 30
player_y = 30
player = pygame.Rect (30, 30, player_size, player_size)
speed = 4

#set up music 
pygame.mixer.music.load("atlasaudio-arcade-game-617542.mp3")
pygame.mixer.music.play(-1)

#set up the enemies

enemy_size = 25
enemy_speed = 0.8
#enemy 1 (it will appear in the right section of the screen (350-650))
enemy1_x = random.randint (350, SCREEN_WIDTH - enemy_size)
enemy1_y = 0
enemy1 = pygame.Rect (enemy1_x, enemy1_y, enemy_size, enemy_size)

#enemy2 (will appear in the left side of the screen)
enemy2_x = random.randint(50, SCREEN_WIDTH - enemy_size)
enemy2_y = 0
enemy2 = pygame.Rect(enemy2_x, enemy2_y, enemy_size, enemy_size)

#bullets creation
bullet_x = 0            
bullet_y = 0            
bullet_speed = 5        
bullet_active = False 

# Create the exit
exit_rect = pygame.Rect(540, 340, 30, 30)

# Create the maze walls
walls = [
    pygame.Rect(80, 0, 20, 400),
    pygame.Rect(100, 200, 60, 20),
    pygame.Rect(40, 100, 60, 20),
    pygame.Rect(150, 300, 20, 200),
    pygame.Rect(220, 100, 20, 400),
    pygame.Rect(140, 140, 100, 20),
    pygame.Rect(130, 50, 60, 60),
    pygame.Rect(220, 300, 120, 20),
    pygame.Rect(300, 0, 20, 250),
    pygame.Rect(400, 100, 20, 350),
    pygame.Rect(300, 200, 70, 20),
    pygame.Rect(580, 0, 20, 250),
    pygame.Rect(450, 150, 140, 20),
    pygame.Rect(360, 80, 170, 20),
    pygame.Rect(380, 300, 250, 20),
    pygame.Rect(340,400,260,20)
]

#gate configuration for level 2
gate_wall = pygame.Rect (500, 320, 20, 80)
gate_open = False #to track if the gate is open

current_level = 1 #to establish the levels

# Set up the game
clock = pygame.time.Clock()
running = True
won1 = False
won2 = False
lost = False
menu_screen = False #to have a condition for when I freeze the game


# Main game loop
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 #       if event.type == pygame.KEYDOWN:
  #          if event.key == pygame.K_SPACE and freeze_transition_screen:
   #             #to pass to level 2, reset the player and end the waiting window
    #            current_level = 2
     #           player.x = 30
      #          player.y = 30
       #         walls.append(gate_wall)
       #         freeze_transition_screen = False 


    #get the keys being pressed
    keys = pygame.key.get_pressed ()
    if not menu_screen: 
        if not won2 and not lost: #to play only if I didnt win

            handle_player_movement(keys, player, speed, walls) #call the function to check movement and wall collision
            player_x = player.x
            player_y = player.y

            check_bounds(player, SCREEN_WIDTH, SCREEN_HEIGHT) #call the function to check the boundaries

            #set the enemies movement logic (towards the player)
            # enemy one chase logic:
            if enemy1_x < player_x: #to make the enemy move differently depending on the player
                enemy1_x += enemy_speed
            elif enemy1_x > player_x:
                enemy1_x -= enemy_speed
            
            if enemy1_y < player_y:
                enemy1_y += enemy_speed
            elif enemy1_y > player_y:
                enemy1_y -= enemy_speed

            # enemy two logic, same as the enemy one but with its different speed
            if enemy2_x < player_x:
                enemy2_x += enemy_speed
            elif enemy2_x > player_x:
                enemy2_x -= enemy_speed
            
            if enemy2_y < player_y:
                enemy2_y += enemy_speed
            elif enemy2_y > player_y:
                enemy2_y -= enemy_speed

            enemy1.x = int(enemy1_x)
            enemy1.y = int(enemy1_y)
            enemy2.x = int(enemy2_x)
            enemy2.y = int(enemy2_y)

            #if the player touches either enemy, stop the loop
            if player.colliderect(enemy1) or player.colliderect(enemy2):
                print("Game Over! An enemy caught you.")
                lost = True

            if keys[pygame.K_SPACE]:         
                if not bullet_active:
                    bullet_x = player_x  
                    bullet_y = player_y
                    bullet_active = True

            if bullet_active:
                bullet_y -= bullet_speed 
                bullet_rect = pygame.Rect(bullet_x, bullet_y, 15, 15)

                # Si la bala sale del mapa, desaparece
                if bullet_x >= SCREEN_WIDTH or bullet_y >= SCREEN_HEIGHT or bullet_y <= 0 or bullet_x <= 0:                      
                    bullet_active = False
            
                # collision with enemy 1
                if bullet_rect.colliderect(enemy1):
                    enemy1_x = random.randint(0, SCREEN_WIDTH - enemy_size)
                    enemy1_y = 0
                    bullet_active = False 
                
                # collision with enemy 2
                if bullet_rect.colliderect(enemy2):
                    enemy2_x = random.randint(0, SCREEN_WIDTH - enemy_size)
                    enemy2_y = 0
                    bullet_active = False 

            #level 1 exit check
            if current_level == 1 and player.colliderect(exit_rect):
                current_level = 2
                won1 = True
                menu_screen = True
                #reset player and enemies for level 2
                player.x = 30
                player.y = 30
                enemy1_x = random.randint(350, SCREEN_WIDTH - enemy_size)
                enemy1_y = 0
                enemy2_x = random.randint(50, SCREEN_WIDTH - enemy_size)
                enemy2_y = 0
                if gate_wall not in walls:
                    walls.append(gate_wall)

            #level 2 star and exit rect

            elif not lost and current_level == 2 and won1 == True and menu_screen == False and won2 == False:
                for star in reversed(stars):
                    if player.colliderect(star):
                        stars.remove(star) # Safely delete the star from our list
                if not stars and not gate_open:
                    if gate_wall in walls:
                        walls.remove(gate_wall)
                        gate_open = True
                if player.colliderect(exit_rect):
                    won2 = True

    

    #to keep the player within the screen bounds
    check_bounds(player, SCREEN_WIDTH, SCREEN_HEIGHT)


        #check if the player won
       # if player.colliderect(exit_rect):
          #  won = True

    #if won1 and current_level == 2 and menu_screen == True:
      

   
    

#DRAWING:
  # Draw the background
    
    screen.fill(LIGHT_GREEN)


    # Draw the maze walls
    for wall in walls:
        pygame.draw.rect(screen, DARK_GREEN, wall)
        if wall == gate_wall:
            pygame.draw.rect(screen, BLUE, wall)
        else:
            pygame.draw.rect(screen, DARK_GREEN, wall)

    # Draw the exit
    pygame.draw.rect(screen, GREEN, exit_rect)

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    #
    #draw the enemy
    pygame.draw.rect(screen, RED, enemy1)
    pygame.draw.rect(screen, RED, enemy2)

    #draw the text for the level 
    font_level = pygame.font.SysFont(None, 25)
    level_text = font_level.render("Level: " + str(current_level), True, BLACK) #to convert the text into image
    screen.blit(level_text, (10, 20))

    if bullet_active:
        pygame.draw.rect(screen, YELLOW, (bullet_x, bullet_y, 15, 15))

    #if won1 == True and current_level == 2 and menu_screen == True:
     #   font = pygame.font.SysFont(None, 40)
      #  message = font.render("Level 2: Press SPACE to Play", True, BLACK)
       # screen.blit(message, (250, 275))
        #for star in stars:
#           pygame.draw.rect(screen, GOLD, star)
        #print("HERE 1")
    if menu_screen == True:
        menu_bg = pygame.Surface((450, 120))
        menu_bg.fill(WHITE)
        menu_bg.set_alpha(200)
        screen.blit(menu_bg, (125, 220))

        font = pygame.font.SysFont(None, 36)
        message = font.render("Level 2: Press SPACE to Play", True, BLACK)
        screen.blit(message, (175, 265))


        if keys[pygame.K_SPACE]:
            menu_screen = False

    if current_level == 2 and won2 == False:
        for star in stars:
                    pygame.draw.rect(screen, GOLD, star)

    # Display the winning message
    if won2 == True:
        font = pygame.font.SysFont(None, 48)
        message = font.render("YOU WIN!", True, BLACK)
        screen.blit(message, (220, 180))
        print("HERE 3")

    # Update the display
    pygame.display.flip()

    # Limit the game to 60 FPS
    clock.tick(60)

# Close Pygame
pygame.quit()