# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 17:19:19 2017

@author: svp34sc
"""
from __future__ import print_function,division
import random
player = int(raw_input('anzahl spieler: '))

spieler = {}

for i in range(player):
    key = str(raw_input('your name: '))
    spieler[key] = 0
  
ziele = (15,16,'Double',17,18,'Triple',19,20,'Bulls-Eye')

spielerliste = spieler.keys()
random.seed()
random.shuffle(spielerliste)
while True:
    for key in spielerliste:
        spieler[key] = 0
    for ziel in ziele:
        for key in spielerliste:
            wert = int(eval(raw_input('{0}: Triff {1} -- '.format(str(key),str(ziel)))))
            
            if ziel == 'Double':
                ziel = 2
            elif ziel == 'Triple':
                ziel = 3
            elif ziel == 'Bulls-Eye':
                ziel = 25
            else:
                pass
            
            wert *= ziel
            if wert == 0:            
                val = spieler[key]
                spieler[key] = val//2 + val%2          
            else:
                spieler[key] += wert
                
            print(spieler[key])
            
            if ziel == 2:
                ziel = 'Double'
            elif ziel == 3:
                ziel = 'Triple'
            elif ziel == 25:
                ziel = 'Bulls-Eye'
            else:
                pass
                
    print(spieler)
    if str(raw_input('drueck "y enter" fuer neues spiel: ')) == 'y':
        pass
    else:
        break