import pygame
import random

def check_collision (player, walls):
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
        if player.colliderect(wall):
            return True #a collision happened
    return False

def check_bounds(rect_object, max_width, max_height):
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
    if rect_object.left < 0:
        rect_object.left = 0
    if rect_object.right > max_width:
        rect_object.right = max_width
# Vertical Bounds 
    if rect_object.top < 0:
        rect_object.top = 0
    if rect_object.bottom > max_height:
        rect_object.bottom = max_height

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
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400  

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
player = pygame.Rect (30, 30, player_size, player_size)
speed = 4

#to have a list for the new bullets
bullets = []
bullet_speed = 4

# Create the exit
exit_rect = pygame.Rect(540, 340, 30, 30)

# Create the maze walls
walls = [
    pygame.Rect(100, 0, 20, 300),
    pygame.Rect(200, 100, 20, 300),
    pygame.Rect(300, 0, 20, 250),
    pygame.Rect(400, 100, 20, 300),
    pygame.Rect(500, 0, 20, 250)
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