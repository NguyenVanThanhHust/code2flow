class Node:
    def __init__(self, name):
        self.name = name

    def  __rshift__(self, other):
        return f"{self.name} >> {other.name}"
