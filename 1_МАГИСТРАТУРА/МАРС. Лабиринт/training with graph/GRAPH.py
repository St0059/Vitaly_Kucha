
class Graph():
    def __init__(self, directed = True):
        self.directed = directed
        self.edges_list = []

    def add_edge(self, node_0, node_1, x_1, y_1, directions = {}):
        self.edges_list.append([node_0, node_1, x_1, y_1, directions])
        if not self.directed:
            self.edges_list.append([node_0, node_1, x_1, y_1, directions])

    def print_edge_list(self):
        for i in range(len(self.edges_list)):
            directs = [*self.edges_list[i][4]]
            print(f'Edge {i+1} : Кординаты х, у узла {self.edges_list[i][1]} = '
                  f'[{self.edges_list[i][2]},{self.edges_list[i][3]}]\n'
                  f'Узел имеет направления {directs[0]}')

graph = Graph()

graph.add_edge(0, 0, 0, 0, {'Forward': 'Free'})
graph.add_edge(0, 1, 2, 0, {'Forward': 'Занято', 'Left': 'Free', 'Right': 'Free'})
graph.add_edge(1, 2, 4, 0, {'Forward': 'Free'})
graph.add_edge(1, 3, 2, -2, {'Forward': 'Free'})
graph.add_edge(1, 4, 0, 0, {'Forward': 'Free'})

graph.print_edge_list()
