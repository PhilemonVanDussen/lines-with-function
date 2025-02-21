# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_line(screen, line_color, start_point, end_point, width):
    pygame.draw.line(screen, line_color, start_point, end_point, width,)


def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.GREEN) # Use color from config

        width = 5
        line_color = config.BLUE

        start_pos1 = [400, 350]
        end_pos1 = [225, 425]
        
        
        start_pos2 = [400, 350]
        end_pos2 = [225, 425]
        
        
        start_pos3 = [400, 350]
        end_pos3 = [225, 425]
        

        start_pos4 = [400, 350]
        end_pos4 = [225, 425]
        

        start_pos5 = [400, 350]
        end_pos5 = [225, 425]
        

        start_pos6 = [400, 350]
        end_pos6 = [225, 425]
        

        draw_line(screen, line_color, start_pos1, end_pos1, width) 
        
        
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



