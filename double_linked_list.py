class Node():
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class Dlinked():
    def __init__(self):
        self.head = None

    def insert(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            tmp = self.head
            node.next = self.head
            tmp.prev = node
            self.head = node

    def find(self, tmp, val, idx=0):
        if tmp is None:
            return "Not Found"
        elif tmp.value == val:
            return idx
        else:
            return self.find(tmp.next, val, idx+1)

    def delete(self, val):
        tmp = self.head
        idx = self.find(self.head, val)

        if idx == "Not Found":
            print( "No such node" )
        elif val == 0:
            self.head = tmp.next
        else:
            for _ in range(idx-1):
                tmp = tmp.next

            tmp.next = tmp.next.next
            tmp.next.prev = tmp.prev

    def size(self, tmp, idx=1):
        if tmp is not None:
            return self.size(tmp.next, idx+1)
        else:
            return idx

    def __repr__(self):
        tmp = self.head
        while tmp:
            print( tmp.value, end="-->")
            tmp = tmp.next
        print("Null")
        return ''

if __name__ == "__main__":
    dl = Dlinked()
    for i in range(8):
        dl.insert(i)
    print(dl)
    print(dl.find(dl.head, 2))
    dl.delete(2)
    print(dl)
    print(dl.size(dl.head))