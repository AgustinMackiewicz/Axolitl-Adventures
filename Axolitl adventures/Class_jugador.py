import pygame
from Class_bala import Bala
from Class_archivos import Archivo

class Player:
    def __init__(self, x, y, dick_vars:dict):
        self.image = pygame.image.load(dick_vars["jugador_img"])
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vida = 3
        self.cooldown = 0
        
    

    def mover(self, direccion):
        """Mueve al jugador en la dirección indicada con limites

        Args:
            direccion (str): Dirección en la que se mueve el jugador
        """
        match direccion:
            case "arriba":
                self.y -= 8
                if self.y < 0:
                    self.y = 0
            case "abajo":
                self.y += 8
                if self.y > 600 - self.rect.height:
                    self.y = 600 - self.rect.height
            case "izquierda":
                self.x -= 8
                if self.x < 0:
                    self.x = 0
            case "derecha":
                self.x += 8
                if self.x > 300 - self.rect.width:
                    self.x = 300 - self.rect.width

    def dibujar(self, superficie):
        """Dibuja al jugador sobre la pantalla

        Args:
            superficie (pygame.Surface): Superficie sobre la que se dibuja
        """
        superficie.blit(self.image, (self.x, self.y))
    
    def shootear_bala(self, dick_vars:dict):
        """Chequea si se puede disparar y que cuantas balas se pueden disparar con el nivel de powerups actuales

        Args:
            dick_vars (dict): Diccionario de variables
        """
        power_ups_obtenidos = dick_vars["power_ups"]
        if self.cooldown == 0:
            dick_vars["disparo"].play()
            self.cooldown = 30
            match power_ups_obtenidos:
                case 0:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 6], dick_vars["bala_img"], 1, 10, dick_vars)
                case 1:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], dick_vars["bala_img"], 1, 10, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], dick_vars["bala_img"], 1, 10, dick_vars)
                case 2:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], dick_vars["bala_img"], 2, 10, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], dick_vars["bala_img"], 2, 10, dick_vars)
                case 3:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], dick_vars["bala_img"], 2, 12, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], dick_vars["bala_img"], 2, 12, dick_vars)
                case 4:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], dick_vars["bala_img"], 2, 12, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], dick_vars["bala_img"], 2, 12, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 24], dick_vars["bala_img"], 1, 10, dick_vars)
                case 5:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], dick_vars["bala_img"], 2, 12, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], dick_vars["bala_img"], 2, 12, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 24], dick_vars["bala_img"], 1, 10, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 24], dick_vars["bala_img"], 1, 10, dick_vars)
                case 6:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], dick_vars["bala_img"], 2, 15, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], dick_vars["bala_img"], 2, 15, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 24], dick_vars["bala_img"], 1, 10, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 24], dick_vars["bala_img"], 1, 10, dick_vars)
                case 7:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], dick_vars["bala_img"], 5, 15, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], dick_vars["bala_img"], 5, 15, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 24], dick_vars["bala_img"], 3, 15, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 24], dick_vars["bala_img"], 3, 15, dick_vars)

    
    def bajar_cooldown(self):
        """Baja el cooldown en 1 por frame
        """
        if self.cooldown > 0:
            self.cooldown -= 1
    
    def bajar_vida(self, dick_vars:dict):
        """Baja la vida del jugador y detecta si este muere

        Args:
            dick_vars (dict): Diccionario de variables
        """
        if self.vida > 0:
            self.vida -= 1
            if dick_vars["power_ups"] > 0:
                dick_vars["power_ups"] -= 1
        if self.vida == 0:
            dick_vars["gameplay"].stop()
            dick_vars["game_over"].play(-1)
            dick_vars["game_state"] = 2
            dick_vars["lista_enemigos"] = []
            Archivo.actualizar_high_score(dick_vars)
            dick_vars["waves"] = 0
            dick_vars["lista_balas_enemigo"] = []
            dick_vars["lista_balas"] = []
            dick_vars["score"] = 0
            
            

    
    def aumentar_powerup(self, dick_vars:dict):
        """Aumenta la cantidad de powerups

        Args:
            dick_vars (dict): Diccionario de variables
        """
        if dick_vars["power_ups"] < 7:
            dick_vars["power_ups"] += 1
    
    def chequear_colisiones(self, dick_vars:dict):
        """Chequea las colisiones del jugador con enemigos, balas enemigas y powerups

        Args:
            dick_vars (dict): Diccionario de variables
        """
        try:
            if self.rect.collidelist(dick_vars["lista_balas_enemigo_rect"]) != -1:
                self.bajar_vida(dick_vars)
                dick_vars["lista_balas_enemigo"][self.rect.collidelist(dick_vars["lista_balas_enemigo_rect"])].borrar_bala(dick_vars["lista_balas_enemigo"])
            if self.rect.collidelist(dick_vars["lista_enemigos_rect"]) != -1:
                self.bajar_vida(dick_vars)
                dick_vars["lista_enemigos"][self.rect.collidelist(dick_vars["lista_enemigos_rect"])].borrar_enemigo(dick_vars["lista_enemigos"], dick_vars)
            if self.rect.collidelist(dick_vars["lista_powerups_rect"]) != -1:
                self.aumentar_powerup(dick_vars)
                dick_vars["lista_powerups"][self.rect.collidelist(dick_vars["lista_powerups_rect"])].borrar_powerups(dick_vars["lista_powerups"])
        except:
            pass