#Exercicio 3c

from calculadora import Calculadora
c = Calculadora()
a = float(input("Digite a primeira parcela: "))
b = float(input("Digite a segunda parcela: "))
print (a,"+", b, "=", c.soma(a,b))
a = float(input("Digite o termo 1 da subtração: "))
b = float(input("Digite o temo 2 da subtração: "))
print (a,"-", b, "=", c.subtrai(a, b))
a = float(input("Digite o fator 1 da multiplicação: "))
b = float(input("Digite o fator 2 da multiplicação: "))
print (a,"x", b, "=", c.multiplica(a,b))
a = float(input("Digite o dividendo: "))
b = float(input("Digite o divisor: "))
print (a,"/", b, "=", c.divide(a,b))