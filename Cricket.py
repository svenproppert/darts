# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 23:25:41 2017

@author: 
"""
import random
zahlen = {'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'points':0,'finished':0}

#from copy import deepcopy
#
#players = {}
#
#for i in range(int(raw_input('how many players?: '))):
#    vari = str(raw_input('please enter your name: '))
#    players[vari]=deepcopy(zahlen)
#    players[vari]=zahlen
#    
players = {
            'Felix':{'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'points':0,'finished':0},
            'Sven':{'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'points':0,'finished':0},
#            'Martin':{'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'points':0,'finished':0},
#            'Lydia':{'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'points':0,'finished':0},
#            'Johanna':{'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'points':0,'finished':0},
            
#            'Robert':{'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'points':0,'finished':0},
#            'Guest':{'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'points':0,'finished':0},
           }

spielerliste = players.keys()
random.seed()
random.shuffle(spielerliste)
print "\nEnter scores according to this example:\n16,2*15,1*20,4*19,16,16\nDifferent scores \
are separated by comma.\nThe order does not matter.\nTHERE IS NO UNDO!!!\n",60*'=','\n'
while True:
    flagge = 0
    for player in spielerliste:  
        points = []
        print 20*"'",'\n{0}s turn:'.format(player)
        ergebnis = str(raw_input('What did you score? (e for exit): ')).split(',')   
        
        if ergebnis[0] == 'e':
            winner = 'Nobody'
            flagge = 1
            break            

        for item in ergebnis: 
            if '*' in item:
                plus,key = item.split('*')
                if key in zahlen.keys():
                    if players[player][key] <= 3:
                        players[player][key]+=int(plus)                         
                    for spieler in players.keys():
                        if ((players[spieler][key] < 3)*(spieler != player)*(players[player][key] >3)) ==1:
                            players[spieler]['points'] += (players[player][key] -3) *int(key)         
                    if players[player][key] > 3:
                        players[player][key] = 3
            else:
                if item in zahlen.keys():
                    if players[player][item] <= 3:
                        players[player][item]+=1                       
                    for spieler in players.keys():
                        if ((players[spieler][item] < 3)*(spieler != player)*(players[player][item] >3)) ==1:
                            players[spieler]['points'] += int(item)
                    if players[player][item] > 3:
                        players[player][item] = 3
                            
        players[player]['finished'] = 0
        for steve in players[player].keys():
            if steve != 'points':
                if players[player][steve] >=3:
                    players[player]['finished']+=1
        
        for zocker in players.keys():
            points.append(players[zocker]['points'])
        if (players[player]['finished'] >= 6)*(players[player]['points'] == min(points)) ==1:
            flagge = 1
            winner = player
            break
        
        print '\nOverview:\n',20*"'"
        for steve in sorted(players.keys()):
            print steve+':'
            for dorian in sorted(players[steve].keys()):
                if (dorian != 'finished')*(dorian != 'points')==1:
                    if players[steve][dorian] >= 3:
                        print dorian+':', 5*'='                      
                    else:
                        print dorian+':', players[steve][dorian]
                if dorian == 'points':
                    print dorian+':',players[steve][dorian]
            print ''  
            
    if flagge == 1:
        print 20*"*",'\n',20*"*",'\n{0} wins!\n'.format(winner),20*"*",'\n',20*"*"
        print '\nResult:\n',20*"'"
        for steve in sorted(players.keys()):
            print steve+':'
            for dorian in sorted(players[steve].keys()):
                if (dorian != 'finished')*(dorian != 'points')==1:
                    if players[steve][dorian] >= 3:
                        print dorian+':', 5*'=' 
                    else:
                        print dorian+':', players[steve][dorian]
                if dorian == 'points':
                    print dorian+':',players[steve][dorian]    
            print ''
        break
raw_input('hit enter to exit')

