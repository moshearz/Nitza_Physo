from datetime import datetime
import pygame
pygame.init()
from BUTTONS import Button
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)


font = pygame.font.Font(None, 60)

current_time = datetime.now().strftime("%d/%m/%y")
date_surface = font.render(current_time, True, (255, 255, 255))
date_rect = date_surface.get_rect(topleft=(10, 10))
info = pygame.display.Info()
pygame.display.set_caption('Wellness Games')
crown = pygame.image.load("crown.png")
crown = pygame.transform.scale(crown,(70,70))
background_image = pygame.image.load("image_2025-04-08_142824057.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


pygame.mixer.music.load("song.mp3")

font = pygame.font.Font(None, 60)

MENU = "menu"
BREATHING = "breathing"
HAND_TRACKING = "hand_tracking"
Memory = "Memory"
CREDITS = "credits"
GAMES_MENU = "games_menu"
CHAT_BOT = "chat_bot"


button_width = 300
button_height = 40
button_spacing = 10
start_x = (WIDTH - button_width) // 2
start_y = (HEIGHT - (4 * button_height + 3 * button_spacing) - 250) // 2 + 180


Main_Menu = [
    Button(start_x, start_y + 2 *(button_height + button_spacing), button_width, button_height, "Credits", CREDITS),
    Button(start_x, start_y + 4 * (button_height + button_spacing), button_width, button_height, "Quit", "quit"),
    Button(start_x, start_y + (button_height + button_spacing), button_width, button_height,"Games", GAMES_MENU),
    Button(start_x, start_y + 3 * (button_height + button_spacing), button_width, button_height,"Chatbot", CHAT_BOT),
    Button(start_x - 480, start_y + (button_height + button_spacing) + 200, button_width, button_height ,"Turn off Music","music 0")

]
Games = [
    Button(start_x - 40, start_y - 30, button_width + 90, button_height + 10, "Breathing Exercise", BREATHING),
    Button(start_x , start_y + 2 * (button_height + button_spacing) - 25, button_width, button_height, "Memory game", Memory),
    Button(start_x, start_y + button_height + button_spacing - 25, button_width, button_height, "Hand Tracking",HAND_TRACKING)

]

input_box = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 40, 400, 50)
new_profile_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 30, 200, 50, "Create Profile", "create")
continue_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 40, 200, 50, "Continue", "continue")
breath_instructions = ["Inhale...", "Hold...", "Exhale...", "Hold..."]
breath_durations = [4, 4, 6, 2]

colors = {
    "red": ((255, 0, 0), (255, 255, 255)),
    "green": ((0, 255, 0), (255, 255, 255)),
    "blue": ((0, 0, 255), (255, 255, 255)),
    "yellow": ((255, 255, 0), (255, 255, 255))
}

rects = {
    "red": pygame.Rect((WIDTH - 150) // 2 - 80, (HEIGHT - 150) // 2 - 80, 150, 150),
    "green": pygame.Rect((WIDTH - 150) // 2 + 80, (HEIGHT - 150) // 2 - 80, 150, 150),
    "blue": pygame.Rect((WIDTH - 150) // 2 - 80, (HEIGHT - 150) // 2 + 80, 150, 150),
    "yellow": pygame.Rect((WIDTH - 150) // 2 + 80, (HEIGHT - 150) // 2 + 80, 150, 150)
}
