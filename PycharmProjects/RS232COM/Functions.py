# -*- coding: utf-8 -*-
import numpy as np
import time
import serial
import io

""" Fonction nettoyage """
def Clean_Data(List):
    new_list = []
    for i in range(len(List)):
        temp=List[i][2:]
        new_list.append(temp[:-3])
    return new_list


""" Fonction écriture """
def Write(List):
    file=open("data.txt",mode='w')
    for i in range(len(List)):
        file.write(List[i]+'\n')
    file.close()