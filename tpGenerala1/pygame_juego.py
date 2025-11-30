import os
import pygame
import random
from pygame.locals import *
from datos import cartas

SCREEN_W, SCREEN_H = 960, 640

#colores
BG = (28, 39, 54)
PANEL = (18, 24, 34)
GOLD = (235, 190, 70)
GOLD_DARK = (180, 145, 55)
BTN_BLUE = (80, 140, 195)
BTN_RED = (185, 90, 85)
WHITE = (230,230,230)
GRAY = (200,200,200)

FPS = 60


def load_image_for(name):
    path = f"assets/{name}.png"
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(img, (100,100))
    surf = pygame.Surface((100, 100), pygame.SRCALPHA)
    surf.fill((240,240,240))
    pygame.draw.rect(surf, (70,70,70), surf.get_rect(), 3, border_radius=8)
    f = pygame.font.SysFont(None, 18)
    txt = f.render(name, True, (40,40,40))
    surf.blit(txt, (50 - txt.get_width()//2, 50 - txt.get_height()//2))
    return surf


def input_name_modal(screen, clock, font):
    active = True
    name = ""
    prompt = font.render("Ingresa tu nombre y presiona ENTER", True, WHITE)
    rect = pygame.Rect(SCREEN_W//2 - 220, SCREEN_H//2 - 40, 440, 80)
    caret_timer = 0

    while active:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                return "Jugador"
            if ev.type == KEYDOWN:
                if ev.key == K_RETURN:
                    return name.strip() or "Jugador"
                elif ev.key == K_BACKSPACE:
                    name = name[:-1]
                else:
                    if ev.unicode.isprintable() and len(name) < 20:
                        name += ev.unicode

        caret_timer = (caret_timer + 1) % FPS
        screen.fill(BG)

        title = font.render("Generala Temática - Ingresar Nombre", True, GOLD)
        screen.blit(title, (SCREEN_W//2 - title.get_width()//2, 80))

        pygame.draw.rect(screen, PANEL, rect, border_radius=10)
        pygame.draw.rect(screen, GOLD_DARK, rect, 3, border_radius=10)

        screen.blit(prompt, (rect.x + 12, rect.y + 8))
        name_surf = font.render(name, True, WHITE)
        screen.blit(name_surf, (rect.x + 16, rect.y + 36))

        if (caret_timer // (FPS//2)) % 2 == 0:
            cx = rect.x + 16 + name_surf.get_width() + 2
            cy = rect.y + 36
            pygame.draw.line(screen, GOLD, (cx, cy), (cx, cy + name_surf.get_height()), 2)

        pygame.display.flip()
        clock.tick(FPS)


def draw_button(screen, font, rect, text, mouse_pos, mouse_pressed, col, hover, text_color=WHITE):
    is_hover = rect.collidepoint(mouse_pos)
    color = hover if is_hover else col
    pygame.draw.rect(screen, color, rect, border_radius=8)
    pygame.draw.rect(screen, GOLD_DARK, rect, 2, border_radius=8)
    txt = font.render(text, True, text_color)
    screen.blit(txt, (rect.x + (rect.w - txt.get_width())//2,rect.y + (rect.h - txt.get_height())//2))
    return is_hover and mouse_pressed[0]


def verificar_categoria_valida(dados, categoria):
    valores = [d["puntos"] for d in dados]
    counts = [valores.count(v) for v in set(valores)]
    cat = categoria.lower()
    if cat == "generala": return 5 in counts
    if cat in ("poker","póker"): return max(counts) >= 4
    if cat == "full": return sorted(counts) == [2,3]
    if cat == "escalera": return sorted(valores) in ([1,2,3,4,5],[2,3,4,5,6])
    if cat.endswith("s") and cat[:-1].isdigit(): return True
    return False


def show_credits(screen, font):
    running = True
    clock = pygame.time.Clock()
    while running:
        for ev in pygame.event.get():
            if ev.type == QUIT: return
            if ev.type == KEYDOWN and ev.key == K_ESCAPE: running = False

        screen.fill(BG)
        y = 120
        lines = [
            "Generala Temática - League Style",
            "Autor: Néstor Zalazar y Santiago Romero",
            "",
            "Presiona ESC para volver"
        ]
        for l in lines:
            txt = font.render(l, True, WHITE)
            screen.blit(txt, (60, y))
            y += 36
        pygame.display.flip()
        clock.tick(FPS)


def show_stats(screen, font, top_n_fn):
    running = True
    clock = pygame.time.Clock()

    while running:
        for ev in pygame.event.get():
            if ev.type == QUIT: return
            if ev.type == KEYDOWN and ev.key == K_ESCAPE: running = False

        screen.fill(BG)
        title = font.render("Top 10 Puntajes", True, GOLD)
        screen.blit(title, (SCREEN_W//2 - title.get_width()//2, 40))

        top = top_n_fn(10)
        y = 120
        for i,(n,p) in enumerate(top):
            line = font.render(f"{i+1}. {n} - {p}", True, WHITE)
            screen.blit(line, (200, y))
            y += 30

        esc = font.render("ESC para volver", True, GRAY)
        screen.blit(esc, (SCREEN_W//2 - esc.get_width()//2, SCREEN_H - 60))

        pygame.display.flip()
        clock.tick(FPS)


def obtener_carta_por_puntaje(puntaje: int): 
    for carta in cartas: 
        if carta["puntos"] == puntaje: 
            return carta
    return None 

def pintar_puntaje(val, inner, fuente_num_peq, pantalla):
    carta = obtener_carta_por_puntaje(val)
    if carta is None:
        puntos = val
    else:
        puntos = carta.get("puntos", val)
    
    num_peq = fuente_num_peq.render(str(puntos) if puntos > 0 else "?", True, WHITE)
    num_peq_x = inner.x + inner.width - num_peq.get_width() - 8
    num_peq_y = inner.y + 6
    pantalla.blit(num_peq, (num_peq_x, num_peq_y))

def pintar_cartas(dados, screen, estado_juego, botones, guardados=None):
    DADO_W, DADO_H = 100, 140
    espacio = 12
    total_w = DADO_W * len(dados) + espacio * (len(dados) - 1)
    start_x = (1000 - total_w) // 2
    y = 70
    SMOOTHING = 0.25
    HOVER_TARGET = 1.2
    fuente_nombre = pygame.font.Font(None, 24)
    fuente_num_peq = pygame.font.Font(None, 28)

    if guardados is None:
        guardados = []

    scales = estado_juego.get("hover_scales")
    if not isinstance(scales, list) or len(scales) != len(dados):
        scales = [1.0] * len(dados)

    mx, my = pygame.mouse.get_pos()
    hand_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
    arrow_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
    esta_el_cursor_encima = False

    botones.clear()
    for i, val in enumerate(dados):
        carta = obtener_carta_por_puntaje(val["puntos"]) 
        if carta is None:
            continue

        x = start_x + i * (DADO_W + espacio)
        rect = pygame.Rect(x, y, DADO_W, DADO_H)
        pygame.draw.rect(screen, (0, 0, 0), rect, border_radius=12)
        inner = rect.inflate(-6, -6)

        if i < len(guardados) and guardados[i]:
            pygame.draw.rect(screen, GOLD, rect, 3, border_radius=12)

        imagen_path = carta.get("imagen")
        if imagen_path:
            if os.path.exists(imagen_path):
                surf = pygame.image.load(imagen_path).convert_alpha()
            else:
                surf = load_image_for(carta["nombre"])

        if inner.collidepoint(mx, my):
            target = HOVER_TARGET
            esta_el_cursor_encima = True
        else:
            target = 1.0
        new_scale = scales[i] + (target - scales[i]) * SMOOTHING
        scales[i] = new_scale

        new_w = max(1, int(inner.width * new_scale))
        new_h = max(1, int(inner.height * new_scale))
        fondo_carta = pygame.transform.smoothscale(surf, (new_w, new_h))
        clip_surf = pygame.Surface(inner.size, pygame.SRCALPHA)
        offset_x = (inner.width - new_w) // 2
        offset_y = (inner.height - new_h) // 2
        clip_surf.blit(fondo_carta, (offset_x, offset_y))
        screen.blit(clip_surf, inner.topleft)

        pintar_puntaje(val["puntos"], inner, fuente_num_peq, screen)

        nombre = carta["nombre"]
        nombre_txt = fuente_nombre.render(nombre, True, WHITE)
        FLAG_H = 34
        FLAG_COLOR = (10, 90, 220)
        flag_rect = pygame.Rect(inner.x, inner.y + inner.height - FLAG_H, inner.width, FLAG_H)
        pygame.draw.rect(screen, FLAG_COLOR, flag_rect, border_radius=8)
        nombre_x = inner.x + 8
        nombre_y = flag_rect.y + (FLAG_H - nombre_txt.get_height()) // 2
        screen.blit(nombre_txt, (nombre_x, nombre_y))

        botones.append({"accion": f"lock_{i}", "rect": rect})

    estado_juego["hover_scales"] = scales
    if esta_el_cursor_encima:
        pygame.mouse.set_cursor(hand_cursor)
    else:
        pygame.mouse.set_cursor(arrow_cursor)

# ============================
#        GAME FINAL
# ============================
def run_game(screen, clock, font, tirar_dados_fn, calcular_jugada_fn, guardar_fn):

    player_name = input_name_modal(screen, clock, font)

    categorias = ['Generala','Póker','Full','Escalera','1s','2s','3s','4s','5s','6s']
    planilla = {c: None for c in categorias}

    puntos_totales = 0
    turno = 0

    while turno < 10:

        dados = tirar_dados_fn()
        guardados = [False]*5
        tiros = 3
        rolling = False
        frames = 0

        estado_juego = {}          #estado para pintar_cartas (hover scales, etc)
        running_turn = True
        while running_turn:

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            #animacion
            if rolling and frames > 0:
                for i in range(5):
                    if not guardados[i]:
                        #tirar dados
                        dados[i] = random.choice(tirar_dados_fn())
                frames -= 1
                if frames == 0:
                    tiros -= 1
                    rolling = False

            #draw
            screen.fill(BG)

            header = font.render(f"Turno {turno+1} - Puntos: {puntos_totales}", True, GOLD)
            screen.blit(header, (40,40))

            #pinta cartas
            botones = []
            pintar_cartas(dados, screen, estado_juego, botones, guardados)

            #planilla izquierda
            p_x = 40
            p_y = 290
            panel_h = 330
            pygame.draw.rect(screen, PANEL, (p_x - 10, p_y - 10, 260, panel_h), border_radius=12)

            for idx,c in enumerate(planilla.keys()):
                r = pygame.Rect(p_x, p_y + idx*32, 220, 28)
                pygame.draw.rect(screen, PANEL, r, border_radius=6)
                pygame.draw.rect(screen, GOLD_DARK, r, 2, border_radius=6)
                val = planilla[c]
                t = f"{c}: {'-' if val is None else val}"
                screen.blit(font.render(t, True, WHITE), (r.x + 10, r.y + 4))

            #buttons
            btn_tirar = pygame.Rect(SCREEN_W - 200, 420, 140, 48)
            btn_anotar = pygame.Rect(SCREEN_W - 200, 480, 140, 48)

            draw_button(screen, font, btn_tirar, f"Tirar ({tiros})", mouse_pos, mouse_pressed,
                        BTN_BLUE, (min(255,BTN_BLUE[0]+20), min(255,BTN_BLUE[1]+20), min(255,BTN_BLUE[2]+20)))

            draw_button(screen, font, btn_anotar, "Anotar", mouse_pos, mouse_pressed,
                        BTN_RED, (min(255,BTN_RED[0]+20), min(255,BTN_RED[1]+20), min(255,BTN_RED[2]+20)))

            pygame.display.flip()
            clock.tick(FPS)

            #eventos, procesa dsp de clickear
            for ev in pygame.event.get():
                if ev.type == QUIT: return
                if ev.type == KEYDOWN and ev.key == K_ESCAPE: return

                if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                    mx,my = ev.pos

                    #click en dados
                    for b in botones:
                        if b["rect"].collidepoint(mx,my):
                            if b["accion"].startswith("lock_"):
                                parts = b["accion"].split("_", 1)
                                if len(parts) == 2 and parts[1].isdigit():
                                    idx = int(parts[1])
                                    if 0 <= idx < len(guardados):
                                        guardados[idx] = not guardados[idx]

                    #botones de tirar y anoitar
                    if btn_tirar.collidepoint(mx,my) and tiros > 0:
                        rolling = True
                        frames = 10

                    if btn_anotar.collidepoint(mx,my) and tiros < 3:
                        disp = [c for c in categorias if planilla[c] is None]
                        if disp:
                            sel = disp[0]
                            pts = calcular_jugada_fn(dados, sel)
                            if not verificar_categoria_valida(dados, sel):
                                if sel.lower() in ["generala","poker","póker","full","escalera"]:
                                    pts = 0
                            planilla[sel] = pts
                            puntos_totales += pts
                            running_turn = False

                    #click en planilla
                    for idx,c in enumerate(planilla.keys()):
                        slot = pygame.Rect(p_x, p_y + idx*32, 220, 28)
                        if slot.collidepoint(mx,my) and planilla[c] is None:
                            pts = calcular_jugada_fn(dados, c)
                            if not verificar_categoria_valida(dados, c):
                                if c.lower() in ["generala","poker","póker","full","escalera"]:
                                    pts = 0
                            planilla[c] = pts
                            puntos_totales += pts
                            running_turn = False

        turno += 1

    guardar_fn(player_name, puntos_totales)
    return