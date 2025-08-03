import heapq

class ColaPrioridad:
	def __init__(self):
		self._cola = []
		self._indice = 0

	def push(self, elemento, prioridad):
		heapq.heappush(self._cola, (-prioridad, self._indice, elemento))
		self._indice += 1

	def pop(self):
		return heapq.heappop(self._cola)[-1]


class Elemento:
	def __init__(self, nombre):
		self.nombre = nombre

	def __repr__(self):
		return '{!r}'.format(self.nombre)