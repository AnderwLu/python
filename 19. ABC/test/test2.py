from abc import ABC, abstractmethod

class Sequence(ABC):
    @abstractmethod
    def append(self, item):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    def is_empty(self):
        return self.length() == 0

# 实现 LinkedListSequence（基于链表）
class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
    def __str__(self):
        return f"{self.value} : {self.next}"
class LinkedListSequence(Sequence):
    def __init__(self):
        super().__init__()
        self.node = None

    def append(self, item):
        if self.node:
            n = Node(item)
            n.next = self.node
            self.node = n
        else:
            self.node = Node(item)

    def get(self, index):
        inx = 0
        for i in self:
            if inx == index:
                return i
            inx += 1
        return None

    def length(self):
        index = 0
        for i in self:
            index += 1
        return index

    def __iter__(self):
        now = self.node
        while now:
            yield now
            now = now.next

link = LinkedListSequence()
link.append(5)
link.append(6)
print(link.get(1))
print(link.length())
for i in link:
    print(i)

print(link.is_empty())