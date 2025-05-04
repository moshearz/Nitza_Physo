from Hand_Tracking import *
from Breath_excersise import *
from Extras import *
from Memory_game import *
from profile_manager import *
import CONSTANTS
from Chatbot import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Wellness Games')

start_music()

current_state = MENU
running = True
username = ""
entered = False

username = profile_manager(entered,username)

while running:
    username_rect = font.render(f"Hello {username}, Welcome to Nitza-Physo!", True, (0, 0, 0))
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0),(date_rect.x - 5, date_rect.y - 5, date_rect.width + 10, date_rect.height + 10))  # Black rectangle
    screen.blit(date_surface, date_rect)
    screen.blit(username_rect,(start_x - 200,start_y + button_height + button_spacing -35 - 10))

    if current_state == MENU:
        for button in Main_Menu:
            button.draw(screen, hover=button.rect.collidepoint(pygame.mouse.get_pos()))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in Main_Menu + [CONSTANTS.Main_Menu[2]]:
                action = button.check_click(event)
                if action:
                    if action == "quit":
                        running = False
                    elif action == "music 0" and pygame.mixer.music.get_volume() != 0:
                        pygame.mixer.music.set_volume(0)
                        CONSTANTS.Main_Menu[4].text = "turn on music"
                    elif action == "music 0" and pygame.mixer.music.get_volume() == 0:
                        pygame.mixer.music.set_volume(100)
                        CONSTANTS.Main_Menu[4].text = "turn off music"
                    else:
                        current_state = action

    elif current_state == GAMES_MENU:
        for button in Games:
            button.draw(screen, hover=button.rect.collidepoint(pygame.mouse.get_pos()))

        back_button = Button(start_x,550, button_width, button_height, "Back", MENU)
        back_button.draw(screen, hover=back_button.rect.collidepoint(pygame.mouse.get_pos()))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in Games + [back_button]:
                action = button.check_click(event)
                if action:
                    if action == MENU:
                        current_state = MENU
                    else:
                        current_state = action

    elif current_state == BREATHING:
        if breathing_exercise(current_state, running) == MENU:
            current_state = MENU
    elif current_state == HAND_TRACKING:
        if hand_tracking_game(current_state, running) == MENU:
            current_state = MENU
    elif current_state == CREDITS:
        if credits_screen(current_state, running) == MENU:
            current_state = MENU
    elif current_state == Memory:
        if memory_game(current_state, running) == MENU:
            current_state = MENU
    elif current_state == CHAT_BOT:
         current_state = chatbot_screen()
         continue


    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
sys.exit()