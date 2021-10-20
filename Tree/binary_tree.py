class treeNode():
    def __init__(self, Key):
        self.key = Key
        self.left = None
        self.right = None


def display_tree(node, lvl=0):
    if node is None:
        print("")
        return

    if isinstance(node, (int)):
        print("\t" * lvl + str(node))
        return

    if node.left is None and node.right is None:
        print("\t" * lvl + str(node.key))
        return

    display_tree(node.right, lvl + 1)
    display_tree(node.key, lvl)
    display_tree(node.left, lvl + 1)


def tuple_parse(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = treeNode(data[1])
        node.left = tuple_parse(data[0])
        node.right = tuple_parse(data[2])
    elif data is None:
        node = None
    else:
        node = treeNode(data)
    return node


def inorder_traversal(node):
    if node is None:
        return

    if node.left is None and node.right is None:
        print(node.key)
        return

    inorder_traversal(node.left)
    print(node.key)
    inorder_traversal(node.right)


def preorder_traversal(node):
    if node is None:
        return

    if node.left is None and node.right is None:
        print(node.key)
        return

    print(node.key)
    preorder_traversal(node.left)
    preorder_traversal(node.right)


if __name__ == '__main__':
    dt = ((3, 2, 4), 1, ((7, 6, 11), 5, (9, 8, 10)))
    tree = tuple_parse(dt)
    display_tree(tree)

    # in_ord = inorder_traversal(tree)
    preord = preorder_traversal(tree)
