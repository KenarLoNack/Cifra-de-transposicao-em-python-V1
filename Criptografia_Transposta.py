import numpy as np


def chavetransposta(chave):
    # Encontrar a inversa da permutação
    inversa = np.argsort(chave) + 1  # argsort dá os índices ordenados

    return inversa.tolist()  # Retorna como lista normal


def decifrar_transposicao_dupla(texto_cifrado, num_colunas, num_linhas, chave_colunas, chave_linhas):

    column_trans = chavetransposta(chave_colunas)
    row_trans = chavetransposta(chave_linhas)

    # Garantir que o texto tenha o tamanho correto baseado nas chaves e compelta com x caso necessario
    if len(texto_cifrado) < num_linhas * num_colunas:
        texto_cifrado = texto_cifrado + 'X' * \
            (num_linhas * num_colunas - len(texto_cifrado))

    # cria a matriz inicial com o texto cifrado
    matriz_cifrada = []
    for i in range(0, len(texto_cifrado), num_colunas):
        matriz_cifrada.append(list(texto_cifrado[i:i+num_colunas]))

    print("\nMatriz Original:")
    for i in matriz_cifrada:
        print(i)

    # Reorganizar as linhas na ordem correta utilizando chave_linhas transposta
    matriz_temp = [['' for _ in range(num_colunas)] for _ in range(num_linhas)]
    for i in range(num_linhas):
        # A chave indica a posição original da linha
        linha_atual = row_trans[i] - 1
        # mover para a nova posição
        matriz_temp[i] = matriz_cifrada[linha_atual]

    print("\nApós organizar linhas:")
    for i in matriz_temp:
        print(i)

    # Criar uma nova matriz vazia para armazenar a ordem correta das colunas
    matriz_final = [['' for _ in range(num_colunas)]
                    for _ in range(num_linhas)]

    # Agora desfazer a transposição de colunas
    for i in range(num_colunas):
        # A chave indica a posição original da coluna (acredito que deveria ser transposta tambem)
        coluna_atual = chave_colunas[i] - 1
        for j in range(num_linhas):
            matriz_final[j][coluna_atual] = matriz_temp[j][i]

    print("\nApós organizar colunas:")
    for i in matriz_final:
        print(i)

    # converter a matriz final em texto
    mensagem_original = ''
    for linha in matriz_final:
        mensagem_original += ''.join(linha)
    return mensagem_original


def cifrar_transposicao_dupla(texto, chave_colunas, chave_linhas):
    num_linhas = len(chave_linhas)
    num_colunas = len(chave_colunas)

    # converte a chave para sua versao inversa
    columntrans = chavetransposta(chave_colunas)
    rowtrans = chavetransposta(chave_linhas)

    # Garantir que o texto tenha o tamanho correto
    if len(texto) < num_linhas * num_colunas:
        texto = texto + 'X' * (num_linhas * num_colunas - len(texto))

    # Criar matriz inicial com o texto e completa com x
    matriz_original = []
    for i in range(0, len(texto), num_colunas):
        matriz_original.append(list(texto[i:i+num_colunas]))

    print("Matriz Original:")
    for linha in matriz_original:
        print(linha)

    # Organiza as linhas de acordo com a chave da coluna
    matriz_temp = [['' for _ in range(num_colunas)] for _ in range(num_linhas)]

    for i in range(num_colunas):
        # Nova posição baseada na chave da coluna transposta
        nova_posicao = columntrans[i] - 1
        for j in range(num_linhas):
            matriz_temp[j][nova_posicao] = matriz_original[j][i]

    print("\nApós organizar colunas:")
    for linha in matriz_temp:
        print(linha)

    # Organiza as linhas de acordo com a chave da linha
    matriz_final = [['' for _ in range(num_colunas)]
                    for _ in range(num_linhas)]
    for i in range(num_linhas):
        # Nova posição baseada na chave da linha transposta
        nova_posicao = rowtrans[i] - 1
        matriz_final[nova_posicao] = matriz_temp[i]  # Mover a linha

    print("\nApós organizar linhas:")
    for linha in matriz_final:
        print(linha)

    # Converter a matriz final em texto
    texto_cifrado = ''.join([''.join(linha) for linha in matriz_final])

    return texto_cifrado


# mesangens
cifra = "XMXAXOASMTJHEOVAORMU"
mensagem = "HOJEVAMOSTOMARUMA"

chave_colunas = [3, 1, 4, 2, 5]
chave_linhas = [4, 2, 1, 3]


msg_cifrada = cifrar_transposicao_dupla(mensagem, chave_colunas, chave_linhas)
print(f"\nMensagem cifrada: {msg_cifrada}")

msg_decifrada = decifrar_transposicao_dupla(cifra, len(
    chave_colunas), len(chave_linhas), chave_colunas, chave_linhas)
print(f"\nMensagem decifrada: {msg_decifrada}")
