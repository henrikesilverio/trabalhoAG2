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
# Calcular a distancia entre dois vertices


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


def ImprimirCaminho(verticeInicial, verticeFinal):
    if verticeFinal["nome"] == verticeInicial["nome"]:
        print(verticeInicial["nome"])
    elif not verticeFinal["predecessor"]:
        print("não existe caminho de {0} a {1}".format(
            verticeInicial["nome"], verticeFinal["nome"]))
    else:
        ImprimirCaminho(verticeInicial, verticeFinal["predecessor"])
        print(verticeFinal["nome"])


WFS(grafo, grafo[fonte])
ImprimirCaminho(grafo[fonte], grafo[sumidouro])
