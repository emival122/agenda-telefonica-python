import csv

# Adiciona uma linha ao arquivo CSV


def adicionar_dados(i):
    # 'a+' abre para leitura e escrita, anexando ao final do arquivo
    with open('dados.csv', 'a+', newline='', encoding='utf-8') as file:
        escrever = csv.writer(file)
        escrever.writerow(i)

# Retorna todos os dados do arquivo CSV para a Treeview


def ver_dados():
    dados = []
    try:
        with open('dados.csv', 'r', encoding='utf-8') as file:
            ler_csv = csv.reader(file)
            for linha in ler_csv:
                dados.append(linha)
    except FileNotFoundError:
        # Cria um arquivo vazio se ele não existir
        return []
    return dados

# Remove um dado baseado no telefone (campo único)


def remover_dados(i):
    def adicionar_novalista(j):
        with open('dados.csv', 'w', newline='', encoding='utf-8') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)

    nova_lista = []
    with open('dados.csv', 'r', encoding='utf-8') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            # i é o telefone passado pelo botão Deletar
            if i not in linha:
                nova_lista.append(linha)

    adicionar_novalista(nova_lista)

# Atualiza um dado existente


def atualizar_dados(i):
    def adicionar_novalista(j):
        with open('dados.csv', 'w', newline='', encoding='utf-8') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)

    nova_lista = []
    # i[0] é o telefone_antigo que salvamos na global do main.py
    telefone_antigo = i[0]

    with open('dados.csv', 'r', encoding='utf-8') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            if telefone_antigo in linha:
                # Substitui a linha antiga pelos novos dados editados
                nova_lista.append([i[1], i[2], i[3], i[4]])
            else:
                nova_lista.append(linha)

    adicionar_novalista(nova_lista)
