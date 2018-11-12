#Faça um programa que peça as 4 notas bimestrais e mostre a média.

primeira_nota = input("Digite a primeira nota: ")
segunda_nota = input("Digite a segunda nota: ")
terceira_nota = input("Digite a terceira nota: ")
quarta_nota = input("Digite a quarta nota: ")

soma_notas = int(primeira_nota) + int(segunda_nota) + int(terceira_nota) + int(quarta_nota)
media = soma_notas / 4

print("A média das notas informadas é: ", media)
