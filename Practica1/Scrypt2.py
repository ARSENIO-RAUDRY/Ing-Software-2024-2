def count_valleys(string):
    counter = 0
    is_valley = False
    valleys = 0

    for character in string:
        if character == 'D':
            counter -= 1
        else:
            counter += 1

        if counter < 0:
            is_valley = True

        if is_valley and counter == 0:
            valleys += 1
            is_valley = False
    return valleys


def validate_string(string):
    for character in string:
        if not (character == 'D' or character == 'U'):
            return False
    return True

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.daddy = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
                self.left.daddy = self
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
                self.right.daddy = self
            else:
                self.right.insert(value)

    def preorder(self):
        nodes = [self.value]
        if self.left is not None:
            nodes.append(self.left.preorder())

        if self.right is not None:
            nodes.append(self.right.preorder())

        return nodes

    def inorder(self):
        nodes = []
        if self.left is not None:
            nodes.append(self.left.inorder())

        nodes.append(self.value)

        if self.right is not None:
            nodes.append(self.right.inorder())

        return nodes

    def postorder(self):
        nodes = []

        if self.left is not None:
            nodes.append(self.left.postorder())

        if self.right is not None:
            nodes.append(self.right.postorder())

        nodes.append(self.value)

        return nodes


def __name__ == '__main__':
    string = input("Ingresa una secuencia de los caracteres 'U' o 'D': ")

    while not validate_string(string):
        string = input("Cadena incorrecta! Ingrese solo caracteres que sean 'U' o 'D'")
    print("La cantidad de valles es", count_valleys(string))

    tree = Node(18)
    tree.insert(4)
    tree.insert(2)
    tree.insert(20)
    tree.insert(19)
    tree.insert(15)
    tree.insert(22)
    tree.insert(18)

    print("Preorden", tree.preorder())
    print("Inorden", tree.inorder())
    print("Postorden", tree.postorder())