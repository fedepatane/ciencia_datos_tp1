import scipy.stats as sp
import numpy as np 
import operator 
#from funciones import *

def test1(d1, d2):

	"""
	Premisa = Los atletas son mas lentos en dias de lluvia que en dias
	soleados. 
	Osea queremos ver que d2 tiene una media mayor que d. 
	Para eso tenemos que usar un test de una cola. 
	H0 = Las muestras provienen de distribuciones de igual media
	H1 = La distribuion de d2 tiene media mayor que la distribucion d1
	Vamos a usar el test de scipy.stats.mannwhitneyu
	"""
	np.random.shuffle(d1)
	np.random.shuffle(d2)
	f = sp.mannwhitneyu(d1, d2, alternative='less')
	return f[0] , f[1] 

def test3(d1, d2, d3):
	"""
		H0 = Las distribuciones son independientes. 
	"""
	soleado = {}
	nublado = {}
	lluvioso = {}
	i = 1
	for t in d1 : 
		soleado[i] = t
		i = i + 1
	i = 1
	for t in d2 : 
		nublado[i] = t
		i = i + 1	
	i = 1
	for t in d3 : 
		lluvioso[i] = t
		i = i + 1



	sorted_soleado = sorted(soleado.items(), key=operator.itemgetter(1))
	sorted_nublado = sorted(nublado.items(), key=operator.itemgetter(1))
	sorted_lluvioso = sorted(lluvioso.items(), key=operator.itemgetter(1))
	i = 0 
	while i <= len(sorted_lluvioso) - 1 : 
		print str(sorted_soleado[i][0]) + " , " + str(sorted_nublado[i][0]) + " , " + str(sorted_lluvioso[i][0])
		i = i + 1
	print "------------------------------------------------------"
	return 1 , 1 
	#return f[0] , f[1]


def test4(d1, d2, d3):
	#HACERRRRRRRRRRR
	return 1 , 1 
def ejercicio3(data):
	
	soleado = data[:, 0]
	nublado = data[:, 1]
	lluvioso = data[:, 2] 
	media1 = np.mean(soleado)
	media2 =  np.mean(nublado)
	media3 =  np.mean(lluvioso)
	# media1 y media2 son iguales 

	#estadistico , pvalor = test1(soleado, lluvioso)
	#print estadistico , '%.10f' % pvalor

	#estadistico , pvalor = test2(nublado, soleado)
	#print estadistico , '%.10f' % pvalor

	estadistico , pvalor = test3(soleado, nublado, lluvioso)
	print estadistico , '%.10f' % pvalor
	
	#test4(soleado, nublado, lluvioso)
	#print estadistico , '%.10f' % pvalor

	#estadistico , pvalor = test5(lluvioso, soleado)
	#print estadistico , '%.10f' % pvalor
