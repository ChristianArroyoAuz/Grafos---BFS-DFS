# 🔍 Algoritmos de Búsqueda en Grafos - BFS & DFS

## 🌳 Implementación Completa de Algoritmos de Traversión de Grafos

Una herramienta educativa avanzada que implementa y visualiza dos algoritmos fundamentales de búsqueda en grafos: **Breadth-First Search (BFS)** y **Depth-First Search (DFS)**, con múltiples modalidades de análisis y representación gráfica.

## 🎯 Características Principales

### 🔄 **Algoritmo BFS (Breadth-First Search)**
- **Estrategia**: Búsqueda por niveles - expansión radial
- **Óptimo para**: Encontrar el camino más corto en grafos no ponderados
- **Estructura de datos**: Cola (FIFO)
- **Complejidad**: O(V + E)

### 🏊 **Algoritmo DFS (Depth-First Search)**
- **Estrategia**: Búsqueda en profundidad - exploración recursiva
- **Óptimo para**: Detección de ciclos, ordenamiento topológico
- **Estructura de datos**: Pila (LIFO)
- **Complejidad**: O(V + E)

## 🛠️ Arquitectura del Sistema

### **Módulo BFS Principal**
1. **Búsqueda de Mejor Ruta**
   - Encuentra el camino más corto entre dos nodos
   - Visualización paso a paso del proceso
   - Cálculo del número mínimo de saltos

2. **Búsqueda de Todas las Rutas**
   - Enumera todos los caminos posibles entre nodos
   - Compara longitudes de rutas
   - Identifica la ruta óptima entre múltiples opciones

### **Módulo de Árboles de Búsqueda**
1. **Árbol BFS**
   - Representación jerárquica por niveles
   - Visualización de la expansión en anchura
   - Aplicación en grafos direccionales y no direccionales

2. **Árbol DFS**
   - Representación de exploración en profundidad
   - Visualización de caminos recursivos
   - Comparación con el enfoque BFS

## 📊 Tecnologías y Visualizaciones

### **Librerías Utilizadas**
- **NetworkX**: Construcción y manipulación de grafos
- **Matplotlib**: Visualización avanzada de grafos y árboles
- **Collections.deque**: Implementación eficiente de colas para BFS
- **Colorama**: Interfaz de usuario colorida en terminal

### **Características de Visualización**
- 🎨 Grafos direccionales y no direccionales
- 📍 Layouts automáticos y personalizados
- 🔄 Comparación lado a lado de diferentes estrategias
- 🎯 Highlighting de rutas encontradas
- 📊 Representación de árboles de búsqueda

## 🚀 Ejecución y Navegación

```bash
python Python_BFS_DFS.py
```

### **Menú Principal**
```
1. Algoritmo BFS
2. Árboles BFS y DFS  
0. Salir
```

### **Submenú BFS**
```
1. Búsqueda de la mejor ruta
2. Búsqueda de todas las rutas
9. Volver
0. Salir
```

### **Submenú Árboles**
```
1. Árbol BFS
2. Árbol DFS
9. Volver
0. Salir
```

## 💡 Casos de Uso y Aplicaciones

### **Aplicaciones de BFS**
- 🗺️ **Sistemas de Navegación**: GPS y planificación de rutas
- 🌐 **Redes Sociales**: Encontrar conexiones de grado mínimo
- 🎮 **Desarrollo de Videojuegos**: Pathfinding en grid-based games
- 🔗 **Análisis de Redes**: Medición de distancias entre nodos

### **Aplicaciones de DFS**
- 🔍 **Resolución de Laberintos**: Backtracking y exploración exhaustiva
- 📋 **Ordenamiento Topológico**: Dependencias en scheduling
- 🔄 **Detección de Ciclos**: Análisis de circuitos en grafos
- 🧩 **Resolución de Puzzles**: Sudoku, N-Queens problem

## 🎓 Valor Educativo

### **Para Estudiantes**
- ✅ Comprensión intuitiva de algoritmos fundamentales
- ✅ Visualización del proceso de búsqueda paso a paso
- ✅ Comparación directa entre BFS y DFS
- ✅ Ejemplos prácticos con grafos reales

### **Para Desarrolladores**
- 🔧 Implementación de referencia para proyectos
- 🎨 Templates de visualización de grafos
- 📚 Base para algoritmos más complejos (Dijkstra, A*)

## 📈 Ejemplos Incluidos

### **Grafo de Transformación de Palabras**
```
CAB → CAR → BAR → BAT
  ↘   ↘    ↙    ↙
   CAT → MAT → BAT
```
- **Propósito**: Demostrar búsqueda de rutas en grafos semánticos
- **Aplicación**: Algoritmos de corrección ortográfica, juegos de palabras

### **Grafo de Seis Nodos Interconectados**
- **Propósito**: Mostrar traversión completa y generación de árboles
- **Aplicación**: Análisis de conectividad en redes

## ⚡ Características Técnicas Avanzadas

### **Manejo de Errores Robusto**
- ✅ Validación de entrada de usuario
- ✅ Detección de nodos inexistentes
- ✅ Manejo de grafos desconectados
- ✅ Mensajes de error descriptivos

### **Optimizaciones Implementadas**
- 🚀 Uso de deque para colas eficientes en BFS
- 🎯 Almacenamiento de rutas para evitar recomputación
- 📊 Visualización optimizada con layouts automáticos
- 🔄 Limpieza de pantalla para mejor experiencia de usuario

---

**🔬 Herramienta esencial para el aprendizaje y aplicación de algoritmos de grafos en proyectos académicos y profesionales.**

*Perfecta para cursos de estructuras de datos, algoritmos, inteligencia artificial y ciencia de redes* 🌟
