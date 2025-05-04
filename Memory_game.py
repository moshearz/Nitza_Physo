from CONSTANTS import *
import random
import pygame

pygame.init()
back_button = Button(50, HEIGHT - 150, 200, 50, "Exit", MENU)
color_keys = list(colors.keys())

def memory_game(current_state, running):
    sequence = []
    player_sequence = []
    waiting_for_input = False
    game_over = False

    def draw_rects(highlight=None):
        screen.blit(background_image, (0, 0))
        for color, rect in rects.items():
            base, bright = colors[color]
            pygame.draw.rect(screen, bright if color == highlight else base, rect)
        back_button.draw(screen)
        pygame.display.flip()

    def flash_sequence(seq):
        for color in seq:
            draw_rects(highlight=color)
            pygame.time.delay(600)
            draw_rects()
            pygame.time.delay(300)

    def reset_game():
        nonlocal sequence, player_sequence, waiting_for_input, game_over
        sequence = [random.choice(color_keys)]
        player_sequence = []
        game_over = False
        flash_sequence(sequence)
        waiting_for_input = True

    reset_game()

    clock = pygame.time.Clock()

    while running:
        draw_rects()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            if back_button.check_click(event) == MENU:
                return MENU

            if event.type == pygame.MOUSEBUTTONDOWN and waiting_for_input and not game_over:
                for color, rect in rects.items():
                    if rect.collidepoint(event.pos):
                        player_sequence.append(color)
                        draw_rects(highlight=color)
                        pygame.time.delay(300)
                        draw_rects()

                        # Check if the player's input is correct
                        if player_sequence[-1] != sequence[len(player_sequence) - 1]:
                            game_over = True
                        elif len(player_sequence) == len(sequence):
                            pygame.time.delay(500)
                            sequence.append(random.choice(color_keys))
                            player_sequence = []
                            flash_sequence(sequence)

        if game_over:
            screen.blit(background_image, (0, 0))
            text = font.render("Game Over!", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 25))
            back_button.draw(screen)
            pygame.display.flip()
            pygame.time.delay(1500)
            reset_game()

        pygame.display.flip()
        clock.tick(60)  # Limit frame rate to 60 FPS
