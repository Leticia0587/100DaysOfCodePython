programa_dicionario = {
  "Bug": "Um erro em um programa que impede que o programa seja executado conforme o esperado.",
  "Function": "Um trecho de código que você pode chamar facilmente repetidamente.",
}

# Recuperando itens do dicionário.
# print(programa_dicionario["Function"])

# Adicionando novos itens ao dicionário.
programa_dicionario["Loop"] = "A ação de fazer algo repetidamente."

# Criando um dicionário vazio.
vazio_dicionario = {}

# Limpando um dicionário existente.
# programa_dicionario = {}
# print(programa_dicionario)

# Editando um item em um dicionário.
programa_dicionario["Bug"] = "Uma mariposa em seu computador."
# print(programa_dicionario)

# Percorrendo um dicionário.
# for key in programa_dicionario:
#   print(key)
#   print(programa_dicionario[key])

#######################################

# Aninhamento
capitais = {
  "França": "Paris",
  "Alemanha": "Berlim",
  "Brasil": "Brasília"
}

# Aninhando uma lista em um dicionário.
viagem = {
  "França": ["Paris", "Lille", "Dijon"],
  "Alemanha": ["Berlim", "Hamburgo", "Stuttgart"],
}

# Aninhando dicionário em um dicionário.
viagem = {
  "França": {"cidades_visita": ["Paris", "Lille", "Dijon"], "total_visitas": 12},
  "Alemanha": {"cidades_visita": ["Berlim", "Hamburgo", "Stuttgart"], "total_visitas": 5},
}

# Aninhando dicionários em listas.
viagem = [
  {
    "país": "França",
    "cidades_visita": ["Paris", "Lille", "Dijon"],
    "total_visitas": 12,
  },
  {
    "país": "Alemanha",
    "cidades_visita": ["Berlim", "Hamburgo", "Stuttgart"],
    "total_visitas": 5,
  },
]
