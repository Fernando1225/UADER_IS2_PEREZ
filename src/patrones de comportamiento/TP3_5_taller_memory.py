

import os

class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content

class FileWriterUtility:
	def __init__(self, file):
		self.file = file
		self.content = ""
		self.states = []

	def write(self, string):
		self.content += string

	def save(self):
		if len(self.states) == 4:
			self.states.pop(0)
		self.states.append(Memento(self.file, self.content))

	def undo(self, num_states):
		if num_states > len(self.states):
			num_states = len(self.states)
		for i in range(num_states):
			memento = self.states.pop()
			self.file = memento.file
			self.content = memento.content

class FileWriterCaretaker:
	def save(self, writer):
		writer.save()

	def undo(self, writer, num_states):
		writer.undo(num_states)

if __name__ == '__main__':
	os.system("clear")

	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Más material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Incluso más material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("se invoca al <undo>")
	caretaker.undo(writer, 2)
	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	print("se invoca de nuevo al metodo <undo>")
	caretaker.undo(writer, 1)
	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	print("Nuevamente al metodo <undo>")
	caretaker.undo(writer, 3)
	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	print("Y de nuevo al metodo <undo>")
	caretaker.undo(writer, 0)
	print("Se muestra el estado actual")
	print(writer.content + "\n\n")


