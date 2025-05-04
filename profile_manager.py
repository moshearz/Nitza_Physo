from CONSTANTS import *
import sys

def profile_manager(entered,username):

    while not entered:
        screen.blit(background_image, (0, 0))
        prompt_surface = font.render("Hey, please Enter your name: ", True, (0, 0, 0))
        screen.blit(prompt_surface, (input_box.x - 60, input_box.y - 60))

        pygame.draw.rect(screen, (255, 255, 255), input_box)
        text_surface = font.render(username, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

        continue_button.draw(screen, hover=continue_button.rect.collidepoint(pygame.mouse.get_pos()))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif event.key == pygame.K_RETURN and username.strip() != "":
                    entered = True
                    return username
                else:
                    username += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.rect.collidepoint(event.pos) and username.strip() != "":
                    entered = True
                    return username

        pygame.display.flip()
        pygame.time.delay(50)
