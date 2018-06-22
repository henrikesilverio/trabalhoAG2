arquivo = open("exemplo1.txt")

linhas = arquivo.read().split("\n")
definicoes = linhas[0].split(' ')
linhas = linhas[1:]

fonte = definicoes[0]
sumidouro = definicoes[1]
arquivo.close()
grafo = {}
grafo[fonte] = {}
grafo[sumidouro] = {}

def criarGrafo(linhas):
    for linha in linhas:
        vertices = linha.split(' ')
        if vertices[0] in grafo and type(grafo[vertices[0]]) is dict:
            grafo[vertices[0]][vertices[1]] = vertices[2]
        else:
            grafo[vertices[0]] = { vertices[1]: vertices[2] }

criarGrafo(linhas)
print(grafo)