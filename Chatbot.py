import pygame
from AzureChatAPI import ask_chatbot
from CONSTANTS import *
from BUTTONS import Button

def chatbot_screen():
    FONT = pygame.font.Font("fonts/Alef-Regular.ttf", 28)
    CHAT_FONT = pygame.font.Font(None, 32)

    user_input = ""
    ai_response = ""
    input_box = pygame.Rect(100, HEIGHT - 150, 1000, 60)
    back_button = Button(50, HEIGHT - 200, 200, 50, "Exit", MENU)

    active = False
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')
    color = color_passive

    running = True

    def rtl(text):
        return text[::-1]

    while running:
        screen.blit(background_image, (0, 0))

        # Greeting text
        text_surface = FONT.render(
            rtl("שלום! הגעת לצ'אט בוט פיזיותרפיה של ניצנים אשדוד 3. אני כאן כדי לתת תמיכה בנושא פיזיותרפיה ועוד!"),
            True, (255, 255, 255))
        text_surface1 = FONT.render(
            rtl("תרגיש חופשי לשאול מה אתה רוצה (באנגלית בבקשה, אני פרוטוטייפ ראשוני)"),
            True, (255, 255, 255))
        screen.blit(text_surface, (100, 100))
        screen.blit(text_surface1, (100, 200))

        # Draw input box
        pygame.draw.rect(screen, color, input_box, 2)
        input_surface = FONT.render(user_input, True, (255, 255, 255))
        screen.blit(input_surface, (input_box.x + 10, input_box.y + 10))

        # Draw AI response
        if ai_response:
            response_lines = ai_response.split('\n')
            for i, line in enumerate(response_lines):
                response_surface = CHAT_FONT.render(line, True, (255, 255, 255))
                screen.blit(response_surface, (100, 400 + i * 40))

        # Draw back button
        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

            if back_button.check_click(event) == MENU:
                return MENU

            if event.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(event.pos)
                color = color_active if active else color_passive

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    try:
                        ai_response = ask_chatbot(user_input)
                    except Exception:
                        ai_response = "שגיאה בשליחת ההודעה."
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    if len(user_input) < 100:
                        user_input += event.unicode

        pygame.display.flip()
        pygame.time.delay(50)
