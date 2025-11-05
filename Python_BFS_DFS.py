from IPython.display import clear_output
import matplotlib.pyplot as plt
from collections import deque
from colorama import Fore
import networkx as nx
import sys

def base():
    print("                                                   ")
    print(Fore.BLUE + '\t\t\t ALGRITMOS BFS & DFS \t\t\t')
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para el Algoritmo BFS.')
    print('\t 2. Ingrese "2" para los Arboles BFS y DFS.')
    print('\t 3. Ingrese "0" para Salir.')
    opcion_ingresada_bfs_dfs = input("\t  " + "¿Cual es tu opción?: ")
    if opcion_ingresada_bfs_dfs.isdigit() & len(opcion_ingresada_bfs_dfs) != 0:
        clear_output(wait=True)
        tipo_seleccion(int(opcion_ingresada_bfs_dfs))
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        base()

def bfs():
    print("                                                   ")
    print(Fore.BLUE + "\t\t\t     ALGORITMO BFS      \t\t\t")
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para busqueda de la mejor ruta.')
    print('\t 2. Ingrese "2" para busqueda de todas las rutas.')
    print('\t 3. Ingrese "9" para Volver.')
    print('\t 4. Ingrese "0" para Salir.')
    opcion_ingresada_bfs = input("\t  " + "¿Cual es tu opción?: ")
    if opcion_ingresada_bfs.isdigit() & len(opcion_ingresada_bfs) != 0:
        clear_output(wait=True)
        seleccion_bfs(int(opcion_ingresada_bfs))
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        bfs()

def mejor_ruta():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t DETERMINACIÓN DE LA MEJOR RUTA CON BFS \t\t\t' + Fore.BLACK)
    print(Fore.BLACK + 'Información del Proceso:')
    print('\t A. Se elige el nodo de incicio.')
    print('\t B. Se elige el nodo final.')
    print('\t C. Se observa la ruta más corta.')
    print('\t D. Escribir los nodos como se encuentran en el grafo.')
    print("                                   ")
    print(Fore.GREEN + "\t\t\t GRAFO A SER ANALIZADO \t\t\t" + Fore.BLACK)
    G = nx.DiGraph()
    edges = [["CAB", "CAR"], ["CAB", "CAT"], ["CAR", "CAT"], ["CAR", "BAR"], ["CAT", "BAT"], ["BAR", "BAT"], ["CAT", "MAT"], 
             ["MAT", "BAT"]]
    G.add_edges_from(edges)
    ubicacion_nodos = {"CAB":(0,0), "CAR":(1,0), "CAT":(1,1), "BAR":(2,0), "BAT":(2,1), "MAT":(1,2)}
    nx.draw(G, ubicacion_nodos, edge_color = 'black', width = 1, linewidths = 1, node_size = 500, node_color = 'pink',
            alpha = 0.9, labels = {node : node for node in G.nodes()})
    plt.axis('on')
    plt.show()
    print("                                   ")
    nodo_inicio = input("\t    " + "Escriba el nombre del nodo de inicio: ")
    nodo_final =  input("\t    " + "Escriba el nombre del nodo de fin: ")
    if len(nodo_inicio) or len(nodo_final):
        print("                                   ")
        def BFS(grafo, inicio, final):
            print("Nodo Inicio: " + inicio)
            print("Nodo Final: " + final)
            if inicio == final:
                print(Fore.GREEN + "\n" + "El Camino más corto entre " + inicio + " y " + final + " es: " + Fore.BLACK)
                return [inicio]
            visitados = {inicio}
            cola = deque([(inicio, [])])
            while cola:
                current, ruta = cola.popleft()
                print("\nNodo Revisado: " + current)
                visitados.add(current)
                try:
                    for vecinos in grafo[current]:
                        print("\t Vecino " + "de " + inicio + " es: " + str(vecinos))
                        if vecinos == final:
                            print(Fore.GREEN + "\n" + "El Camino más corto entre " + inicio + " y " + final + " es: " + Fore.BLACK)
                            return ruta + [current, vecinos]
                        if vecinos in visitados:
                            continue
                        cola.append((vecinos, ruta + [current]))
                        visitados.add(vecinos)
                except:
                    print(Fore.RED + "\nOcurrio un error en la ejecución:" + Fore.BLACK)
                    print(Fore.RED + "\t No se encontro conexión entre los nodos ingresados" + Fore.BLACK)
                    print(Fore.RED + "\t Uno o los dos nodos ingresados no se encuentran en el grafo" + Fore.BLACK)
            return None
        if __name__ == '__main__':
            grafo = {"CAB" : ["CAR", "CAT"], "CAR" : ["CAT", "BAR"], "CAT" : ["BAT", "MAT"], "BAR" : ["BAT"], "MAT" : ["BAT"]}
            ruta = BFS(grafo, nodo_inicio, nodo_final)
            if ruta:
                print(Fore.GREEN + str(ruta) + Fore.BLACK)
                print(Fore.GREEN + "Con un número de saltos igual a: " + str(len(ruta) - 1) + Fore.BLACK)
            else:
                print(Fore.RED + "\nRuta No Encontrada." + Fore.BLACK)
        salir()
    else:
        clear_output(wait=True)
        print("                                                                                         ")
        print(Fore.RED + "\t  Opción Erronea - No se ingreso correctamente los nodos.  \t\n" + Fore.BLACK)
        mejor_ruta()

def todas_rutas():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t DETERMINACIÓN DE TODAS LAS RUTAS CON BFS \t\t\t' + Fore.BLACK)
    print(Fore.BLACK + 'Información del Proceso:')
    print('\t A. Se elige el nodo de incicio.')
    print('\t B. Se elige el nodo final.')
    print('\t C. Se observa la ruta más corta.')
    print('\t D. Escribir los nodos como se encuentran en el grafo.')
    print("                                   ")
    print(Fore.GREEN + "\t\t\t GRAFO A SER ANALIZADO \t\t\t" + Fore.BLACK)
    G = nx.DiGraph()
    edges = [["CAB", "CAR"], ["CAB", "CAT"], ["CAR", "CAT"], ["CAR", "BAR"], ["CAT", "BAT"], ["BAR", "BAT"], ["CAT", "MAT"], 
             ["MAT", "BAT"]]
    G.add_edges_from(edges)
    ubicacion_nodos = {"CAB":(0,0), "CAR":(1,0), "CAT":(1,1), "BAR":(2,0), "BAT":(2,1), "MAT":(1,2)}
    nx.draw(G, ubicacion_nodos, edge_color = 'black', width = 1, linewidths = 1, node_size = 500, node_color = 'pink',
            alpha = 0.9, labels = {node : node for node in G.nodes()})
    plt.axis('on')
    plt.show()
    print("                                   ")
    nodo_inicio = input("\t    " + "Escriba el nombre del nodo de inicio: ")
    nodo_final =  input("\t    " + "Escriba el nombre del nodo de fin: ")
    if len(nodo_inicio) or len(nodo_final):
        print("                                   ")
        print("Nodo Inicio: " + nodo_inicio)
        print("Nodo Final: " + nodo_final)
        def todasRutas(grafo, inicio, final, ruta=[]):
            ruta = ruta + [inicio]
            if inicio == final:
                return [ruta]
            if inicio not in grafo:
                print(Fore.RED + "\n\t Ocurrio un error en la ejecución:" + Fore.BLACK)
                print(Fore.RED + "\t No se encontro conexión entre los nodos ingresados" + Fore.BLACK)
                print(Fore.RED + "\t Uno o los dos nodos ingresados no se encuentran en el grafo" + Fore.BLACK)
                salir()
            rutas = []
            for nodo in grafo[inicio]:
                if nodo not in ruta:
                    camino_nuevo = todasRutas(grafo, nodo, final, ruta)
                    for otro_camino in camino_nuevo:
                        rutas.append(otro_camino)
            return rutas       
        def min_ruta(grafo, inicio, final):
            rutas = todasRutas(grafo,inicio,final)
            limite_superior = 10**99
            mi_camino = []
            contador = 0
            print("\nTodas las rutas posibles desde " + inicio + " hasta " + final + " son: ")
            for ruta in rutas:
                contador = contador + 1
                total = sum(grafo[i][j] for i,j in zip(ruta,ruta[1::]))
                print ("\t Ruta " + str(contador) + ":", ruta, "\n\t\t  Con un total de: " + str(total) + " saltos.\n")
                if total < limite_superior: 
                    limite_superior = total
                    mi_camino = ruta
            camino = str(mi_camino)
            saltos = str(sum(grafo[i][j] for i, j in zip(mi_camino, mi_camino[1::])))
            print (Fore.GREEN + "El Camino más corto entre: " + nodo_inicio + " y " + nodo_final + " es: " + "\n" + camino + Fore.BLACK)
            print (Fore.GREEN + "Con un número de saltos igual a: " + saltos + Fore.BLACK)  
        edges = [["CAB", "CAR"], ["CAB", "CAT"], ["CAR", "CAT"], ["CAR", "BAR"], ["CAT", "BAT"], ["BAR", "BAT"], ["CAT", "MAT"], 
             ["MAT", "BAT"]]
        if __name__ == "__main__":
            grafo = {"CAB" : {"CAR" : 1, "CAT" : 1},
                     "CAR" : {"CAT" : 1, "BAR" : 1},
                     "CAT" : {"BAT" : 1, "MAT" : 1},
                     "BAR" : {"BAT" : 1},
                     "MAT":  {"BAT" : 1}}
            min_ruta(grafo, nodo_inicio, nodo_final)
        salir()
    else:
        clear_output(wait=True)
        print("                                                                                         ")
        print(Fore.RED + "\t  Opción Erronea - No se ingreso correctamente los nodos.  \t\n" + Fore.BLACK)
        todas_rutas()
    
def arboles():
    print("                                                   ")
    print(Fore.BLUE + "\t\t\t     ARBOLES BFS y DFS     \t\t\t")
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para Arbol BFS.')
    print('\t 2. Ingrese "2" para Arbol DFS.')
    print('\t 3. Ingrese "9" para Volver.')
    print('\t 4. Ingrese "0" para Salir.')
    opcion_ingresada_arbol = input("\t  " + "¿Cual es tu opción?: ")
    if opcion_ingresada_arbol.isdigit():
        clear_output(wait=True)
        seleccion_dfs(int(opcion_ingresada_arbol))
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        arboles()    

def arbolBFS():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t ARBOL BFS - BREADTH FIRST SEARCH - BÚSQUEDA EN ANCHURA \t\t\t' + Fore.BLACK)
    print("                                   ")
    print(Fore.GREEN + "\t\t\t GRAFO DIRECCIONAL A SER ANALIZADO \t\t\t" + Fore.BLACK)
    G = nx.DiGraph()
    edges = [["0", "1"], ["1", "0"], ["0", "2"], ["2", "0"], ["0", "5"], ["5", "0"], ["2", "3"], ["3", "2"], ["2", "4"], ["4", "2"],
             ["5", "3"], ["3", "5"], ["3", "4"], ["4", "3"], ["1", "2"], ["2", "1"]]
    G.add_edges_from(edges)
    ubicacion_nodos = {"0":(0,1), "1":(1,0.5), "2":(2,1), "3":(1,0), "4":(2,0), "5":(0,0)}
    nx.draw(G, ubicacion_nodos, edge_color = 'black', width = 1, linewidths = 1, node_size = 500, node_color = 'pink', alpha = 0.9, 
            labels = {node : node for node in G.nodes()})
    plt.axis('on')
    plt.show()
    print("                                   ")
    print(Fore.GREEN + "\t\t\t GRAFO NO DIRECCIONAL BFS A SER ANALIZADO \t\t\t" + Fore.BLACK)
    print('Resultado despues del análisis')
    G = nx.Graph()
    edges = [["0", "1"], ["1", "0"], ["0", "2"], ["2", "0"], ["0", "5"], ["5", "0"], ["2", "3"], ["3", "2"], ["2", "4"], ["4", "2"],
             ["5", "3"], ["3", "5"], ["3", "4"], ["4", "3"], ["1", "2"], ["2", "1"]]
    G.add_edges_from(edges)
    ubicacion_nodos = {"0":(0,1), "1":(1,0.5), "2":(2,1), "3":(1,0), "4":(2,0), "5":(0,0)}
    nx.draw(G, ubicacion_nodos, edge_color = 'black', width = 1, linewidths = 1, node_size = 500, node_color = 'pink', alpha = 0.9,
            labels = {node : node for node in G.nodes()})
    plt.axis('on')
    plt.show()
    print("                                   ")
    print(Fore.GREEN + "\t\t\t ARBOL BFS DEL GRAFO \t\t\t" + Fore.BLACK)
    print('Resultado despues del análisis')
    G = nx.Graph()
    G = nx.Graph()
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(0,5)
    G.add_edge(2,3)
    G.add_edge(2,4)
    G.add_edge(5,3)
    G.add_edge(3,4)
    G.add_edge(1,2)
    pos = nx.spring_layout(G, seed = 70)
    nx.draw(nx.bfs_tree(G, 0), pos, with_labels = True)
    plt.axis('on')
    plt.show()
    salir()

def arbolDFS():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t ARBOL DFS - DEPTH FIRST SEARCH - BÚSQUEDA EN PROFUNDIDAD \t\t\t' + Fore.BLACK)
    print("                                   ")
    print(Fore.GREEN + "\t\t\t GRAFO DIRECCIONAL A SER ANALIZADO \t\t\t" + Fore.BLACK)
    G = nx.DiGraph()
    edges = [["0", "1"], ["1", "0"], ["0", "2"], ["2", "0"], ["0", "5"], ["5", "0"], ["2", "3"], ["3", "2"], ["2", "4"], ["4", "2"],
             ["5", "3"], ["3", "5"], ["3", "4"], ["4", "3"], ["1", "2"], ["2", "1"]]
    G.add_edges_from(edges)
    ubicacion_nodos = {"0":(0,1), "1":(1,0.5), "2":(2,1), "3":(1,0), "4":(2,0), "5":(0,0)}
    nx.draw(G, ubicacion_nodos, edge_color = 'black', width = 1, linewidths = 1, node_size = 500, node_color = 'pink', alpha = 0.9, 
            labels = {node : node for node in G.nodes()})
    plt.axis('on')
    plt.show()
    print("                                   ")
    print(Fore.GREEN + "\t\t\t GRAFO NO DIRECCIONAL DFS A SER ANALIZADO \t\t\t" + Fore.BLACK)
    print('Resultado despues del análisis')
    G = nx.Graph()
    edges = [["0", "1"], ["1", "0"], ["0", "2"], ["2", "0"], ["0", "5"], ["5", "0"], ["2", "3"], ["3", "2"], ["2", "4"], ["4", "2"],
             ["5", "3"], ["3", "5"], ["3", "4"], ["4", "3"], ["1", "2"], ["2", "1"]]
    G.add_edges_from(edges)
    ubicacion_nodos = {"0":(0,1), "1":(1,0.5), "2":(2,1), "3":(1,0), "4":(2,0), "5":(0,0)}
    nx.draw(G, ubicacion_nodos, edge_color = 'black', width = 1, linewidths = 1, node_size = 500, node_color = 'pink', alpha = 0.9,
            labels = {node : node for node in G.nodes()})
    plt.axis('on')
    plt.show()
    print(Fore.GREEN + "\t\t\t ARBOL DFS DEL GRAFO \t\t\t" + Fore.BLACK)
    print('Resultado despues del análisis')
    G = nx.Graph()
    G = nx.Graph()
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(0,5)
    G.add_edge(2,3)
    G.add_edge(2,4)
    G.add_edge(5,3)
    G.add_edge(3,4)
    G.add_edge(1,2)
    pos = nx.spring_layout(G, seed = 50)
    nx.draw(nx.dfs_tree(G, 0), pos, with_labels = True)
    plt.axis('on')
    plt.show()
    salir()
    
def default_1():
    clear_output(wait = True)
    print(Fore.RED + "                                                                    ")
    print(Fore.RED + "\t  Opción Erronea - Ingrese una de las opciones establecidas.  \t\n")
    base()

def default_2():
    clear_output(wait = True)
    print(Fore.RED + "                                                                    ")
    print(Fore.RED + "\t  Opción Erronea - Ingrese una de las opciones establecidas.  \t\n")
    bfs()
    
def default_3():
    clear_output(wait = True)
    print(Fore.RED + "                                                                    ")
    print(Fore.RED + "\t  Opción Erronea - Ingrese una de las opciones establecidas.  \t\n")
    arboles()

def tipo_seleccion(numero_0):
    return opciones_bfs_o_arboles.get(numero_0, default_1)()

def seleccion_bfs(numero_1):
    return algoritmo_bfs.get(numero_1, default_2)()

def seleccion_dfs(numero_2):
    return arboles_bfs_dfs.get(numero_2, default_3)()

def salir():
    print("                                                     ")
    print(Fore.BLUE + '\t\t\t ADIÓS HASTA LA PRÓXIMA \t\t\t' + Fore.BLACK)
    sys.exit()

def volver():
    clear_output(wait=True)
    base()

opciones_bfs_o_arboles = {
    1: bfs,
    2: arboles,
    0: salir
    }

algoritmo_bfs = {
    1: mejor_ruta,
    2: todas_rutas,
    9: volver,
    0: salir
    }

arboles_bfs_dfs = {
    1: arbolBFS,
    2: arbolDFS,
    9: volver,
    0: salir
    }

base()