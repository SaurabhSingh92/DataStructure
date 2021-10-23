class Gmatrix():
    def __init__(self, node, edges):
        self.node = node
        self.data = [[0 for _ in range(len(node))] for _ in range(len(node))]
        for i, v in edges:
            self.data[i][v] = 1
            self.data[v][i] = 1

    def __repr__(self):
        for i in range(len(self.node)):
            for j in range(len(self.node)):
                print(f"{self.data[i][j]}", end="", sep="\t")
            print("\n")
        return ''

    def __str__(self):
        return self.__repr__()

if __name__ == "__main__":
    node = [_ for _ in range(5)]
    edges = [(0,1), (0,4),(1,3), (1,2), (3,2), (1,4), (3,4)]

    graph = Gmatrix(node, edges)
    print(graph)
