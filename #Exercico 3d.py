#Exercico 3d

from usuario import User 
c = 1
while c==1:   
    a = (input("Digite nome do usuário: ")) 
    b = int(input("Digite idade do usuário: ")) 
    u = User(a, b)
    u.save()
    c = int(input("Digite (1) se deseja adicionar mais um usuário ou outro número para finalizar: "))
print(User.all())