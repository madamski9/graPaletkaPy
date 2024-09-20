from settings import FONT, WIN, WIDTH
import pygame

def draw_button(text, y, color):
    text_surface = FONT.render(text, 1, pygame.Color(color))
    text_rect = text_surface.get_rect(center=(WIDTH / 2, y))
    
    WIN.blit(text_surface, text_rect)

    return text_rect