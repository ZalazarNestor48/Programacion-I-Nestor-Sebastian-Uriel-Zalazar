import os, sys, pygame
from pygame.locals import *
from juego import tirar_dados
from puntuacion import calcular_jugada
from archivos import guardar_puntaje, top_n
import pygame_juego

SCREEN_W, SCREEN_H = 960, 640

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption('Generala Temática - Pygame')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    menu = ['Jugar', 'Estadísticas', 'Créditos', 'Salir']
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
                    opt = menu[selected]
                    if opt == 'Jugar':
                        pygame_juego.run_game(screen, clock, font, tirar_dados, calcular_jugada, guardar_puntaje)
                    elif opt == 'Estadísticas':
                        pygame_juego.show_stats(screen, font, top_n)
                    elif opt == 'Créditos':
                        pygame_juego.show_credits(screen, font)
                    elif opt == 'Salir':
                        running = False
            elif event.type == MOUSEBUTTONDOWN:
                mx,my = event.pos
                start_y = 200
                for i,opt in enumerate(menu):
                    rect = pygame.Rect(380, start_y + i*60, 200, 48)
                    if rect.collidepoint(mx,my):
                        selected = i
                        if opt == 'Jugar':
                            pygame_juego.run_game(screen, clock, font, tirar_dados, calcular_jugada, guardar_puntaje)
                        elif opt == 'Estadísticas':
                            pygame_juego.show_stats(screen, font, top_n)
                        elif opt == 'Créditos':
                            pygame_juego.show_credits(screen, font)
                        elif opt == 'Salir':
                            running = False

        screen.fill((18,32,50))
        title = font.render('Generala - Pygame', True, (255,255,255))
        screen.blit(title, (SCREEN_W//2 - title.get_width()//2, 60))

        start_y = 200
        for i,opt in enumerate(menu):
            color = (255,255,255) if i == selected else (160,160,160)
            rect = pygame.Rect(380, start_y + i*60, 200, 48)
            pygame.draw.rect(screen, (60,60,60), rect, border_radius=8)
            text_s = font.render(opt, True, color)
            screen.blit(text_s, (rect.x + (rect.w - text_s.get_width())//2, rect.y + (rect.h - text_s.get_height())//2))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()