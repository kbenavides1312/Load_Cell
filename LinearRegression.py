"""
LinearRegression.py

Read from "datos.txt" (odd row: abscissa; even row:ordinate)
Plot the graph
Compute the linear regression (y = mx+b)
Describe m as rational m1/m2

Author: Kenneth Benavides Rojas 
		kbr1312@gmail.com
	Andrés Salas Aburto
		salasc131@gmail.com
	Derian Palma Quirós
		derianpq@gmail.com
	Orlando Solís Villalta
		osolis1294@live.com

Date: 2006/03
"""

import sys, serial, argparse
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

def main():
	datos = open("datos.txt", "r")
	x = []
	y = []
	valor = datos.readline()
	while valor!='':
		x += [int(valor)]
		y += [int(datos.readline())]
		valor = datos.readline()
	print("values are on x and y now!\n")

	x = np.array(x);
	y = np.array(y);
	n = x.size
	unos = np.ones(n)
	suma_x = np.dot(x,unos)
	suma_y = np.dot(y,unos)
	suma_xy = np.dot(x,y)
	suma_xx = np.dot(x,x)


	m = ((suma_x/suma_xx)*suma_x-n)*suma_xx
	m=((suma_x/suma_xy)*suma_y-n)*suma_xy/m
	m2=2**16
	m1 = int(m*m2)


	plt.plot(x,y, 'ro')
	plt.show()
	print('m1 = %d\n m2 = %d\n b = %d'% (int(m1), int(m2), int(b)))
	datos.close()

# call main
if __name__ == '__main__':
  main()
