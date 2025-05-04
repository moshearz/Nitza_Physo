import pygame
pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 50)
background_image = pygame.image.load("image_2025-04-08_142824057.jpg")  # or whatever you're using
