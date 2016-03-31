"""
SaveData
Send number of samplings for get.
Save those samplings at a file called "tabla.txt".

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
import datetime
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
  datos = open("tabla.txt", "a")
  sleep(0.2)
  #Send number of samplings
  print('start writing... \n')
  SerialPort.write(Iter+'\n')
  print('write already\n')
  sleep(0.1
  #Each time I send data to arduino serial mode, it restarts. So leave free the load cell before send data)
  print('Set the standard\n')
  msg = SerialPort.readline();
  print('saving data from serial port %s...\n' % Port)
  transmisionIncompleta = True
  cont = 1
  while (transmisionIncompleta):
	valor = int(msg[0:-2])
	voltaje_sensor = (valor*1000/2**12)*1000/2**12*0.5/64*5
	cont += 1
	time1=datetime.datetime.strftime(datetime.datetime.now(), '%M:%S')
	print(voltaje_sensor)
	#Format: sample_id | sensor_voltage | Minutes:Seconds | Weight_measurement
  	datos.write(str(cont)+'\t'+str(int(voltaje_sensor))+'\t'+str(time1)+'\t'+str(int(valor/219.45))+'\n')
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
