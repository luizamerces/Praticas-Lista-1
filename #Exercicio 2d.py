#Exercicio 2d

nums = [i for i in range(1,1001)]
sentence = "Practice Problems to Drill List Comprehension in Your Head."

list = list(sentence)

[list.remove(i) for i in list if i == "a"]
[list.remove(i) for i in list if i == "e"]
[list.remove(i) for i in list if i == "i"]
[list.remove(i) for i in list if i == "o"]
[list.remove(i) for i in list if i == "u"]

print(list)