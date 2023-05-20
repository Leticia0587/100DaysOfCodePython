# Função de saída
def format_name(middle_name, last_name):
    formatted_middle_name = middle_name.title()
    formatted_last_name = last_name.title()
    return f"{formatted_middle_name} {formatted_last_name}"


print(format_name(input("Qual é o seu nome do meio? "), input("Qual é o seu último nome? ")))

# Função com retorno
def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "Você não forneceu entradas válidas."
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"Resultado: {formatted_first_name} {formatted_last_name}"


# Armazenando o resultado em uma variável
formatted_name = format_name(input("Seu primeiro nome: "), input("Seu último nome: "))
print(formatted_name)

# Ou imprimindo o resultado diretamente
print(format_name(input("Qual é o seu primeiro nome? "), input("Qual é o seu último nome? ")))

# Usando o retorno de funções previamente utilizadas
length = len(formatted_name)

# Retorno como uma saída antecipada
def format_name(first_name, last_name):
    """Recebe um primeiro e último nome e formata para retornar a versão em caixa alta (título) do nome."""
    if first_name == "" or last_name == "":
        return "Você não forneceu entradas válidas."
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"Resultado: {formatted_first_name} {formatted_last_name}"
