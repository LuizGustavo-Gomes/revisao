# Crie uma variável chamada nome e atribua a ela o seu nome. Crie uma variável idade e atribua a sua idade. Imprima uma mensagem que inclua ambos os valores, por exemplo: 
#     "Meu nome é [nome] e eu tenho [idade] anos."

# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")

# print(f"Seu nome é {nome} e sua idade é de {idade} anos")

# # Converta a variável idade para o tipo de dado float e imprima o tipo da variável.

# idade = float(idade)
# print(f"O tipo da variável idade é {type(idade)}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Escreva um programa que receba um número do usuário e verifique se ele é par ou ímpar. Exiba uma mensagem apropriada.

# numero = int (input("Digite um numero:"))
# if numero % 2 == 0:
#     print("O numero digitado é par")
# else:
#     print("O numero é impar")

# Escreva um programa que receba a nota de um aluno e determine se ele foi aprovado, reprovado ou se está em recuperação. As notas são consideradas da seguinte forma:

# nota = float(input("Digite sua nota: "))

# if nota >= 7:
#     print("Aprovado")
# elif nota >= 5 and nota <= 6.9 :
#     print("Recuperação")
# else:
#     print("reprovado")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Crie uma função chamada saudacao que receba um nome como parâmetro e imprima uma saudação personalizada, por exemplo: "Olá, [nome]!".

# def saudacao():
#     nome = "Luiz"
#     return f"Olá, {nome}"

# variavel = saudacao()
# print(variavel)

# Crie uma função chamada soma que receba dois números como parâmetros e retorne a soma desses números. Teste a função com diferentes valores.

# def soma():
#     a = int(input("Digite um numero: "))
#     b = int(input("Digite outro numero: "))
#     return a + b

# s = soma()
# print(f"A soma dos números é: {(s)}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fatorial():
    resultado = 1
    n = 5
    for i in range(1, n + 1):
        resultado *= i

r = fatorial()
print(r)


