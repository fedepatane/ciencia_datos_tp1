import scipy.stats as sp
import numpy as np 

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
	f = sp.mannwhitneyu(d1, d2, alternative='greater')
	return f[0] , f[1] 

def test2(d1, d2):
	"""
	ni idea hay que preguntarlo , pero me parece que hay que buscar que tengan
	la misma media y ver que no la tienen ?? 
	"""

	return 1 , 1
def test3(d1, d2):
	"""
		H0 = La velocidad en dias de lluvia es independiente del atleta
		Esto significa que por ejemplo, las variables de lluvia y la de nublado son 
		independientes. Test de dos colas por su hipotesis alternativa
		Test a usar : ttest_ind
	"""
	f = sp.ttest_ind(d1,d2)
	return f[0] , f[1]




def test4(d1, d2):

	"""
	Premisa = El tiempo influye en la velocidad de los atletas.
	Osea queremos ver que d1 tiene una media distinta que d2. 
	Para eso tenemos que usar un test de dos colas
	H0 = Las muestras provienen de distribuciones de igual media
	H1 = La distribuion de d2 tiene media distinta que la distribucion d1
	Vamos a usar el test de muestras apareadas. 
	ttest_rel
	"""
	f = sp.ttest_rel(d1, d2)
	return f[0] , f[1] 



def ejercicio3(data):
	
	soleado = data[:, 0] 
	nublado = data[:, 1]
	lluvioso = data[:, 2] 
	media1 = np.mean(soleado)
	media2 =  np.mean(nublado)
	media3 =  np.mean(lluvioso)
	# media1 y media2 son iguales 

	estadistico , pvalor = test1(soleado, lluvioso)
	print estadistico , '%.10f' % pvalor

	estadistico , pvalor = test2(soleado, nublado)
	print estadistico , '%.10f' % pvalor


	estadistico , pvalor = test3(soleado, lluvioso)
	print estadistico , '%.10f' % pvalor


	estadistico , pvalor = test4(nublado, lluvioso)
	print estadistico , '%.10f' % pvalor
