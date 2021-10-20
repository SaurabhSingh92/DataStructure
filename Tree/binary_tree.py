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
        print("\t"*lvl+str(node))
        return

    if node.left is None and node.right is None:
        print("\t"*lvl+str(node.key))
        return

    display_tree(node.right, lvl+1)
    display_tree(node.key, lvl)
    display_tree(node.left, lvl+1)

def tuple_parse(data):
    if isinstance(data, tuple) and len(data)==3:
        node = treeNode(data[1])
        node.left = tuple_parse(data[0])
        node.right = tuple_parse(data[2])
    elif data is None:
        node = None
    else:
        node = treeNode(data)
    return node

dt=((3,2,4),1,((7,6,11),5,(9,8,10)))

tree = tuple_parse(dt)

display_tree(tree)





