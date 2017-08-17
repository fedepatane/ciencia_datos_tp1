import scipy.stats as sp

def test_muestras_apareadas(d1, d2):
	"""
	En este test vamos a probar si las distribuciones d1
	y d2 tienen la misma media. Para eso hay que usar el test de muestras
	apareadas. Esta es la funcion para utilizar scipy.stats.ttest_rel

	Hipotesis nula : Las distribuciones d1 y d2 tienen la misma media.
	
	"""

	f = sp.ttest_rel(d1,d2)
	return f[0] , f[1] 

def test_muestras_independientes(d1, d2):
	"""
	En este test vamos a probar si las distribuciones d1
	y d2 son independientes. Esta es la funcion para utilizar scipy.stats.ttest_rel

	Hipotesis nula : Las distribuciones d1 y d2 son independientes.
	
	"""

	f = sp.ttest_ind(d1,d2)
	return f[0] , f[1] 



def ejercicio2(data):
	muestras_dias_soleados = data[:,0]
	muestras_dias_nublados = data[:,1]
	muestras_dias_lluviosos = data[:,2]

	# aca hay q hacer tests nuestros y probar hipotesis 
	estadistico , pvalor = test_muestras_apareadas(muestras_dias_soleados, muestras_dias_nublados)
	print estadistico , pvalor
	estadistico , pvalor = test_muestras_apareadas(muestras_dias_soleados, muestras_dias_lluviosos)
	print estadistico , pvalor
	estadistico , pvalor = test_muestras_independientes(muestras_dias_soleados, muestras_dias_lluviosos)
	print estadistico , pvalor

