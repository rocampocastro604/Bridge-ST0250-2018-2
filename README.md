# Integrantes del Equipo
Diego Fernando Martinez Osorio
(algo)
(algo)

# Patron de Diseño: Bridge
Este patrón de diseño permite desacoplar una abstracción de su implementación, de manera que ambas puedan variar de forma independiente.

# Modelo de Clases


## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

Bob-->Alice: Checking with John...
Alice->John: Yes... John, how are you?
```

And this will produce a flow chart:

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


