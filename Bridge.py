from abc import ABC, abstractmethod


class figura(ABC):
	def __init__(self, printer):
		self.printer = printer

	@abstractmethod
	def existir(self):
		pass

class cuadrado(figura):
	def existir(self):
		print("Hola soy un Cuadrado de color")
		self.printer.pintar()

class circulo(figura):
	def existir(self):
		print("Hola soy un Circulo de color")
		self.printer.pintar()





class printer(ABC):
	@abstractmethod
	def pintar(self):
		pass

class rojo(printer):
	def pintar(self):
		print("Rojo")

class verde(printer):
	def pintar(self):
		print("Verde")



def main():
	a = cuadrado(rojo())
	a.existir()

	b = cuadrado(verde())
	b.existir()

	c = circulo(rojo())
	c.existir()

	d = circulo(verde())
	d.existir()


if __name__ == '__main__':
	main()