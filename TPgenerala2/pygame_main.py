import os
import sys
import pygame
from pygame.locals import *

# tus módulos reales
from juego import tirar_dados
from puntuacion import calcular_jugada
from archivos import guardar_puntaje

import pygame_juego as pj

BASE_DIR = os.path.dirname(__file__)
SCREEN_W, SCREEN_H = 960, 640


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Generala LoL - TP Pygame")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)

    bg = None

    menu = ["Jugar", "Créditos", "Salir"]
    selected = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    selected = (selected + 1) % len(menu)
                elif event.key == K_UP:
                    selected = (selected - 1) % len(menu)
                elif event.key == K_RETURN:
                    if menu[selected] == "Jugar":
                        pj.run_game(screen, clock, font, tirar_dados, calcular_jugada, guardar_puntaje)
                    elif menu[selected] == "Créditos":
                        pj.show_credits(screen, font)
                    elif menu[selected] == "Salir":
                        running = False

        screen.fill((20, 30, 45))
        title = font.render("Generala Temática LoL", True, (255,255,255))
        screen.blit(title, (SCREEN_W//2 - title.get_width()//2, 60))

        y = 200
        for i,op in enumerate(menu):
            color = (255,255,255) if i == selected else (150,150,150)
            s = font.render(op, True, color)
            screen.blit(s, (SCREEN_W//2 - s.get_width()//2, y))
            y += 60

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()