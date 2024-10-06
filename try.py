import pygame
import random
import streamlit as st
from PIL import Image
import numpy as np

# Initialize pygame
pygame.init()

# Constants for the game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 52
PIPE_HEIGHT = 320
PIPE_GAP = 150
GRAVITY = 1
FLAP_STRENGTH = -12
BIRD_X = 50

# Set up game display
screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

# Bird settings
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0

# Pipe settings
pipe_x = SCREEN_WIDTH
pipe_height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)

# Game variables
score = 0
game_over = False

# Load images
bird_image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_image.fill((255, 255, 0))
pipe_image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
pipe_image.fill((0, 255, 0))

# Capture Pygame screen as an image
def capture_screen():
    data = pygame.surfarray.array3d(screen)
    img = np.transpose(data, (1, 0, 2))
    return img

# Game logic
def flappy_bird_game(user_input):
    global bird_y, bird_velocity, pipe_x, pipe_height, score, game_over

    # Bird movement
    if user_input == "flap" and not game_over:
        bird_velocity = FLAP_STRENGTH

    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # Pipe movement
    pipe_x -= 5
    if pipe_x < -PIPE_WIDTH:
        pipe_x = SCREEN_WIDTH
        pipe_height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        score += 1

    # Check for collisions
    if (bird_y < 0 or bird_y > SCREEN_HEIGHT - BIRD_HEIGHT or
        (pipe_x < BIRD_X + BIRD_WIDTH < pipe_x + PIPE_WIDTH and 
         not (pipe_height < bird_y < pipe_height + PIPE_GAP))):
        game_over = True

    # Draw everything
    screen.fill((135, 206, 250))  # Sky blue background
    screen.blit(bird_image, (BIRD_X, bird_y))
    screen.blit(pipe_image, (pipe_x, pipe_height - PIPE_HEIGHT))
    screen.blit(pipe_image, (pipe_x, pipe_height + PIPE_GAP))

    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    if game_over:
        game_over_surface = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_surface, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))

# Streamlit interface
st.title("Flappy Bird in Streamlit")

# Get user input from Streamlit
user_input = st.button("Flap")  # Simulate the "flap" action

# Run game logic
flappy_bird_game("flap" if user_input else "")

# Capture the pygame surface as an image and display it in Streamlit
img = capture_screen()
img = Image.fromarray(img)
st.image(img, caption="Flappy Bird", use_column_width=True)

# Restart button
if game_over:
    if st.button("Restart"):
        bird_y = SCREEN_HEIGHT // 2
        bird_velocity = 0
        pipe_x = SCREEN_WIDTH
        pipe_height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        score = 0
        game_over = False
