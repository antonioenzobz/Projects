print ("------------- Calculadora de IMC --------------")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso / (altura**2)

print (f"O seu IMC é de {IMC:.2f}")