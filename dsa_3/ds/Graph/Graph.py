class Graph:
    def __init__(self):
        self.graph = {}
        
    
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edges(self, vertex_1, vertex_2):
        if vertex_1 not in self.graph:
            self.add_vertex(vertex_1)
        
        if vertex_2 not in self.graph:
            self.add_vertex(vertex_2)

        self.graph[vertex_1].append(vertex_2)
        self.graph[vertex_2].append(vertex_1)
    
    def display(self):
        for vertex, value in self.graph.items():
            print(f'{vertex} --> {value}')
            
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edges('A', 'B')
g.add_edges('A', 'C')
g.add_edges('B', 'C')
g.display()   