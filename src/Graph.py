class Vertex:
    def __init__(self, vertex):
        self.id = vertex
        self.adjacent = {}

    def __str__(self):
        return str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        if neighbor in self.adjacent:
            self.adjacent[neighbor].append(weight)
        else:
            self.adjacent[neighbor] = []
            self.adjacent[neighbor].append(weight)
        return self.adjacent
    '''
    def remove_neighbor(self, neighbor, cost):
        if neighbor in self.get_connections():
            self.adjacent[neighbor].remove(cost)
    '''

    def get_connections(self):
        key = self.adjacent.keys()
        keys = set()
        for i in key:
            keys.add(i.id)
        return keys

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert = {}
        self.size = 0

    def __iter__(self):
        return iter(self.vert.values())

    def add_vertex(self, node):
        self.size += 1
        new_vertex = Vertex(node)
        self.vert[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert:
            return self.vert[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert:
            self.add_vertex(frm)
        if to not in self.vert:
            self.add_vertex(to)

        self.vert[frm].add_neighbor(self.vert[to], cost)
        self.vert[to].add_neighbor(self.vert[frm], cost)

    def get_weight(self, frm, to):
        return self.vert[frm].get_weight(self.vert[to])

    def get_vertices(self):
        return self.vert.keys()

    def get_size(self):
        return self.size