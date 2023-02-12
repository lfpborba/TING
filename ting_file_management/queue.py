from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def search(self, index):
        if index >= len(self.items) or index < 0:
            raise IndexError("Index out of range")
        return self.items[index]

    def __len__(self):
        return len(self.items)
