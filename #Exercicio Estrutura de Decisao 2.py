#Exercicio Estrutura de Decisao 2

n1 = float(input('Escreva nota 1 do aluno :'))
n2 = float(input('Escreva nota 2 do aluno :'))

nf = (n1+n2)/2
if nf > 6:
    print("Aprovado!")
elif 4 <= nf <= 6:
    print("Exame Especial!")
else: 
    print("Reprovado!")