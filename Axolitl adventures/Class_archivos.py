import pygame
import json

class Archivo:
    def __init__(self):
        pass

    def actualizar_high_score(dick_vars:dict):
        """Actualiza el high score en el archivo CSV

        Args:
            dick_vars (dict): Diccionario de variables
        """
        try:
            with open(Archivo.get_path_actual("high_score.csv"), "r") as archivo:
                contenido = archivo.read()
        except:
            contenido = "0,0"
        contenido.strip("\n")
        contenidos = contenido.split(",")
        score_archivo = int(contenidos[0])
        waves_archivo = int(contenidos[1])
        
        if dick_vars["score"] > score_archivo:
            dick_vars["high_score"] = dick_vars["score"]
        else:
            dick_vars["high_score"] = score_archivo
        
        if dick_vars["waves"] > waves_archivo:
            dick_vars["high_waves"] = dick_vars["waves"]
        else:
            dick_vars["high_waves"] = waves_archivo

        with open(Archivo.get_path_actual("high_score.csv"), "w") as archivo:
            archivo.write(f"{dick_vars["high_score"]},{dick_vars["high_waves"]}")
        
    def get_path_actual(nombre_archivo:str)->str:
        """Devuelve el directorio actual

            Args:
                nombre_archivo (str): el nombre del archivo

            Returns:
                str: el directorio actual
            """
        if type(nombre_archivo) is not str:
            raise TypeError("El nombre del archivo no es de tipo str")
        import os
        directorio_actual = os.path.dirname(__file__)
        return os.path.join(directorio_actual, nombre_archivo)
    

    def cargar_un_json(ruta_archivo:str)->dict:
        """carga un archivo json

        Args:
            ruta_archivo (str): Es la ruta del archivo

        Returns:
            dict: Contenido del archivo json
        """
        if type(ruta_archivo) is not str:
            raise TypeError("La ruta no es de tipo str")
        with open(ruta_archivo) as archivo:
            dick_config = json.load(archivo)
        return dick_config

        