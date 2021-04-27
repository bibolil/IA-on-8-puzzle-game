class File:

	def __init__(self):
		self.valeurs = []

	def enfiler(self, valeur):
		self.valeurs.append(valeur)

	def defiler(self):
		if self.valeurs:
			return self.valeurs.pop(0)

	def estVide(self):
		return self.valeurs == []

	
	def longueur(self):
		return len(self.valeurs)
