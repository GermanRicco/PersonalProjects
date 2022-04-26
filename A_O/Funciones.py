def FibraT2_TelaT2(cantidadFibra):
	RecuperacionProduccion = 0.367
	cantTelaT2 = cantidadFibra
	recuperado = int(round((cantidadFibra*RecuperacionProduccion),0))
	while recuperado != 0:
		cantTelaT2 = cantTelaT2+recuperado
		recuperado = int(round((recuperado*RecuperacionProduccion),0))

def FibraT3_TelaT3(cantidadFibra, cantidadTela, costeProducir, fibrasxU):  #COSTE Y FIBRASXU depende de que tela se vaya a hacer
	RecuperacionProduccion = 0.367                                         #puedo ponerlos con un cuadro de doble entrada
	cantTotal=0
	cantTelaMejorada = 0
	utilFibT3 = int(round((cantidadFibra/fibrasxU),0))

	while (utilFibT3 >= 1) and (cantidadTela >= 1):
		if (utilFibT3 >= cantidadTela):
			cantTelaMejorada = cantidadTela
			cantidadTela = int(round((cantidadTela*RecuperacionProduccion),0))
			cantidadFibra = int(round((cantidadFibra*RecuperacionProduccion),0))
			utilFibT3 = (cantidadFibra/fibrasxU)
		else:
			cantTelaMejorada = utilFibT3
			cantidadTela = int(round((cantidadTela*RecuperacionProduccion),0))
			cantidadFibra = int(round((cantidadFibra*RecuperacionProduccion),0))
			utilFibT3 = (cantidadFibra/fibrasxU)

		cantTotal = int(round(cantTotal + cantTelaMejorada))

		print(int(cantTelaMejorada)) ##Prints de prueba

	gastoProduccion = cantTotal*costeProducir

	print('En total podes hacer ' + str(cantTotal) + ' Telas')
	print('Hacerlas te cuesta en total ' + str(gastoProduccion)+ ' de plata')