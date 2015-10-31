# -*- coding: utf-8 -*-
import threading
import time
import BluetoothClient_class
import Ringbuffer_String
import Ringbuffer_Float
import numpy as np
import datetime
import bluetooth_gui 
import random


exitGuiFlag = 0
exitFlag = 0
guiData = None
threads=[]
queueLock = threading.Lock()
dataList = [100]

class measurementThread (threading.Thread):
    
    data = None 
    
    def __init__(self,name,delay, dataSource,requiredData,ringBuffString,ringBuffFloat):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.dataSource = dataSource
        self.requiredData = requiredData
        self.ringBuffString = ringBuffString
        self.ringBuffFloat = ringBuffFloat
        self.ringBuffString.__reset__()
        self.ringBuffFloat.__reset__()
        
    def run(self):
        print ("Starting " + self.name)
        get_data(self.name, self.delay,self.dataSource,self.requiredData,self.ringBuffString,self.ringBuffFloat)
        print ("Exiting " + self.name)
        print ("Last Data " , measurementThread.data)
        
    def __del__(self):
        print (self.name, 'died')

def get_data(threadName, delay,dataSource,requiredData,ringBuffString,ringBuffFloat):   
        global guiData
        global exitFlag
        
        x = np.array([0.0,0.0])
   
        while (exitFlag == 0):
              #global exitFlag
              #guiData = dataSource.getData(requiredData).decode("utf-8")    # Werteübergabe
              buff = dataSource.getData(requiredData).decode("utf-8")    # Werteübergabe
              guiData = buff
              float(buff)
              x[1]=buff
              ringBuffFloat.append(x[1])
              #save Timestamp
              ringBuffString.append(np.datetime64(datetime.datetime.now()))
              print ("Measured Value: ",guiData)
              time.sleep(delay)



class guiThread (threading.Thread):
    def __init__(self,name,delay,outputText,canvas,ringBuffString,ringBuffFloat):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.outputText = outputText
        self.canvas = canvas
        self.ringBuffString = ringBuffString
        self.ringBuffFloat = ringBuffFloat
        
    def run(self):
        print ("Starting " + self.name)
        updateGUI(self.outputText,self.delay,self.canvas,self.ringBuffString,self.ringBuffFloat)
        print ("Exiting " + self.name)
        
    def __del__(self):
        print (self.name, 'died')


def updateGUI(outputText,delay,canvas,ringBuffString,ringBuffFloat):
              global guiData  
              global exitGuiFlag
              buffer = str(exitGuiFlag)               
              print ("exitGuiFlag " + buffer)
              
              while (exitGuiFlag == 0):
                    outputText.setText(str(guiData))
                    canvas.ax.clear()
                    #Set up GUI-Graph
                    t = np.arange(0.0, 5.0, 0.05)
                    canvas.ax.set_ylabel('Data')
                    canvas.ax.set_xlabel('Data Points/50ms')
                    canvas.ax.grid()
                    canvas.ax.plot(t,ringBuffFloat.get_all(),color='red',label="Data")     
                    canvas.draw()
                    time.sleep(delay)



class stopThread (threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):
        print ("Starting " + self.name)
        setExitFlag()
        print ("Exiting " + self.name)

    def __del__(self):
        print (self.name, 'died')


def setExitFlag():
              global exitFlag
              exitFlag =1
              #time.sleep(0.5)
             
class exitFlagGui (threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):
        print ("Starting " + self.name)
        setFlagGUIExit()
        print ("Exiting " + self.name)

    def __del__(self):
        print (self.name, 'died')


def setFlagGUIExit():
              global exitGuiFlag
              exitGuiFlag =1
              #time.sleep(0.5)


class resetExitFlagThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):
        print ("Starting " + self.name)
        resetExitFlag()
        print ("Exiting " + self.name)
        
    def __del__(self):
        print (self.name, 'died')

def resetExitFlag():
              global exitFlag
              exitFlag =0
                          
