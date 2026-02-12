class LinkedList:
    class Node:
        def __init__(self, value: any, next: "Node" = None) -> None:
            self.value = value
            self.next = next

        def __repr__(self) -> str:
            if self.next:
                return f"{self.value}->"
            return f"{self.value}"

        def setNext(self, next: "Node") -> None:
            self.next = next

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def __repr__(self) -> str:
        text_to_return = ""
        current = self.first
        while current is not None:
            text_to_add = repr(current)
            text_to_return += text_to_add
            current = current.next
        return text_to_return + " "

    def sizeOf(self) -> None:
        print(f"{self.size}")

    def insert(self, value: any) -> None:
        nodeLast = self.Node(value)
        if self.size == 0:
            self.first = nodeLast
        else:
            self.last.setNext(nodeLast)
        self.last = nodeLast
        self.size += 1

    def __indiceIsToLong(self, indice) -> None:
        if indice > self.size:
            raise ValueError("L'indice est plus grand que la liste")

    def __goTo(self, indice) -> Node:
        compt = 0
        current = self.first
        while compt < indice - 1:
            current = current.next
            compt += 1
        return current

    def getTo(self, indice):
        self.__indiceIsToLong(indice)
        current = self.__goTo(indice)
        print(current)

    def insertTo(self, value, indice):
        self.__indiceIsToLong(indice)
        if indice == self.size:
            self.insert(value)
        else:
            nodeInsert = self.Node(value)

            if indice == 1:
                nodeInsert.setNext(self.first)
                self.first = nodeInsert
            else:
                current = self.__goTo(indice - 1)
                nodeInsert.setNext(current.next)
                current.setNext(nodeInsert)
            self.size += 1

    def deleteTo(self, indice):
        self.__indiceIsToLong(indice)
        if indice == 1:
            self.first = self.first.next
        else:
            current = self.__goTo(indice - 1)
            if indice == self.size:
                current.next = None
                self.last == current
            else:
                current.next = current.next.next
        self.size -= 1

    def searchValue(self, value):
        current = self.first
        while value != current.value:
            if current.next == None:
                return False
            current = current.next
        return True


if __name__ == "__main__":
    linkedList1 = LinkedList()
    linkedList1.insert(5)
    linkedList1.insert(6)
    linkedList1.insert(7)
    linkedList1.sizeOf()
    print(linkedList1)
    linkedList1.getTo(2)
    linkedList1.insertTo(8, 1)
    print(linkedList1)
    linkedList1.insertTo(9, 4)
    print(linkedList1)
    linkedList1.insertTo(10, 3)
    print(linkedList1)
    linkedList1.deleteTo(2)
    print(linkedList1)
    linkedList1.deleteTo(1)
    print(linkedList1)
    linkedList1.deleteTo(4)
    print(linkedList1)
    if linkedList1.searchValue(8):
        print("La valeur est présente")
    else:
        print("La valeur n'est pas présente")
