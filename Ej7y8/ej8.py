from ej7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion
    
    def titular_valido(self):
        edad = self.titular.get_edad()
        return 18 <= edad < 25
    
    def retirar(self, cantidad):
        if self.titular_valido():
            super().retirar(cantidad)
    
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.bonificacion)