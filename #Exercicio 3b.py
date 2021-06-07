#Exercicio 3b

from calculadorasimples import CalculadoraSimples
c = CalculadoraSimples(10,5)
print("Soma: ", c.soma())
print("Subtração: ", c.subtrai())
print("Multiplicação: ", c.multiplica())
print("Divisão: ", c.divide())
c.a = 50
c.b = 10
print(c.a," + ", c.b , " = ", c.soma())
print(c.a, " - ", c.b, " = ", c.subtrai())
print(c.a , " x ", c.b, " = ", c.multiplica())
print(c.a, " / ", c.b, " = ", c.divide())