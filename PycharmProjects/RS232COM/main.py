# -*- coding: utf-8 -*-
import time
import serial
import io
from Functions import *


if __name__ == "__main__":
    """ Ouverture du Port 3 """
    port = 'COM3'
    baudrate = 115200
    parity = serial.PARITY_NONE
    stopbits = serial.STOPBITS_ONE
    bytesize = serial.EIGHTBITS
    timeout = 0.05

    """ Création d'une instance de la classe Serial"""
    ser = serial.Serial(port, baudrate, parity, stopbits, bytesize, timeout)

    """ Lecture et affichage des données en boucle """
    while True:
        RawData = []
        value = ser.readline()
        RawData.append(str((value)))  # Stockage des données en Str dans RawData

        """ Affichage des données dans la console """
        cleandata = Clean_Data(RawData)
        print(cleandata)

        """ Ecriture des données dans le fichier data.txt """
        Write(cleandata)