class TrenLaminador:
    def producir(self, lamina):
        raise NotImplementedError("Este método debe ser implementado por una subclase.")


class Tren5mts(TrenLaminador):
    def producir(self, lamina):
        print(f"[Tren5mts] Produciendo lámina de {lamina.espesor}\" x {lamina.ancho}m x 5m")

class Tren10mts(TrenLaminador):
    def producir(self, lamina):
        print(f"[Tren10mts] Produciendo lámina de {lamina.espesor}\" x {lamina.ancho}m x 10m")


class LaminaAcero:
    def __init__(self, tren_laminador: TrenLaminador):
        self.espesor = 0.5  # pulgadas
        self.ancho = 1.5    # metros
        self.tren = tren_laminador

    def producir(self):
        print(f"[LaminaAcero] Enviando a producción con {self.tren.__class__.__name__}")
        self.tren.producir(self)
