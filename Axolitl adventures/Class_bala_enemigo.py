import pygame

class Bala_enemigo:
    def __init__(self, pos, imagen, dick_vars:dict):
        self.imagenes = imagen
        self.pos = pos
        self.index = 0
        self.velocidad = 8
        dick_vars["lista_balas_enemigo"].append(self)
        
        self.imagenes_lista = []
        for i in range(11):
            image = pygame.image.load(f"{self.imagenes}/{i}.png")
            self.imagenes_lista.append(image)

        

    def mover_bala_enemigo(self, dick_vars:dict):
        """Mueve la bala del enemigo y chequea si se va de la pantalla

        Args:
            dick_vars (dict): Diccionario de variables
        """
        self.pos[0] -= self.velocidad
        if self.pos[0] < 0:
            self.borrar_bala(dick_vars["lista_balas_enemigo"])

    def dibujar_bala_enemigo(self, superficie):
        """Dibuja la bala sobre la pantalla

        Args:
            superficie (pygame.Surface): Superficie sobre la que se dibuja
        """
        superficie.blit(self.image, self.pos)
        

    def actualizar_animacion(self):
        """Cambia el index cada frame y la imagen con la correspondiente
        """
        if self.index < 10:
            self.index += 1
        else:
            self.index = 0
            
        self.image = self.imagenes_lista[self.index]
        
    
    def borrar_bala(self, lista_balas_enemigo:dict):
        """Se elimina la bala de la lista de balas

        Args:
            lista_balas_enemigo (dict): Lista de las balas enemigas
        """
        lista_balas_enemigo.remove(self)
        

    