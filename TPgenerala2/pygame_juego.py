import os
import pygame
from pygame.locals import *
import random

BASE_DIR = os.path.dirname(__file__)
IMG_DIR = os.path.join(BASE_DIR, "imagenes")

SCREEN_W, SCREEN_H = 960, 640


# ---------------------------------------------------------
# CARGA DE IMÁGENES SEGÚN "nombre" de la carta
# ---------------------------------------------------------
def load_champion_image(nombre):
    path = os.path.join(IMG_DIR, f"{nombre}.png")

    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(img, (100, 100))
    else:
        # Placeholder si no existe imagen
        surf = pygame.Surface((100,100))
        surf.fill((220,220,220))
        pygame.draw.rect(surf, (60,60,60), surf.get_rect(), 4)

        f = pygame.font.SysFont(None, 24)
        txt = f.render(nombre, True, (30,30,30))
        surf.blit(txt, (50 - txt.get_width()//2, 50 - txt.get_height()//2))

        return surf


# ---------------------------------------------------------
# CRÉDITOS
# ---------------------------------------------------------
def show_credits(screen, font):
    clock = pygame.time.Clock()
    running = True
    lines = [
        "Generala Temática - League of Legends",
        "Trabajo Práctico Programación I",
        "Realizado por: Romero Santiago y Zalazar Nestor",
        "",
        "Presioná ESC para volver"
    ]

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        screen.fill((15,15,40))

        y = 120
        for l in lines:
            t = font.render(l, True, (230,230,230))
            screen.blit(t, (60, y))
            y += 40

        pygame.display.flip()
        clock.tick(30)


# ---------------------------------------------------------
# JUEGO PRINCIPAL
# ---------------------------------------------------------
def run_game(screen, clock, font, tirar_dados_fn, calcular_jugada_fn, guardar_score_fn):

    # 10 turnos, igual que en consola
    turnos_restantes = 10
    puntos_totales = 0

    # dados del turno actual
    dados = tirar_dados_fn()
    guardados = [False] * 5
    tiros_restantes = 3

    nombre_jugador = "Jugador"

    running = True
    while running:

        # EVENTOS
        for event in pygame.event.get():
            if event.type == QUIT:
                return

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

                # TIRAR
                if event.key == K_SPACE and tiros_restantes > 0:
                    for i in range(5):
                        if not guardados[i]:
                            dados[i] = random.choice(dados)  # tira uno nuevo según tus reglas
                    tiros_restantes -= 1

            elif event.type == MOUSEBUTTONDOWN:
                mx,my = event.pos

                # CLIC EN DADOS
                start_x = 80
                y = 230

                for i in range(5):
                    rect = pygame.Rect(start_x + i*140, y, 100, 100)
                    if rect.collidepoint(mx,my):
                        guardados[i] = not guardados[i]

                # BOTÓN TIRAR
                btn = pygame.Rect(780, 230, 150, 50)
                if btn.collidepoint(mx,my) and tiros_restantes > 0:
                    for i in range(5):
                        if not guardados[i]:
                            dados[i] = random.choice(dados)
                    tiros_restantes -= 1

                # BOTÓN ANOTAR CATEGORÍA
                cat_box = pygame.Rect(780, 310, 150, 50)
                if cat_box.collidepoint(mx,my) and tiros_restantes < 3:
                    # Pedimos categoría por teclado tradicional
                    categoria = input("Categoría: ")
                    puntos = calcular_jugada_fn(dados, categoria)
                    puntos_totales += puntos

                    # pasar al siguiente turno
                    turnos_restantes -= 1
                    if turnos_restantes == 0:
                        nombre = input("Nombre: ")
                        guardar_score_fn(nombre, puntos_totales)
                        return

                    # reiniciar turno
                    dados = tirar_dados_fn()
                    guardados = [False] * 5
                    tiros_restantes = 3

        # -------------------------------------------------------------
        # DIBUJADO
        # -------------------------------------------------------------
        screen.fill((25,35,55))

        # HUD
        t = font.render(f"Puntos Totales: {puntos_totales}", True, (255,255,255))
        screen.blit(t, (50, 40))

        t2 = font.render(f"Turnos restantes: {turnos_restantes}", True, (255,255,255))
        screen.blit(t2, (50, 80))

        # DADOS
        start_x = 80
        y = 230
        for i,d in enumerate(dados):
            img = load_champion_image(d["nombre"])
            screen.blit(img, (start_x + i*140, y))

            # marco si está guardado
            if guardados[i]:
                pygame.draw.rect(screen, (255,215,0), (start_x + i*140, y, 100, 100), 4)

        # BOTÓN TIRAR
        btn = pygame.Rect(780, 230, 150, 50)
        pygame.draw.rect(screen, (70,120,180), btn)
        t = font.render(f"Tirar ({tiros_restantes})", True, (255,255,255))
        screen.blit(t, (btn.x + 15, btn.y + 10))

        # BOTÓN ANOTAR
        cat = pygame.Rect(780, 310, 150, 50)
        pygame.draw.rect(screen, (180,70,70), cat)
        lab = font.render("Anotar", True, (255,255,255))
        screen.blit(lab, (cat.x + 30, cat.y + 10))

        pygame.display.flip()
        clock.tick(30)