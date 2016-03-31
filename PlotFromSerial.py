"""
PlotFromSerial.py

Plot samplings from load cell with Arduino

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
from collections import deque

import matplotlib.pyplot as plt 
import matplotlib.animation as animation

size_array = 1;
Nsamplings = 100;
    


#********************************************************************************************************
#[1] Modified

# plot class
class AnalogPlot:
  # constr
  def __init__(self, strPort, maxLen):
      # open serial port
      self.ser = serial.Serial(strPort, 9600)

      self.ax = deque([0.0]*maxLen)
      self.ay = deque([0.0]*maxLen)
      self.maxLen = maxLen

  # add to buffer
  def addToBuf(self, buf, val):
      if len(buf) < self.maxLen:
          buf.append(val)
      else:
          buf.pop()
          buf.appendleft(val)

  # add data
  def add(self, data):
      assert(len(data) == size_array)
      self.addToBuf(self.ax, data[0])
      self.addToBuf(self.ay, data[1])

  # update plot
  def update(self, frameNum, a0, a1):
      try:
          line = self.ser.readline()
          data = [int(line)/219.45 for val in line.split()]
	  #print data
          if(len(data) == size_array):
              self.add(data)
              a0.set_data(range(self.maxLen), self.ax)
              a1.set_data(range(self.maxLen), self.ay)
      except KeyboardInterrupt:
          print('exiting')
      
      return a0, 

  # clean up
  def close(self):
      # close serial
      self.ser.flush()
      self.ser.close()    

#***************************************************************************************

# main() function
def main():
  # create parser
  parser = argparse.ArgumentParser()
  # add expected arguments
  parser.add_argument('--port', dest='port', required=True)
  # parse args
  args = parser.parse_args()
  Port = args.port
  print('reading from serial port %s...' % Port)
  # plot parameters
  analogPlot = AnalogPlot(Port, 100)
  print('plotting data...')
  # set up animation
  analogPlot.ser.write('%d \n' %Nsamplings)
  print('write already\n')
  sleep(0.1)
  fig = plt.figure()
  ax = plt.axes(xlim=(0, 100), ylim=(0, 3023))
  a0, = ax.plot([], [])
  a1, = ax.plot([], [])
  anim = animation.FuncAnimation(fig, analogPlot.update, 
                                 fargs=(a0, a1), 
                                 interval=50)
  # show plot
  plt.show()
  # clean up
  analogPlot.close()

  print('exiting.')
  

# call main
if __name__ == '__main__':
  main()

"""
References:


[1]	Author: Mahesh Venkitachalam 
	Website: electronut.in
	Taken from: http://www.instructables.com/id/Plotting-real-time-data-from-Arduino-using-Python-/
	Date: 2013
	Source code available at: https://gist.github.com/electronut/d5e5f68c610821e311b0
"""
