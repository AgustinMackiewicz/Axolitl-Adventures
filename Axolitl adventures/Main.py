import pygame
from Class_jugador import Player
from Class_event_handler import EventHandler
from Class_Graficos import Graficos
from Class_bala import Bala
from Class_enemies import Enemigo
from Class_bala_enemigo import Bala_enemigo
from Class_archivos import Archivo

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Axolitl adventures")
pantalla = pygame.display.set_mode((800, 600))
dick_config = Archivo.cargar_un_json(Archivo.get_path_actual("config.json"))
dick_vars = {
    "running" : True,

    "boton_jugar" : None,
    "boton_mutear" : None,

    "jugador" : None,

    "lista_balas" : [],

    "game_state" : 0,

    "mute" : False,
    "intro" : pygame.mixer.Sound("Assets/Music/Intro.mp3"),
    "game_over" : pygame.mixer.Sound("Assets/Music/Game Over.mp3"),
    "disparo" : pygame.mixer.Sound("Assets/Music/Disparo.mp3"),
    "gameplay" : pygame.mixer.Sound("Assets/Music/Game Music.mp3"),
    "logo_img" : dick_config["logo_img"],
    "mute_img" : dick_config["mute_img"],
    "fuente" : pygame.font.Font("Assets/Graficos/Sans.ttf", 30),
    "bala_img" : dick_config["bala_img"],
    "score" : 0,
    "jugador_img": dick_config["jugador_img"],
    "vida" : 3,
    "enemigo_img" : dick_config["enemigo_img"],
    "power_ups" : 0,
    "powerup_img" : dick_config["powerup_img"],
    "high_score" : 0,
    "high_waves" : 0,
    "bala_enemigo_img" : dick_config["bala_enemigo_img"],
    "corazon_amado_img" : dick_config["corazon_amado_img"],
    "corazon_vacio_img" : dick_config["corazon_vacio_img"],
    
    "waves" : 0,
    "lista_enemigos" : [],
    "lista_balas_enemigo" : [],

    "lista_balas_rect": [],
    "lista_enemigos_rect": [],
    "lista_balas_enemigo_rect": [],
    "lista_powerups" : [],
    "lista_powerups_rect" : [],
}

dick_vars["jugador"] = Player(0, 380, dick_vars)
dick_vars["intro"].set_volume(0.08)
dick_vars["disparo"].set_volume(0.5)
dick_vars["gameplay"].set_volume(0.04)
dick_vars["game_over"].set_volume(0.05)
dick_vars["intro"].play(-1)
while dick_vars["running"]:
    EventHandler(dick_vars, pygame.event.get())
    pantalla.blit(pygame.image.load(dick_config["fondo_img"]), (0, 0))
    if dick_vars["game_state"] == 0:
        dick_vars["boton_jugar"] = pygame.draw.rect(pantalla, (0, 255, 255), (300, 300, 200, 70))
        Graficos.render_fuente( "Jugar", dick_vars["fuente"], (0, 0, 0), pantalla, (356, 315))
        pantalla.blit(pygame.image.load(dick_config["logo_img"]), (254, 75))
        dick_vars["boton_mutear"] = pygame.draw.rect(pantalla, (0, 255, 255), (700, 25, 70, 70))
        pantalla.blit(pygame.image.load(dick_config["mute_img"]), (700, 25))
    elif dick_vars["game_state"] == 1:
        Graficos.dibujar_lista_balas(dick_vars["lista_balas"], pantalla, dick_vars)
        Graficos.calcular_rects(dick_vars)
        Graficos.dibujar_jugador(dick_vars["jugador"], pantalla, dick_vars)
        Graficos.dibujar_vida(dick_vars, pantalla)
        Graficos.dibujar_lista_enemigos(dick_vars["lista_enemigos"], pantalla, dick_vars)
        Graficos.dibujar_lista_balas_enemigos(dick_vars["lista_balas_enemigo"], pantalla, dick_vars)
        Graficos.dibujar_lista_powerups(dick_vars["lista_powerups"], pantalla, dick_vars)
        Graficos.render_fuente( f"{dick_vars["score"]}", dick_vars["fuente"], (0, 0, 0), pantalla, (400, 30))
        Graficos.chequear_cantidad_enemigos(dick_vars)
    elif dick_vars["game_state"] == 2:
        pygame.draw.rect(pantalla, (0, 0, 0), (0, 0, 800, 600))
        dick_vars["boton_jugar"] = pygame.draw.rect(pantalla, (0, 255, 255), (275, 300, 250, 70))
        Graficos.render_fuente( "Jugar de nuevo?", dick_vars["fuente"], (0, 0, 0), pantalla, (282, 315))
        Graficos.render_fuente( "Game Over", dick_vars["fuente"], (255, 0, 0), pantalla, (325, 75))
        Graficos.render_fuente( f"high score: {dick_vars["high_score"]}", dick_vars["fuente"], (255, 0, 0), pantalla, (315, 100))
        Graficos.render_fuente( f"high score wave: {dick_vars["high_waves"]}", dick_vars["fuente"], (255, 0, 0), pantalla, (285, 125))
        


    pygame.display.update()
    clock.tick(30)
    

pygame.mixer.quit()
pygame.quit()