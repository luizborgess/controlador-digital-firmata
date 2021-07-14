from numpy import genfromtxt
import matplotlib.pyplot as plt


dir=input('Insira a localizaçao do arquivo csv Ex(/Users/Downloads/meu_save.csv): ')
my_data = genfromtxt(dir, delimiter=',')


plt.plot(my_data[:,0],my_data[:,1])
plt.ylabel('response')
plt.xlabel('tempo')
plt.show()
