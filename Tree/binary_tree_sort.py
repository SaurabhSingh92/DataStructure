class BSTNode():
    def __init__(self, Key, Value=None):
        self.key = Key
        self.Value = Value
        self.left = None
        self.right = None
        self.parent = None

    @staticmethod
    def remove_none(lst):
        return [x for x in lst if x is not None]

    def check_BSTNode(self):
        if self is None:
            return True, None, None

        is_BSTNode_l, max_l, min_l = BSTNode.check_BSTNode(self.left)
        is_BSTNode_r, max_r, min_r = BSTNode.check_BSTNode(self.right)

        is_BSTNode = (is_BSTNode_l and is_BSTNode_r and (max_l is None or max_l < self.key) and (
                    min_l is None or min_r > self.key))
        min_key = min(BSTNode.remove_none([min_l, self.key, min_r]))
        max_key = max(BSTNode.remove_none([max_l, self.key, max_r]))

        return is_BSTNode, max_key, min_key

    def display(self, lvl=0):
        if self is None:
            return

        if self.right is None and self.left is None:
            print("\t" * lvl + str(self.key))
            return

        BSTNode.display(self.right, lvl + 1)
        print("\t" * lvl + str(self.key))
        BSTNode.display(self.left, lvl + 1)

    @staticmethod
    def parse(data):
        if isinstance(data, tuple) and len(data) == 3:
            node = BSTNode(data[1])
            node.left = BSTNode.parse(data[0])
            node.right = BSTNode.parse(data[2])
            node.left.parent = node
            node.right.parent = node
        elif data is None:
            node = None
        else:
            node = BSTNode(data)
        return node

    def insert(self, key, value=None):
        if self is None:
            self = BSTNode(key, value)
        elif self.key > key:
            self.left = BSTNode.insert(self.left, key, value)
            self.left.parent = self
        elif self.key < key:
            self.right = BSTNode.insert(self.right, key, value)
            self.right.parent = self
        return self

    def find(self, key):
        if self is None:
            return False
        elif self.key == key:
            return True
        elif self.key<key:
            return BSTNode.find(self.right, key)
        else:
            return BSTNode.find(self.left, key)


if __name__ == "__main__":
    print(f"Input Range :")
    k = BSTNode.insert(None, 7)
    k.insert(1)
    k.insert(9)
    k.insert(4)
    k.insert(10)
    k.insert(8)

    k.display()

    print(f"\n\n Find- { k.find(0) }")



