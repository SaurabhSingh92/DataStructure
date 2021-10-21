class treeNode():

    def __init__(self, Key):
        self.key = Key
        self.left = None
        self.right = None

    def tree_print(self, lvl=0):
        if self is None:
            return
        if self.left is None and self.right is None:
            print("\t" * lvl + str(self.key))
            return

        treeNode.tree_print(self.right, lvl + 1)
        print("\t" * lvl + str(self.key))
        treeNode.tree_print(self.left, lvl + 1)

    def touple_parse(data):
        if isinstance(data, tuple) and len(data) == 3:
            node = treeNode(data[1])
            node.left = treeNode.touple_parse(data[0])
            node.right = treeNode.touple_parse(data[2])
        elif data is None:
            node = None
        else:
            node = treeNode(data)

        return node

    def tree_height(self):
        if self is None:
            return 0

        return max(1 + treeNode.tree_height(self.left), 1 + treeNode.tree_height(self.right))

    def tot_tree_height(t):
        if t is None:
            return 0

        return 1 + treeNode.tot_tree_height(t.left) + treeNode.tot_tree_height(t.right)

    def inorder(self):
        if self is None:
            return []

        if self.left is None and self.right is None:
            return [self.key]

        return treeNode.inorder(self.left) + [self.key] + treeNode.inorder(self.right)

    def pre_order(self):
        if self is None:
            return []

        if self.left is None and self.right is None:
            return [self.key]

        return [self.key] + treeNode.pre_order(self.left) + treeNode.pre_order(self.right)

    def post_order(self):
        if self is None:
            return []

        if self.left is None and self.right is None:
            return [self.key]

        return treeNode.post_order(self.right) + [self.key] + treeNode.post_order(self.left)


if __name__ == "__main__":
    tp = ((1, 2, 3), 4, (5, 6, (7, 8, 9)))
    tree = treeNode.touple_parse(tp)

    tree.tree_print()

    print(f"\n Max Depth : {tree.tree_height()}")
    print(f"\n Total Depth : {tree.tot_tree_height()}")

    print(f"Inorder: {tree.inorder()}")
    print(f"PreOrder:{tree.pre_order()}")
    print(f"PostOrder:{tree.post_order()}")
