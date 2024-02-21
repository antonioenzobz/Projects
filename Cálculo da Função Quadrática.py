print ("------------- CALCULADORAEQUAÇÃO DE SEGUNDO GRAU --------------")

#Definindo as variáveis
a = float(input("Coeficiente a:"))
b = float(input("Coeficiente b:"))
c = float(input("Coeficiente c:"))

#Calculando o valor do delta:
d = b**2 - 4 * a * c

#Calculando as raízes por meio da formula de bhaskara
r1 = ((-1 * b) + d**(1/2)) / (2 * a)
r2 = ((-1 * b) - d**(1/2)) / (2 * a)
print(f"As raízes da equação são {r1} e {r2}")