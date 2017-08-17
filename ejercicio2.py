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


def test_muestra_unica(d, media_para_comparar):
	""" Dada una muestra vamos a calcular que tan lejos se encuentra de la media pasada
		como parametro. Es el test de muestra unica y se utiliza la funcion 
		scipy.stats.ttest_1samp
	"""
	f = sp.ttest_1samp(d, media_para_comparar)
	return f[0] , f[1] 

def test_wilcoxon(d1, d2):
	"""
	Test para ver si dos muestras dependientes provienen de la misma distribucion, es decir
	si la diferencia de las dos, tiene media 0. Se utiliza la funcion scipy.stats.wilcoxon

	"""
	f = sp.wilcoxon(d1, d2)
	return f[0] , f[1] 

def test_mannwhitneyu(d1, d2):
	"""
	Test para ver si de dos muestras independientes , cualquier valor tomado al azar de
	la segunda muestra va a ser mayor que alguno tomado de la primera
	"""
	f = sp.mannwhitneyu(d1, d2, alternative='greater')
	return f[0] , f[1] 


def ejercicio2(data):
	muestras_dias_soleados = data[:,0]
	muestras_dias_nublados = data[:,1]
	muestras_dias_lluviosos = data[:,2]

	# aca hay q hacer tests nuestros y probar hipotesis 
	estadistico , pvalor = test_muestras_apareadas(muestras_dias_soleados, muestras_dias_nublados)
	print estadistico , '%.10f' % pvalor
	estadistico , pvalor = test_muestras_apareadas(muestras_dias_soleados, muestras_dias_lluviosos)
	print estadistico , '%.10f' % pvalor
	estadistico , pvalor = test_muestras_independientes(muestras_dias_soleados, muestras_dias_lluviosos)
	print estadistico , '%.10f' % pvalor
	usainBolt_record_100_mts = 9.58
	usainBolt_promedio_100_mts_medallaOro = (9.69+9.58+9.63+9.77+9.79+9.81) / 6
	estadistico , pvalor = test_muestra_unica(muestras_dias_soleados, usainBolt_record_100_mts)
	print estadistico , '%.10f' % pvalor
	estadistico , pvalor = test_muestra_unica(muestras_dias_soleados, usainBolt_promedio_100_mts_medallaOro)
	print estadistico , '%.10f' % pvalor
	estadistico , pvalor = test_muestra_unica(muestras_dias_soleados, 12.5)
	print estadistico , '%.10f' % pvalor
	estadistico , pvalor = test_wilcoxon(muestras_dias_soleados, muestras_dias_nublados)
	print estadistico , '%.10f' % pvalor
	estadistico , pvalor = test_wilcoxon(muestras_dias_soleados, muestras_dias_lluviosos)
	print estadistico , '%.10f' % pvalor
	estadistico , pvalor = test_wilcoxon(muestras_dias_nublados, muestras_dias_lluviosos)
	print estadistico , '%.10f' % pvalor
	estadistico , pvalor = test_mannwhitneyu(muestras_dias_nublados, muestras_dias_lluviosos)
	print estadistico , '%.10f' % pvalor
	estadistico , pvalor = test_mannwhitneyu(muestras_dias_lluviosos, muestras_dias_nublados)
	print estadistico , '%.10f' % pvalor
	estadistico , pvalor = test_mannwhitneyu(muestras_dias_soleados, muestras_dias_lluviosos)
	print estadistico , '%.10f' % pvalor
