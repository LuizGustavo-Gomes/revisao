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

# Crie uma função chamada fatorial que calcule o fatorial de um número inteiro não-negativo. Lembre-se de que o fatorial de um número n é o produto de todos os números inteiros positivos menores ou iguais a n. Por exemplo, o fatorial de 5 (5!) é 120.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Crie uma lista contendo cinco números inteiros. Adicione um número no final da lista e remova o primeiro número. Em seguida, imprima a lista atualizada.

# lista = [1, 2, 3, 4, 5]
# print(lista)
# lista.append(int(input("Digite um numero: ")))
# lista.remove(1)
# print(lista)


# Escreva um programa que encontre o maior e o menor número em uma lista.​

# lista = [1, 2, 3, 4, 5]
# maior = max(lista)
# menor = min(lista)
# print(lista)
# print(f"o maior numero da lista é {maior} e o menor é {menor}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

livro = {
    "titulo": "Harry Potter e a Pedra Filosofal",
    "autor": "J. K. Rowling",
    "ano_publicacao": 1997
}

print("Título:", livro["titulo"])
print("Autor:", livro["autor"])
print("Ano de Publicação:", livro["ano_publicacao"])

