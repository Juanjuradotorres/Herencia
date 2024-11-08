# profesores.py
from persona import Persona

class Profesores(Persona):
    def __init__(self):
        super().__init__()
        self._departamento = None
        self._categoria = None
        self._maximo_grado_estudios = None

    # Getters y Setters con validación
    def get_departamento(self):
        if self._departamento is None:
            raise ValueError("El departamento no tiene un valor asignado.")
        return self._departamento

    def set_departamento(self, departamento):
        self._departamento = departamento

    def get_categoria(self):
        if self._categoria is None:
            raise ValueError("La categoría no tiene un valor asignado.")
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_maximo_grado_estudios(self):
        if self._maximo_grado_estudios is None:
            raise ValueError("El máximo grado de estudios no tiene un valor asignado.")
        return self._maximo_grado_estudios

    def set_maximo_grado_estudios(self, maximo_grado_estudios):
        self._maximo_grado_estudios = maximo_grado_estudios

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Departamento: {self._departamento}, Categoría: {self._categoria}, Máximo Grado de Estudios: {self._maximo_grado_estudios}"

