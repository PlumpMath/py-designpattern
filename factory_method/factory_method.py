#!/usr/bin/python
# -*- coding : utf-8 -*-
"""
    @author: Diogenes Augusto Fernandes Herminio <diofeher@gmail.com>
"""
import string

# Product
class Churrasco(object): 
    def __init__(self):
        self.fala = None
 
 
class ChurrascoGato(Churrasco):
    def __init__(self):
        self.fala = 'Miau'
        
        
class ChurrascoCarneiro(Churrasco):
    def __init__(self):
        self.fala = 'Beeeeeeeh'
        
        
# Factory 
class ChurrascoFactory(object):
    @staticmethod
    def fazer_churrasco(churras):
        if churras == 'carneiro':
            return ChurrascoCarneiro()
        elif churras == 'gato':
            return ChurrascoGato()
        
#Client
if __name__== "__main__":
    for i in ['gato', 'carneiro']:
        churras_obj = ChurrascoFactory.fazer_churrasco(i)
        print churras_obj.fala