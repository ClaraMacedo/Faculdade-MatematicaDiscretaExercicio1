#Exercício 2
#Acadêmica: Ana Clara da Conceição Macêdo da Silva.

# criando um conjunto
conjunto = {1,2,3}
print (conjunto)

#pertinência de conjunto
c1 = {1, 2, 3}
c2 = {3, 4, 5}
print(3 in c1)

#continência de conjunto
a1 = {1, 2}
a2 = {1, 2}
print(a2.issubset(a1))

#subconjunto de conjunto
ac1 = {1, 2, 3}
ac2 = {1, 2}
print(ac2.issubset(ac1))

#igualdade de conjunto
ad1 = {1, 2, 3}
ad2 = {1, 2}
print(ad1==ad2)

# criando uma lista
lista = [1, 2, 3]
print (lista)

#pertinência de lista
comida = ['arroz', 'batata']
print('batata' in comida)

#continência de lista
l1 = [5, 6, 7]
l2 = [4, 5, 6, 7]
s1 = set(l1)
s2 = set(l2)
print(s1.issubset(s2))

#subconjunto de lista
lt1 = [5, 6, 7]
lt2 = [5, 6, 7]
print(lt1<=lt2)

#igualdade de lista
lst1 = [5, 6, 7, 8]
lst2 = [5, 6, 7, 8]
print(lst1==lst2)
