import requests
import json
import Funciones

class Item():
	nombre = None
	cantidad = None
	Tier = None
	Nivel = None

	bestCity = None
	bestSellPrice = None
	mayoresganancias = None

	segBestCity = None
	segBestSellPrice = None
	segMayoresGanancias = None

	def __init__(self, nombre, cantidad):
		import operator
		Ciudades = 'Bridgewatch,Caerleon,Fort Sterling,Lymhurst,Martlock,Thetford'
		CantCiudades = 6
		TaxPremium = 0.02
		TaxNormal = 0.06
		AjusteCuota = 0.015
		precios={}
		self.nombre = nombre
		self.cantidad = cantidad
		self.Tier = nombre[1]
		self.Nivel = nombre[-1]
		if (self.Nivel == "R") or (self.Nivel == "H"):
			self.Nivel = "0"
		url = f"https://www.albion-online-data.com/api/v2/stats/prices/{nombre}?locations={Ciudades}&qualities=1"
		r1 = requests.get(url)
		if (r1.status_code==200):
			r1j = r1.json()
			for i in range (CantCiudades):
				ciudad=r1j[i]["city"]
				precio=r1j[i]["sell_price_min"]
				precios.setdefault(ciudad,precio)
			precios_ord = dict(sorted(precios.items(), key=operator.itemgetter(1), reverse=True))
			ListbestPrice = list(precios_ord.values())  #Listas ordenadas con el mejor precio en la posicion 0 
			ListbestCity = list(precios_ord.keys())
			self.bestSellPrice = ListbestPrice[0]
			self.bestCity = ListbestCity[0]
			self.segBestSellPrice = ListbestPrice[1]
			self.segBestCity = ListbestCity[1]
				#Obtencio de ganancias vendiendo en la mejor ciudad
			GananciaBruta = cantidad*ListbestPrice[0]
			GananciaBruta2 = cantidad*ListbestPrice[1]   #ESTO SE PUEDE HACER MAS BONITO, YA DESPUES VEO DE HACERLO FUNCION
			Impuesto = GananciaBruta*TaxNormal
			Impuesto2 = GananciaBruta2*TaxNormal  
			SetupFee = GananciaBruta*AjusteCuota
			SetupFee2 = GananciaBruta2*AjusteCuota
			self.mayoresganancias = int(GananciaBruta-Impuesto-SetupFee)
			self.segMayoresGanancias = int(GananciaBruta2-Impuesto2-SetupFee2)
		else:
			print(f"error {r1.status_code}")

	def imprimir(self):
		print ('nombre: '+ self.nombre)
		print ('cantidad: '+ str(self.cantidad))
		print ('Tier: '+ self.Tier)
		print ('Nivel: '+ self.Nivel)
		print('\n')
		print ('La mejor opcion es vender en: '+ self.bestCity)
		print ('Mejor Precio: '+ str(self.bestSellPrice))
		print ('Ganancias Posibles: '+ str(self.mayoresganancias))
		print ('La segunda opcion es vender en: '+ self.segBestCity)
		print ('Donde se vende a: '+ str(self.segBestSellPrice))
		print ('Y podrias ganar: '+ str(self.segMayoresGanancias))



FibraT4 = Item("T4_CLOTH", 300)

FibraT4.imprimir()