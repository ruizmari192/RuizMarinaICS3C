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

def fire_bullet(player, bullets):
    """
    -------------------------------------------------------
    Spawns a new bullet starting at the player's current center position.
    -------------------------------------------------------
    Parameters:
       player - the rectangle representing the player (pygame.Rect)
       bullets - the list where active bullet Rects are stored (list)
    -------------------------------------------------------
    """
    bullet_width = 15
    bullet_height = 15
    #reset bullet position to the player's position when fired
    bullet_x = player.x
    bullet_y = player.y
  
    new_bullet = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    bullets.append(new_bullet)
    return
  
    


pygame.init()
# Set screen resolution
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500  

# Set up colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Set up the player
player_size = 25
player_x = 30
player_y = 30
player = pygame.Rect (30, 30, player_size, player_size)
speed = 4

#set up the enemies

enemy_size = 25
enemy_speed = 1.2
#enemy 1 (it will appear in the right section of the screen (350-650))
enemy1_x = random.randint (350, SCREEN_WIDTH - enemy_size)
enemy1_y = random.randint (50, SCREEN_HEIGHT - enemy_size)
enemy1 = pygame.Rect (enemy1_x, enemy1_y, enemy_size, enemy_size)

#enemy2 (will appear in the left side of the screen)
enemy2_x = random.randint(50, SCREEN_WIDTH - enemy_size)
enemy2_y = random.randint(250, SCREEN_HEIGHT - enemy_size)
enemy2 = pygame.Rect(enemy2_x, enemy2_y, enemy_size, enemy_size)

#to have a list for the new bullets
bullets = []
bullet_speed = 4

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

# Set up the game
clock = pygame.time.Clock()
running = True
won = False
# Main game loop
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not won:
                fire_bullet (player, bullets)

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

    # Get the keys being pressed
    keys = pygame.key.get_pressed()

    if not won:
        #update player position
        handle_player_movement(keys, player, speed, walls)

        #to keep the player within the screen bounds
        check_bounds(player, SCREEN_WIDTH, SCREEN_HEIGHT)

        for bullet in bullets:
            bullet.y -= bullet_speed

        #check if the player won
        if player.colliderect(exit_rect):
            won = True

#DRAWING:
  # Draw the background
    screen.fill(WHITE)

    # Draw the maze walls
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

    # Draw the exit
    pygame.draw.rect(screen, GREEN, exit_rect)

    # Draw the player
    pygame.draw.rect(screen, RED, player)

    #draw the bullet
    for bullet in bullets:
        pygame.draw.rect (screen, BLUE, bullet)

    #draw the enemy
    enemy_rect = pygame.Rect(player.left, player.right, enemy_size, enemy_size)
    pygame.draw.rect (screen, BLUE, enemy_rect)

    # Display the winning message
    if won:
        font = pygame.font.SysFont(None, 48)
        message = font.render("YOU WIN!", True, BLACK)
        screen.blit(message, (220, 180))

    # Update the display
    pygame.display.flip()

    # Limit the game to 60 FPS
    clock.tick(60)

# Close Pygame
pygame.quit()