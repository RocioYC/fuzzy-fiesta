from collections import deque

cuidades = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['G'],
    'G': []
}


def bfs(inicio,destino):
    cola= deque([[inicio]])
    visitados=set()

    while cola:
        camino=cola.popleft()
        actual=camino[-1]

        if actual==destino:
            return camino
        
        if actual==visitados:
            continue

        visitados.add(actual)

        for i in cuidades[actual]:
            cola.append(camino + [i])
    return None

camino= bfs('A','G')

if camino:
    print("camino", "->".join(camino))
else:
    print("no")
