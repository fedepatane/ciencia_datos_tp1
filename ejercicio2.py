import scipy.stats as sp

def test_muestras_apareadas(data):
	"""
	En este test vamos a probar si las distribuciones de dias soleados
	y dias nublados tienen la misma media. Para eso hay que usar el test de muestras
	apareadas. Esta es la funcion para utilizar scipy.stats.ttest_rel

	Hipotesis nula : Las distribuciones de tiempos en dias soleados y dias nublados
	tienen la misma media.
	
	"""

	muestra_dias_soleados = data[:,0]
	muestra_dias_nublados = data[:,1]
	f = sp.ttest_rel(muestra_dias_soleados,muestra_dias_nublados)
	return f[0] , f[1] 


def ejercicio2(data):
	# aca hay q hacer tests nuestros y probar hipotesis 
	estadistico , pvalor = test_muestras_apareadas(data)

