import pygame
from Class_enemies import Enemigo

class EventHandler:
    def __init__(self, dick_vars:dict, lista_eventos:list[pygame.event.Event]) -> None:
        for event in lista_eventos:
            match event.type:     
                case pygame.QUIT:  
                    dick_vars["running"] = False
                case pygame.MOUSEBUTTONDOWN:
                    EventHandler.event_mouse_button_down(self, dick_vars, event)
                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        dick_vars["running"] = False
        EventHandler.event_case_key_pressed(self, dick_vars)
                
                
    def event_mouse_button_down(self, dick_vars:dict, evento:pygame.event.Event) -> None:
        """Evento de click y botones de UI

        Args:
            dick_vars (dict): Diccionario de variables
            evento (pygame.event.Event): Evento
        """
        if evento.button == 1:
                if dick_vars["boton_jugar"].collidepoint(evento.pos) and dick_vars["game_state"] == 0 or dick_vars["game_state"] == 2:
                        dick_vars["game_state"] = 1
                        dick_vars["intro"].stop()
                        dick_vars["gameplay"].play(-1)
                        dick_vars["game_over"].stop()
                        dick_vars["vida"] = 3
                        dick_vars["jugador"].vida = 3
                        dick_vars["power_ups"] = 0
                        dick_vars["lista_power_ups"] = []
                        dick_vars["jugador"].x = 0
                        dick_vars["jugador"].y = 380
                if dick_vars["boton_mutear"].collidepoint(evento.pos) and dick_vars["game_state"] == 0:
                    dick_vars["mute"] = not dick_vars["mute"]
                    if not dick_vars["mute"]:
                        dick_vars["intro"].set_volume(0.08)
                        dick_vars["disparo"].set_volume(0.5)
                        dick_vars["gameplay"].set_volume(0.04)
                    else:
                        dick_vars["intro"].set_volume(0)
                        dick_vars["disparo"].set_volume(0)
                        dick_vars["gameplay"].set_volume(0)

        

    def event_case_key_pressed(self, dick_vars:dict) -> None:
        """Evento de tecla mantenida

        Args:
            dick_vars (dict): Diccionario de variables
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dick_vars["jugador"].mover("arriba")
        if keys[pygame.K_s]:
            dick_vars["jugador"].mover("abajo")
        if keys[pygame.K_a]:
            dick_vars["jugador"].mover("izquierda")
        if keys[pygame.K_d]:
            dick_vars["jugador"].mover("derecha")
        if keys[pygame.K_SPACE]:
            dick_vars["jugador"].shootear_bala(dick_vars)
    
    
        

    