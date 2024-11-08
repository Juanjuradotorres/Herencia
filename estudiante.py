# estudiantes.py
from persona import Persona

class Estudiantes(Persona):
    def __init__(self):
        super().__init__()
        self._matricula = None
        self._carrera = None
        self._semestre = None

    # Getters y Setters con validación
    def get_matricula(self):
        if self._matricula is None:
            raise ValueError("La matrícula no tiene un valor asignado.")
        return self._matricula

    def set_matricula(self, matricula):
        self._matricula = matricula

    def get_carrera(self):
        if self._carrera is None:
            raise ValueError("La carrera no tiene un valor asignado.")
        return self._carrera

    def set_carrera(self, carrera):
        self._carrera = carrera

    def get_semestre(self):
        if self._semestre is None:
            raise ValueError("El semestre no tiene un valor asignado.")
        return self._semestre

    def set_semestre(self, semestre):
        self._semestre = semestre

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Matrícula: {self._matricula}, Carrera: {self._carrera}, Semestre: {self._semestre}"

