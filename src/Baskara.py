#-*- coding: utf-8 -*-
from math import sqrt as rq
from org.kod.baskara.interfaces import Converte;

class Baskara(Converte):
    
    def __init__(self, avalue=1, bvalue=0, cvalue=0):
        '''
        Inicializa os objetos pricipais A, B e C.
        '''    
        self.avalue = float(avalue)
        self.bvalue = float(bvalue)
        self.cvalue = float(cvalue)
        self.pydelta = (self.bvalue ** 2) - (4 * self.avalue * self.cvalue)
        
    def getA(self):
        return self.intTransform(self.avalue)
    
    def getB(self):
        return self.intTransform(self.bvalue)
    
    def getC(self):
        return self.intTransform(self.cvalue)
    
    def getDelta(self):
        return self.intTransform(self.pydelta)
                    
    def resultValues(self):
        '''
        Retorna o resultado da fórmula de Baskara.
        '''
        
        if self.pydelta < 0:
            return u"Delta negativo, sem valores reais."
        
        elif self.pydelta == 0:
            self.x1 = (-(self.bvalue) + rq(self.pydelta)) / (2 * self.avalue)
            self.res = u"X = " + self.intTransform(self.x1)
            return self.res
        
        else:
            self.x1 = (-(self.bvalue) + rq(self.pydelta)) / (2 * self.avalue)
            self.x2 = (-(self.bvalue) - rq(self.pydelta)) / (2 * self.avalue)
            self.res = "X1 = " + self.intTransform(self.x1) + "\nX2 = " + self.intTransform(self.x2)
            return self.res
        
    def intTransform(self, valor):
        self.valor = valor
        if int(self.valor) == self.valor:
            return "%i" % int(self.valor)
        else:
            return "%.2f" % self.valor
