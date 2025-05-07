# Componente base
class Numero:
    def imprimir(self):
        raise NotImplementedError("Debe implementar imprimir()")

# Componente concreto
class NumeroBase(Numero):
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        return self.valor

# Decorador base
class Operacion(Numero):
    def __init__(self, componente: Numero):
        self.componente = componente

# Decoradores concretos
class SumarDos(Operacion):
    def imprimir(self):
        return self.componente.imprimir() + 2

class MultiplicarPorDos(Operacion):
    def imprimir(self):
        return self.componente.imprimir() * 2

class DividirPorTres(Operacion):
    def imprimir(self):
        return self.componente.imprimir() / 3

# Ejemplo de uso
if __name__ == "__main__":
    base = NumeroBase(9)
    print("Número base:", base.imprimir())

    # Sumar 2
    suma = SumarDos(base)
    print("Después de sumar 2:", suma.imprimir())

    # Multiplicar por 2 después de sumar 2
    multiplicado = MultiplicarPorDos(suma)
    print("Después de sumar 2 y multiplicar por 2:", multiplicado.imprimir())

    # Dividir por 3 después de las dos operaciones anteriores
    dividido = DividirPorTres(multiplicado)
    print("Después de sumar 2, multiplicar por 2 y dividir por 3:", dividido.imprimir())

    resultado_final = DividirPorTres(MultiplicarPorDos(SumarDos(NumeroBase(9))))
    print("Encadenado directamente:", resultado_final.imprimir())
