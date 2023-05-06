import sys
import pygame
import pygame.mixer

# Initialize Pygame mixer
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load("tcwextended.mp3")

# Play the music file in an infinite loop
pygame.mixer.music.play(-1)

# Define some colors
WHITE = (255, 255, 255)
BLUE = (240, 248, 255)
TRANSPARENT_BLUE = (64, 0, 255, 42)

# Set the dimensions of the screen
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 478

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('SPACE INVADERS')

# Load the menu background image
background_image1 = pygame.image.load("background1.png").convert()



# Create a font object
font = pygame.font.Font('Starwars.TTF', 36)

# Create the start button
start_button = font.render('Start Game', True, WHITE)
start_rect = start_button.get_rect()
start_rect.centerx = SCREEN_WIDTH // 2
start_rect.centery = SCREEN_HEIGHT // 2 - 100

# Create the quit button
quit_button = font.render('Quit Game', True, WHITE)
quit_rect = quit_button.get_rect()
quit_rect.centerx = SCREEN_WIDTH // 2
quit_rect.centery = SCREEN_HEIGHT // 2

# Create semi-transparent surfaces for button backgrounds
start_button_bg = pygame.Surface((start_button.get_width() + 20, start_button.get_height() + 10), pygame.SRCALPHA)
start_button_bg.fill(TRANSPARENT_BLUE)
start_button_bg_rect = start_button_bg.get_rect(center=start_rect.center)

quit_button_bg = pygame.Surface((quit_button.get_width() + 20, quit_button.get_height() + 10), pygame.SRCALPHA)
quit_button_bg.fill(TRANSPARENT_BLUE)
quit_button_bg_rect = quit_button_bg.get_rect(center=quit_rect.center)

# Blit the buttons and backgrounds on the screen
screen.blit(background_image1, [0, 0])
screen.blit(start_button_bg, start_button_bg_rect)
screen.blit(start_button, start_rect)
screen.blit(quit_button_bg, quit_button_bg_rect)
screen.blit(quit_button, quit_rect)


# Create a variable to keep track of whether the game is running or not
game_running = True
# Create a variable to keep track of whether the sound is muted or not
sound_muted = False

# Start the game loop
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the start button was clicked
            if start_rect.collidepoint(event.pos):
                # Stop the music
                pygame.mixer.music.stop()
                # Start the game here
                import main
            # Check if the quit button was clicked
            if quit_rect.collidepoint(event.pos):
                # Quit the game here
                game_running = False


    # Update the screen
    pygame.display.update()

# Quit the game
pygame.quit()
sys.exit()
