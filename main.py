class Mains:
	def __init__(self):
		self.name = "Ucup"

	def perkalian(self,a,b):
		return a*b

	def nama(self):
		print("aaa")
		# self.query = {"id":"1","nama":"Juber"}
		

class Inheritence(Mains):
	pass

class MakeSuper(Mains):
	def __init__(self):
		super().__init__()
		super().nama()

	def ambil_nama_dari_mains_dengan_super(self):
		super().nama()
		a = "JAJAJA"
		return a

# a = Mains()
# print(a.name)
# print(a.perkalian(2,3))
# inhe = Inheritence()
# print(inhe.perkalian(3,4))
# s = MakeSuper()
# print(s.name)
# print(s.ambil_nama_dari_mains_dengan_super())


class Satu:
	def a(self):
		a = "Method A"
		return a
class Dua:
	def b(self):
		b = "Method B"
		return b

class Ambil(Satu,Dua):
	def cetak(self):
		cecep = {
			"1":self.a(),
			"2":self.b()
		}
		return cecep

# asem = Ambil()
# print(asem.cetak()['1'])


class Pemain:
	def setPemain(self,nama,umur):
		self.nama = nama
		self.umur = umur

class Posisi:
	def setPosisi(self,posisi):
		self.posisi = posisi

class Club(Pemain,Posisi):
	def __init__(self,gaji,kontrak):
		self.gaji = gaji
		self.kontrak = kontrak

	def showData(self):
		data = {
			"Nama":self.nama,
			"Umur":self.umur,
			"Poisi":self.posisi,
			"Gaji":self.gaji,
			"Kontrak":f"{self.kontrak} Years"
		}
		return data

# Kepin = Club(500000000,2)
# Kepin.setPemain('Kepin De Brune',18)
# Kepin.setPosisi("CB")

# print(Kepin.showData())


