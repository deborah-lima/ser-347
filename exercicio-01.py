import numpy as np

#Series temporais como listas
s1 = [168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,242, 331, 251, 323, 106, 1055, 170]
s2= [168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,242, 331, 251, 180, 106, 1055, 200]

#criando arrays a partir das listas
a = np.array(s1)
b = np.array(s2)

#calculo distancia euclidiana

#subtraçao
subtracao = a - b
quadrado = subtracao**2
somatorio = np.sum(quadrado)
distancia = np.sqrt(somatorio)

print("A distância euclidiana entre as séries é:\n",distancia)

print()

#valores medios
media = (a+b) / 2
print("A matriz com os valores médios \n",media)

print()

#valores maximos
max =np.maximum(a, b)
print("Matriz com valores máximos:\n",max )

print()

#valores minimos
min =np.minimum(a, b)
print("Matriz com valores mínimos:\n",min )


