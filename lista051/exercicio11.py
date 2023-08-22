'''
 Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be . (Sem usar Math.pow();)
'''

base = float(input("Fale uma base da potencia: "))

expoente = float(input("Fale o expoente da potencia: "))

contador = 1
acumulador = 1

while contador<= expoente:

    acumulador = acumulador * base
    contador = contador + 1

print(f"A base elevada a {expoente} é {acumulador}")











