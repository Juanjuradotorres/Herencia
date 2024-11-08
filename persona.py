# persona.py
class Persona:
    def __init__(self):
        self._nombre = None
        self._apellido = None
        self._edad = None

    # Getters y Setters con validación
    def get_nombre(self):
        if self._nombre is None:
            raise ValueError("El nombre no tiene un valor asignado.")
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        if self._apellido is None:
            raise ValueError("El apellido no tiene un valor asignado.")
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_edad(self):
        if self._edad is None:
            raise ValueError("La edad no tiene un valor asignado.")
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def mostrar_informacion(self):
        return f"Nombre: {self._nombre} {self._apellido}, Edad: {self._edad}"
