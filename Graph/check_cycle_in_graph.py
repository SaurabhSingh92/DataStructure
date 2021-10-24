class Graph():
    def __init__(self, node, edges):
        self.node = node
        self.size = len(node)
        self.data = [[] for _ in range(self.size)]
        for i, v in edges:
            self.data[i].append(v)
            self.data[v].append(i)

    def cycle_check(self, idx=0):
        stack = []
        discovered = [False] * self.size
        result = []
        stack.append(idx)

        while len(stack) > 0:
            print(f"Stack : {stack} ")
            curr = stack.pop()
            print(curr)
            if not discovered[curr]:
                discovered[curr] = True
                result.append(curr)
                for n in self.data[curr]:
                    stack.append(n)
            print(f"Result :{result}")
        return False

    def __repr__(self):
        return '\n'.join(["{} : {}".format(i,v) for i,v in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    node = [ i for i in range(5) ]
    edges = [(0,1), (0,2), (0,3), (1,2), (3,4)]

    graph = Graph(node, edges)
    print(graph.cycle_check())