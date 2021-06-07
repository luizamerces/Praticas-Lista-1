#Exercicio 3a

class Pessoa: 
    def __init__(self, name):
        self.name = name 
    def __str__(self): 
        return self.name 

luiza = Pessoa("Luiza")
print(luiza)
mary = Pessoa("Mary")
print(mary)

