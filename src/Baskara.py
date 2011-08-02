#-*- coding: utf-8 -*-
from math import sqrt as rq
from org.kod.baskara.interfaces import Converte;

class Baskara(Converte):
    
    def __init__(self, avalue=1, bvalue=0, cvalue=0):
        '''
        Inicializa os objetos pricipais A, B e C.
        '''    
        self.avalue = self.floatTransform(avalue)
        self.bvalue = self.floatTransform(bvalue)
        self.cvalue = self.floatTransform(cvalue)
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
        if self.avalue == 0:
            self.res = u"O valor de 'a' não pode ser nulo."
            
        elif self.bvalue == 0:
            self.xqu = -(self.cvalue / self.avalue)
            if self.xqu < 0:
                self.res = u"x = \u221a" + self.intTransform(self.xqu)
            else:
                self.res = u"x = \xb1\u221a" + self.intTransform(self.xqu) + u" \u21d2 x = \xb1" + self.intTransform(rq(self.xqu))
        
        elif self.cvalue == 0:
            self.res = -(self.bvalue / self.avalue) 
            
        elif self.pydelta < 0:
            self.res = u"Delta negativo, sem valores reais."
        
        elif self.pydelta == 0:
            self.x1 = -(self.bvalue) / (2 * self.avalue)
            self.res = u"x = " + self.intTransform(self.x1)
        
        else:
            self.x1 = (-(self.bvalue) + rq(self.pydelta)) / (2 * self.avalue)
            self.x2 = (-(self.bvalue) - rq(self.pydelta)) / (2 * self.avalue)
            self.res = u"x\u2081 = " + self.intTransform(self.x1) + u"\nx\u2082 = " + self.intTransform(self.x2)
        return self.res
        
    def intTransform(self, valor):
        self.valor = valor
        if int(self.valor) == self.valor:
            return "%i" % int(self.valor)
        else:
            return "%.2f" % self.valor
    
    def floatTransform(self, valor):
        self.valor = valor
        
        if ',' in self.valor:
            while self.valor.count(',') > 1:
                self.valor = self.valor.replace(',', '', 1)
            self.valor = self.valor.replace(',', '.')
        
        if ' ' in self.valor:
            self.valor = self.valor.replace(' ', '')
        
        if len(self.valor) == 0 or len(self.valor) == 1 and self.valor == '.':
            self.valor = "0"
        
        
        return float(self.valor)
