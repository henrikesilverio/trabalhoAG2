arquivo = open("exemplo4.txt")

linhas = arquivo.read().split("\n")
definicoes = linhas[0].split(' ')
linhas = linhas[1:]

fonte = definicoes[2]
sumidouro = definicoes[3]
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
        aresta = linha.split(' ')
        if aresta[0] in grafo and type(grafo[aresta[0]]) is dict:
            grafo[aresta[0]]["adjacentes"][aresta[1]] = int(aresta[2])
        else:
            grafo[aresta[0]] = {
                "nome": aresta[0],
                "cor": "branco",
                "adjacentes": {aresta[1]: int(aresta[2])},
                "predecessor": {}
            }

# Inclui vertices separadores e arestas de avanço


def incluiVerticeSeparador():
    for vertice in grafo.copy().keys():
        for adjacente in grafo[vertice]["adjacentes"].keys():
            adjacentes = grafo[adjacente]["adjacentes"]
            if vertice in adjacentes and adjacentes[vertice] > 0:
                valor = int(grafo[adjacente]["adjacentes"][vertice])
                grafo[adjacente + vertice] = {
                    "nome": adjacente + vertice,
                    "cor": "branco",
                    "adjacentes": {vertice: valor},
                    "predecessor": {}
                }
                grafo[adjacente]["adjacentes"][adjacente + vertice] = valor
                del grafo[adjacente]["adjacentes"][vertice]


def incluiArestaDeAvanco():
    for vertice in grafo.keys():
        for adjacente in grafo[vertice]["adjacentes"].keys():
            if not vertice in grafo[adjacente]["adjacentes"]:
                grafo[adjacente]["adjacentes"][vertice] = 0


criarGrafo(linhas)
incluiVerticeSeparador()
incluiArestaDeAvanco()

# Busca em largura


def buscaEmLargura(grafo, verticeInicial):
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


def obtemCaminho():
    caminho = []
    vertice = grafo[sumidouro]
    while(vertice):
        caminho.insert(0, vertice["nome"])
        vertice = vertice["predecessor"]
    return caminho


def obtemGargalo(caminho):
    gargalo = 99999999999999
    for i in range(len(caminho) - 1):
        capacidade = grafo[caminho[i]]["adjacentes"][caminho[i + 1]]
        if capacidade < gargalo:
            gargalo = capacidade
    return gargalo


def limpaGrafo():
    for vertice in grafo:
        grafo[vertice]["cor"] = "branco"
        grafo[vertice]["predecessor"] = {}

# Algorito de fluxo


def fluxoMaximo():
    buscaEmLargura(grafo, grafo[fonte])
    caminho = obtemCaminho()
    maximo = 0
    while(len(caminho) > 1):
        gargalo = obtemGargalo(caminho)
        for i in range(len(caminho) - 1):
            # Fonte -> Sumidouro
            grafo[caminho[i]]["adjacentes"][caminho[i + 1]] -= gargalo
            # Sumidouro -> Fonte
            grafo[caminho[i + 1]]["adjacentes"][caminho[i]] += gargalo
        limpaGrafo()
        buscaEmLargura(grafo, grafo[fonte])
        caminho = obtemCaminho()
    for vertice in grafo[sumidouro]["adjacentes"].keys():
        maximo += grafo[sumidouro]["adjacentes"][vertice]
    return maximo


print(fluxoMaximo())