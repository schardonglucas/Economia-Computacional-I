"""
# Descrição: Este programa pergunta a idade do usuário, se a idade for maior que 18 anos haverá a mensagem na tela "oi, você é adulto"
# Autor: Lucas Schardong
# Data: 24.03.2026
# Versão: 0.0.1
"""

# Alocação de memória

idade = 0
texto = ""

# Entrada de dados

idade = int(input("\nQual a sua idade?"))

# Processamento de dados

if idade >= 18:
    texto = "Oi! Você é um adulto"

# Saída de dados

print(texto)