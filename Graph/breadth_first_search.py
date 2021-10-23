class Graph:
    def __init__(self, node, edges):
        self.node = node
        self.n = len(node)
        self.data = [ [] for _ in range(self.n)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def bfs(self, node):
        dq = []
        parent=[]
        dist = [0] * self.n
        discovered = [False] * self.n
        discovered[node] = True
        parent.append(0)
        dist[node]=0
        dq.append(node)
        idx = 0
        while idx < self.n:
            current = dq[idx]
            idx += 1

            for node in self.data[current]:

                if not discovered[node]:
                    dq.append(node)
                    parent.append(current)
                    dist[node]=1+dist[current]
                    discovered[node] = True

        return dq, parent, dist

    def __repr__(self):
        return '\n'.join(["{}.{}".format(i, v) for i, v in self.data])

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    node = [i for i in range(5)]
    edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

    graph = Graph(node, edges)

    print(graph.bfs(3))
