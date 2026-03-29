"""
# Descrição: Este programa pergunta a idade do usuário, se a idade for maior que 18 anos haverá a mensagem na tela "oi, você é adulto"
# Autor: Lucas Schardong
# Data: 24.03.2026
# Versão: 0.1.0
"""

# Alocação de memória

idade = 0
texto = ""
texto_2 = ""

# Entrada de dados

idade = int(input("\nQual a sua idade?"))

# Processamento de dados

if idade >= 18:
    texto = "Oi! Você é um adulto"
else:
    texto_2 = "Oi! Você é menor de idade"

# Saída de dados

print(texto)
print(texto_2)