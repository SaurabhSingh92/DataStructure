class DFSgraph():
    def __init__(self, node, edges):
        self.node = node
        self.size = len(node)
        self.data = [[] for x in range(self.size)]
        for i, v in edges:
            self.data[i].append(v)
            self.data[v].append(i)

    def dfs(self, root):
        stack = []
        discover = [False] * self.size
        result = []
        stack.append(root)

        while len(stack) > 0:
            current = stack.pop()
            if not discover[current]:
                discover[current] = True
                result.append(current)
                for n in self.data[current]:
                    stack.append(n)
        return result

    def __repr__(self):
        return '\n'.join(["{} : {}".format(i, v) for i, v in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    node = [i for i in range(5)]
    edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

    graph = DFSgraph(node, edges)

    print(graph)

    print(graph.dfs(3))
