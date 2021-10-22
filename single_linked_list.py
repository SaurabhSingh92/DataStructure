class Node():
    def __init__(self, value, next=None):
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

    def delete(self, val):
        tmp = self.head
        idx = self.find(tmp, tmp.value, 0)
        for _ in range(idx):
            tmp = tmp.next
        tmp.next = tmp.next.next

    def update(self, val, idx):
        tmp = self.head
        for _ in range(idx):
            tmp = tmp.next
        tmp.value = val

    def find(self, head, data, idx=0 ):
        if head.value == data:
            return idx
        else:
            if head.next:
                return self.find(head.next, head.value, idx+1)
            else:
                raise ValueError("Not Found")


    def size(self):
        cnt = 0
        tmp = self.head
        while tmp.next is not None:
            cnt += 1
            tmp = tmp.next
        return cnt

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
    lk.insert(Node(4))
    lk.update(99,2)
    print(lk)
    lk.delete(2)
    print(lk)