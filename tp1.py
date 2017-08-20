import numpy as np
import matplotlib.pylab as plt
import pandas as pd 
import seaborn as sns
from ejercicio2 import *

def cleanData(data):
	means = []
	stds = []
	for c in xrange(0, data.shape[1]):
		 means.append(np.mean(data[:][c]))
		 stds.append(np.std(data[:][c]))
	return np.array(filter(lambda r: filterDataRows(r, means, stds), data))

def filterDataRows(row, means, stds):
	for index in range(len(row)):
		if (abs(row[index] - means[index]) > 5 * stds[index]):
			return False
	return True

def plot(data, data_type):
	d1 = data[:,0]
	d2 = data[:,1]
	d3 = data[:,2]
	binwidth = 0.5
	plt.hist(d1,bins=np.arange(min(d1), max(d1) + binwidth, binwidth), label="Tiempo soleado")
	plt.hist(d2,bins=np.arange(min(d2), max(d2) + binwidth, binwidth), label="Tiempo nublado")
	plt.hist(d3,bins=np.arange(min(d3), max(d3) + binwidth, binwidth), label="Tiempo lluvioso")
	plt.legend(loc='upper right')
	plt.xlabel("Segundos que se tarda en hacer los 100 mts.")
	plt.ylabel("Cantidad de atletas que lo logran en ese tiempo.")
	plt.title("Distribucion de los tiempos de corrida, por estado del dia. Datos " + data_type)
	#plt.show()

	plt.subplot(1,3,1)
	plt.plot(d1, "r-" , marker='o')
	plt.title("Tiempo Soleado. Datos " + data_type)
	plt.xlabel("Numero atleta")
	plt.ylabel("Tiempo en segundos para los 100 mts")
	plt.subplot(1,3,2)
	plt.plot(d2, "b-", marker='o')
	plt.title("Tiempo Nublado. Datos " + data_type)
	plt.xlabel("Numero atleta")
	plt.ylabel("Tiempo en segundos para los 100 mts")
	plt.subplot(1,3,3)
	plt.plot(d3, "g-", marker='o')
	plt.title("Tiempo Lluvioso. Datos " + data_type)
	plt.xlabel("Numero atleta")
	plt.ylabel("Tiempo en segundos para los 100 mts")
	#plt.show()

	plt.plot(d1, label="Tiempo soleado")
	plt.plot(d2, label="Tiempo nublado")
	plt.plot(d3, label="Tiempo lluvioso")
	plt.xlabel("Numero atleta")
	plt.ylabel("Tiempo en segundos para los 100 mts")
	plt.title("Estados del tiempo, superpuestos.Datos " + data_type)
	plt.legend(loc='upper right')
	#plt.show()

	
	data_frame = pd.DataFrame(data)
	data_frame.columns = ["soleado" , "nublado" , "lluvioso"]

	sns_plot = sns.pairplot(data_frame)
	plt.show()


data = np.loadtxt('tiempos.txt')
plot(data , "sucios")
data = cleanData(data)
plot(data, "limpios")



ejercicio2(data)




