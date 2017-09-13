# -*- coding: utf-8 -*-
"""
@author: svenproppert
"""
import random

dico = {}
wert = int(raw_input('Von wie viel soll runter gespielt werden?: '))
nrspieler = int(raw_input('Anzahl Spieler: '))

for ii in range(nrspieler):
    print '{0}. Spieler:'.format(str(ii+1))
    name = str(raw_input('Gib deinen Namen ein: '))
    dico[name] = wert

spielerliste = dico.keys()
random.seed()
random.shuffle(spielerliste)
    
ende = 0    
while ende < 1:
    for spieler in spielerliste:
        print 20*"=",'\nAktueller Punktestand:'
        for zocker in spielerliste:
            print zocker,':', dico[zocker]
        print 20*'='
        
        score  = raw_input('{0}, was hast du getroffen?: '.format(str(spieler))).split(',')
        
        if score[0] == 'e': #ermoeglicht manuellen exit
            ende = 1
            break
        if score[0] != '':
            try:
                memo = dico[spieler]
                for item in score:
                    if item !='':
                        item = int(eval(item))
                        if item <= dico[spieler]:
                            dico[spieler] -= item
                        else:
                            dico[spieler]=memo
                            break
            except:
                eingabe = raw_input('gib den neuen Punktestand manuell ein')
                dico[spieler] = eingabe
        if dico[spieler] == 0:
            print '\n',20*"*",'\n{0} hat gewonnen!\n'.format(str(spieler)),20*"*"
            ende = 1
            break

raw_input('hit enter to exit')            