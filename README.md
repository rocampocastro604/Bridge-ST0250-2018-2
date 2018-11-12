# Integrantes del Equipo
Diego Fernando Martinez Osorio
(algo)
(algo)

# Patron de Diseño: Bridge
Este patrón de diseño permite desacoplar una abstracción de su implementación, de manera que ambas puedan variar de forma independiente.

# Modelo de Clases
```mermaid
classDiagram
figura<|-- cuadrado
figura<|-- circulo
figura: printer printer
figura: existir()
cuadrado: printer printer
cuadrado: existir()
circulo: printer printer
circulo: existir()
printer<|-- rojo
printer<|-- verde
printer : pintar()
rojo : pintar()
verde : pintar()
figura o-- printer

```

## Lenguaje: Python3


