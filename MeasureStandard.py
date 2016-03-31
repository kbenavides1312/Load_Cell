"""
MeasureStandard.py

Send number of samplings for get from a standard.
Save those samplings at a file called "datos.txt".
These data is used to calculate a linear trend line

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
from time import sleep


# main() function
def main():
  # create parser
  parser = argparse.ArgumentParser()
  # add expected arguments
  parser.add_argument('-i', dest='iter', type=str)
  parser.add_argument('-w', dest='weigth', type=str)
  parser.add_argument('--port', dest='port', required=True)
  # parse args
  args = parser.parse_args()
  Port = args.port
  Iter = args.iter
  Weigth = args.weigth

  print('reading from serial port %s...' % Port)
  #Start comunication
  SerialPort = serial.Serial(Port, 9600)
  SerialPort.flush()
  #Open file
  datos = open("datos.txt", "a")
  sleep(0.2)
  #Send number of samplings
  print('start writing... \n')
  SerialPort.write(Iter+'\n')
  print('write already\n')
  sleep(0.1)
  print('Set the standard\n')
  #Each time I send data to arduino serial mode, it restarts. So leave free the load cell before send data
  msg = SerialPort.readline();
  print('saving data from serial port %s...\n' % Port)
  transmisionIncompleta = True
  while (transmisionIncompleta):
	print(msg)
	print('fin de linea \n')
	#Format: Amplified_DigitalCoverted_SensorValue
	#	 ReferenceMeasurment
  	datos.write(msg+'\n')
  	datos.write('%d + \n' %Weigth)
	msg = SerialPort.readline();
   	if (msg[1]=='\n'):
		transmisionIncompleta=False
  

  # clean up
  SerialPort.flush()
  SerialPort.close()

  datos.close()  
  print('save done')

# call main
if __name__ == '__main__':
  main()
