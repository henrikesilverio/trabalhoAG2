arquivo = open("exemplo1.txt")

linhas = arquivo.read().split("\n")
definicoes = linhas[0].split(' ')
linhas = linhas[1:]

fonte = definicoes[0]
sumidouro = definicoes[1]
arquivo.close()
grafo = {}
grafo[fonte] = {
    "nome": fonte,
    "cor": "branco",
    "adjacentes": {},
    "predecessor": {}
}
grafo[sumidouro] = {
    "nome": sumidouro,
    "cor": "branco",
    "adjacentes": {},
    "predecessor": {}
}

# Construindo o grafo


def criarGrafo(linhas):
    for linha in linhas:
        vertices = linha.split(' ')
        if vertices[0] in grafo and type(grafo[vertices[0]]) is dict:
            grafo[vertices[0]]["adjacentes"][vertices[1]] = int(vertices[2])
        else:
            grafo[vertices[0]] = {
                "nome": vertices[0],
                "cor": "branco",
                "adjacentes": {vertices[1]: int(vertices[2])},
                "predecessor": {}
            }

# Inclui arestas de avanço


def incluiArestaDeAvanco(grafo):
    for vertice in grafo.keys():
        for adjacente in grafo[vertice]["adjacentes"].keys():
            if not vertice in grafo[adjacente]["adjacentes"]:
                grafo[adjacente]["adjacentes"][vertice] = 0


criarGrafo(linhas)
incluiArestaDeAvanco(grafo)

# Busca em largura


def WFS(grafo, verticeInicial):
    fila = []
    verticeInicial["cor"] = "cinza"
    fila.append(verticeInicial)
    while(len(fila) != 0):
        vertice = fila.pop(0)
        for adjacente in vertice["adjacentes"].keys():
            valor = grafo[vertice["nome"]]["adjacentes"][adjacente]
            if grafo[adjacente]["cor"] == "branco" and valor != 0:
                grafo[adjacente]["cor"] = "cinza"
                grafo[adjacente]["predecessor"] = vertice
                fila.append(grafo[adjacente])
        vertice["cor"] = "preto"

# funções auxiliares


def ObtemCaminho():
    caminho = []
    vertice = grafo[sumidouro]
    while(vertice):
        caminho.insert(0, vertice["nome"])
        vertice = vertice["predecessor"]
    return caminho


def ObtemGargalo(caminho):
    gargalo = 99999999999999
    for i in range(len(caminho) - 1):
        capacidade = grafo[caminho[i]]["adjacentes"][caminho[i + 1]]
        if capacidade < gargalo:
            gargalo = capacidade
    return gargalo


def LimpaGrafo():
    for vertice in grafo:
        grafo[vertice]["cor"] = "branco"
        grafo[vertice]["predecessor"] = {}

# Algorito de fluxo


def Fluxo():
    WFS(grafo, grafo[fonte])
    caminho = ObtemCaminho()
    while(len(caminho) > 1):
        gargalo = ObtemGargalo(caminho)
        for i in range(len(caminho) - 1):
            # Fonte -> Sumidouro
            grafo[caminho[i]]["adjacentes"][caminho[i + 1]] -= gargalo
            # Sumidouro -> Fonte
            grafo[caminho[i + 1]]["adjacentes"][caminho[i]] += gargalo
        LimpaGrafo()
        WFS(grafo, grafo[fonte])
        caminho = ObtemCaminho()

Fluxo()
