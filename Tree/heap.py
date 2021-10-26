class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, node):

        if self is None:
            self = node
            return self
        elif self.data > node.data:
            self.right = Tree.insert(self.right, node)
        else:
            self.left = Tree.insert(self.left, node)
        return self

    def heap_insert(self, node):
        if self is None:
            self = node
            return self
        elif self.left is None:
            self.left = node
            if self.data >= self.left.data:
                tmp = self.data
                self.data = self.left.data
                self.left.data = tmp
            else:
                pass
            return self
        elif self.right is None:
            self.right = node
            if self.data >= self.left.data:
                tmp = self.data
                self.data = self.left.data
                self.left.data = tmp
            else:
                pass
            return self
        else:




    def display(self, lvl=0):
        if self is None:
            return

        if self.left is None and self.right is None:
            print("\t" * lvl + str(self.data))
            return

        Tree.display(self.right, 1+lvl)
        print("\t" * lvl + str(self.data))
        Tree.display(self.left, 1+lvl)


if __name__ == "__main__":
    tree = Tree(10)
    tree.insert(Tree(5))
    tree.insert(Tree(2))
    tree.insert(Tree(7))
    tree.insert(Tree(20))
    tree.insert(Tree(30))
    tree.insert(Tree(15))

    tree.display()