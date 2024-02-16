def count_valleys(string):
    """
    Funcion encargada de contar los valles en el string
    :param string: secuencia de 'D' y 'U'
    :return: numero de valles
    """
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

     """
    Funcion encargada de que la cadena solo tenga caracteres que sean 'D' o 'U'
    :param string: secuencia de 'D' y 'U'
    :return: numero de valles
    """
    
    for character in string:
        if not (character == 'D' or character == 'U'):
            return False
    return True

class Node:
        """    Clase que representa el nodo de un arbol    """

    def __init__(self, value):
    """
    Constructor del nodo
    :param value: Valor que guardara el nodo
    :atribute value: Valor que guarda el nodo
    :attribute left: Hijo izquierdo del nodo
    :attribute right: Hijo derecho del nodo
    :attribute daddy: Padre del nodo
    """
        self.value = value
        self.left = None
        self.right = None
        self.daddy = None

    def insert(self, value):

     """
    Inserta un nodo al arbol
    :param value: Valor que guardara el nuevo nodo
    """
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
    """
    Hace un recorrido en preorden
    :return: Lista del preorden
    """
        nodes = [self.value]
        if self.left is not None:
            nodes.extend(self.left.preorder())

        if self.right is not None:
            nodes.extend(self.right.preorder())

        return nodes

    def inorder(self):
    """
    Hace un recorrido en inorden
    :return: Lista del inorden
    """
        nodes = []
        if self.left is not None:
            nodes.extend(self.left.inorder())

        nodes.append(self.value)

        if self.right is not None:
            nodes.extend(self.right.inorder())

        return nodes

    def postorder(self):
    """
    Hace un recorrido en postorden
    :return: Lista del postorden
    """
        nodes = []

        if self.left is not None:
            nodes.extend(self.left.postorder())

        if self.right is not None:
            nodes.extend(self.right.postorder())

        nodes.append(self.value)

        return nodes


if __name__ == '__main__':
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
