def getMaximo(listaInteiros):
	max = listaInteiros[0]
	for elemento in listaInteiros:
		if elemento > max:
			max = elemento
	return max

def getMinimo(listaInteiros):
	min = listaInteiros[0]
	for elemento in listaInteiros:
		if elemento < min:
			min = elemento
	return min