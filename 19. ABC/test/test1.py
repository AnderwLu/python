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

# 实现 ListSequence（基于 Python 列表）
# 实现 LinkedListSequence（基于链表）

class ListSequence(Sequence):
    def __init__(self):
        super().__init__()
        self._list = []
    def append(self, item):
        self._list.append(item)

    def get(self, index):
        return self._list[index]

    def length(self):
        return len(self._list)

    def __iter__(self):
        return iter(self._list)

# li = ListSequence()
# li.append(2)
# li.append(3)
# print(li.get(0))
# print(li.length())
# for i in li:
#     print(i)
class Linke:
    def __init__(self,value = None):
        self.value = value
        self.next = None
    def __str__(self):
        return f"{self.value} - {self.next}"
class LinkedList:
    def __init__(self,link):
        self.link = link
        self._next = link

    def __iter__(self):
        return self

    def __next__(self):
        if not self._next:
            raise StopIteration
        e = self._next
        self._next = self._next.next
        return e
        
class LinkedListSequence(Sequence):
    def __init__(self):
        super().__init__()
        self._head = None
        self._size = 0

    def append(self, item):
        lin = Linke(item)
        if self._head :
            lin.next = self._head
        self._head = lin
        self._size += 1

    def get(self, index):
        dex = 0
        for i in link:
            if dex == index:
                return i
            dex += 1
        return None


    def length(self):
        return self._size

    def __iter__(self):
        return LinkedList(self._head)

link = LinkedListSequence()
link.append(5)
link.append(6)
print(link.get(1))
print(link.length())
for i in link:
    print(i)