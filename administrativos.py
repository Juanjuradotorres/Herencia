# administrativos.py
from persona import Persona

class Administrativos(Persona):
    def __init__(self):
        super().__init__()
        self._cargo = None
        self._area = None

    # Getters y Setters con validación
    def get_cargo(self):
        if self._cargo is None:
            raise ValueError("El cargo no tiene un valor asignado.")
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_area(self):
        if self._area is None:
            raise ValueError("El área no tiene un valor asignado.")
        return self._area

    def set_area(self, area):
        self._area = area

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Cargo: {self._cargo}, Área: {self._area}"
