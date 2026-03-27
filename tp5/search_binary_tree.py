from printTree import printTree


class SearchBinaryTree:
    
    class Node:

        def __init__(self, value: int, left: "SearchBinaryTree.Node | None" = None, right: "SearchBinaryTree.Node | None" = None) -> None:
            self.value = value
            self.left = left
            self.right = right

        def __repr__(self) -> str:
            return str(self.value)

        def setLeft(self, vleft: int) -> None:
            left = SearchBinaryTree.Node(vleft)
            self.left = left

        def setRight(self, vright: int) -> None:
            right = SearchBinaryTree.Node(vright)
            self.right = right

        def nodeSearch(self, vtsn: int) -> bool:
            if vtsn == self.value:
                return True
            
            if vtsn > self.value:
                return False if not self.right else self.right.nodeSearch(vtsn)

            if vtsn < self.value:
                return False if not self.left else self.left.nodeSearch(vtsn)

        def nodeInsert(self, vtin: int) -> None:
            if vtin < self.value:
                if not self.left:
                    self.setLeft(vtin)
                else:
                    self.left.nodeInsert(vtin)
            if vtin > self.value:
                if not self.right:
                    self.setRight(vtin)
                else:
                    self.right.nodeInsert(vtin)

        def nodeRightDelete(self) -> None:
            if not self.right.right and self.right.left:
                self.right = None
            
            if self.right.right and self.right.left:
                print("test")

            else:
                if not self.right.left:
                    self.right = self.right.right
                else: 
                    self.right = self.right.left

        def nodeLeftDelete(self) -> None:
            if not self.left.right and self.left.right:
                self.left = None

            if self.left.right and self.left.left:
                print("test")

            else:
                if not self.left.left:
                    self.left = self.left.right
                else: 
                    self.left = self.left.left



    def __init__(self, root_val: int) -> None:
        self.root = self.Node(root_val)


    def print(self) -> None:
        printTree(self)

    def search(self, vts: int) -> bool:
        if not self.root:
            return False
        return self.root.nodeSearch(vts)

    def insert(self, vti: int) -> None:
        if not self.root:
            self.root = self.Node(vti)
        else:
            self.root.nodeInsert(vti)
        


if __name__ == "__main__":

    tree = SearchBinaryTree(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(5)
    tree.insert(9)
    tree.insert(6)
    tree.insert(4)
    tree.print()
    if (tree.search(5)):
        print("5 existe bien")
    else:
        print("5 existe pas")

    if (tree.search(10)):
        print("10 existe bien")
    else:
        print("10 existe pas")
    