class Graph():
    def __init__(self, nodes, edges):
        self.node = nodes
        self.data = [ [] for _ in range(len(nodes))]
        for i,val in edges:
            self.data[i].append(val)
            self.data[val].append(i)

    def insert(self, edge):
        for i, val in edge:
            self.data[i].append(val)
            self.data[val].append(i)

    def __repr__(self):
        return '\n'.join([ "{}:{}".format(i,v) for i,v in enumerate(self.data) ])

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    node = [_ for _ in range(5)]
    edges = [(0,1), (0,4),(1,3), (1,2), (3,2), (1,4), (3,4)]

    graph = Graph(node, edges)
    graph.insert([(0,2)])
    print(graph)
    graph