class Node():
    def __init__(self, value, next= None):
        self.value = value
        self.next = next


class Linked():
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __repr__(self):
        tmp = self.head
        while tmp is not None:
            print(f"{tmp.value}", end="-->")
            tmp = tmp.next
        print('Null')
        return ''

if __name__ == '__main__':
    lk = Linked()
    lk.insert(Node(1))
    lk.insert(Node(2))
    print(lk)