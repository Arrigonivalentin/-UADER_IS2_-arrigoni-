# Componente base
class Componente:
    def mostrar(self, nivel=0):
        raise NotImplementedError("Debe implementar el método mostrar()")

# Hoja 
class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Pieza: {self.nombre}")

# Compuesto
class SubConjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente: Componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"+ SubConjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

# Producto principal
class Producto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.subconjuntos = []

    def agregar(self, subconjunto: SubConjunto):
        self.subconjuntos.append(subconjunto)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"* Producto: {self.nombre}")
        for subconjunto in self.subconjuntos:
            subconjunto.mostrar(nivel + 1)

# Construcción del ensamblado
def construir_ensamblado():
    producto = Producto("Máquina X")

    # Crear tres subconjuntos iniciales con 4 piezas cada uno
    for i in range(1, 4):
        subconjunto = SubConjunto(f"SubConjunto_{i}")
        for j in range(1, 5):
            subconjunto.agregar(Pieza(f"Pieza_{i}.{j}"))
        producto.agregar(subconjunto)

    # Mostrar ensamblado inicial
    print("=== Ensamblado Inicial ===")
    producto.mostrar()

    # Agregar subconjunto opcional
    subconjunto_opcional = SubConjunto("SubConjunto_Extra")
    for k in range(1, 5):
        subconjunto_opcional.agregar(Pieza(f"Pieza_Extra.{k}"))
    producto.agregar(subconjunto_opcional)

    # Mostrar ensamblado actualizado
    print("\n=== Ensamblado con Subconjunto Opcional ===")
    producto.mostrar()

# Ejecutar ejemplo
if __name__ == "__main__":
    construir_ensamblado()
