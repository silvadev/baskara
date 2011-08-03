#-*- coding: utf-8 -*-
from math import sqrt as rq
from org.kod.baskara.interfaces import Converte;

class Baskara(Converte):
    
    def __init__(self, avalue=1, bvalue=0, cvalue=0):
        '''
        Inicializa os objetos pricipais A, B, C e Delta.
        '''    
        self.avalue = self.floatTransform(avalue)
        self.bvalue = self.floatTransform(bvalue)
        self.cvalue = self.floatTransform(cvalue)
        self.belta = (self.bvalue ** 2) - (4 * self.avalue * self.cvalue)
        
    def getA(self):
        '''
        Retorna o valor de 'a'.
        '''
        return self.intTransform(self.avalue)
    
    def getB(self):
        '''
        Retorna o valor de 'b'.
        '''
        return self.intTransform(self.bvalue)
    
    def getC(self):
        '''
        Retorna o valor de 'c'.
        '''
        return self.intTransform(self.cvalue)
    
    def getDelta(self):
        '''
        Retorna o valor de 'delta'.
        '''
        return self.intTransform(self.belta)
                    
    def resultValues(self):
        '''
        Retorna o resultado da Fórmula de Bhaskara.
        '''
        if self.avalue == 0:
            '''
            Retorna uma exceção se o valor de 'a' for nulo.
            '''
            self.res = u"O valor de 'a' não pode ser nulo."
            
        elif self.bvalue == 0:
            '''
            Caso o valor de 'b' for nulo retorna a fórmula de resolução
            das equações quadráticas incompletas sem a icógnita 'bx'.
            '''
            self.xqu = -(self.cvalue / self.avalue)
            if self.xqu < 0:
                '''
                Se o resultado de 'x^2' for negativo não haverá uma solução
                real.
                '''
                self.res = u"x = \u221a" + self.intTransform(self.xqu)
            else:
                self.res = u"x = \xb1\u221a" + self.intTransform(self.xqu) + u" \u21d2 x = \xb1" + self.intTransform(rq(self.xqu))
        
        elif self.cvalue == 0:
            '''
            Caso o valor de 'c' for nulo retorna a fórmula de resolução
            das equações quadráticas incompletas sem a icógnita 'c'.
            '''
            self.x1 = -(self.bvalue / self.avalue)
            self.res = u"x = " + self.intTransform(self.x1) 
            
        elif self.belta < 0:
            '''
            Se o resultado de 'delta' for negativo não haverá uma solução
            real.
            '''
            self.res = u"Delta negativo, sem valores reais."
        
        elif self.belta == 0:
            '''
            Se o resultado de 'delta' for nulo só haverá uma raiz para 'x'.
            '''
            self.x1 = -(self.bvalue) / (2 * self.avalue)
            self.res = u"x = " + self.intTransform(self.x1)
        
        else:
            self.x1 = (-(self.bvalue) + rq(self.belta)) / (2 * self.avalue)
            self.x2 = (-(self.bvalue) - rq(self.belta)) / (2 * self.avalue)
            self.res = u"x\u2081 = " + self.intTransform(self.x1) + u"\nx\u2082 = " + self.intTransform(self.x2)
        return self.res
        
    def intTransform(self, valor):
        '''
        Esta função formata um valor dado de float para inteiro caso o valor
        não apresente valores decimais como: 50.00000, 20000.00000000.
        Caso ele não se pareça com a descrição acima o valor retornaado será
        com duas casa decimais de precisão. 
        '''
        self.valor = valor
        if int(self.valor) == self.valor:
            return "%i" % int(self.valor)
        else:
            return "%.2f" % self.valor
    
    def floatTransform(self, valor):
        '''
        Esta função transforma a string em float suprimindo e realocando
        caracteres como a ',' (vírgula) e espaço em branco.
        TODO: Ainda falta implementar a exclusão de caracteres do alfabeto
        que não se enquadra na construção de uma variável do tipo float.
        '''
        self.valor = valor
        
        if ',' in self.valor:
            '''
            Caso apareça alguma vírgula na variável ela é substituída por
            ponto (.).
            '''
            while self.valor.count(',') > 1:
                '''
                Enquanto houver mais de uma vírgula, serão eliminadas as
                primeiras ficando somente a última vírgulan como sendo
                válida na demarcação de número decimal.
                '''
                self.valor = self.valor.replace(',', '', 1)
            self.valor = self.valor.replace(',', '.')
        
        if ' ' in self.valor:
            '''
            Caso haja algum espaço em branco esses serão eliminados.
            '''
            self.valor = self.valor.replace(' ', '')
        
        if len(self.valor) == 0 or len(self.valor) == 1 and self.valor == '.':
            '''
            Se não houver nenhum caractere na variável ou este contiver apenas
            um ponto (.) seu valor será definido como '0'.
            '''
            self.valor = "0"
        
        
        return float(self.valor)
