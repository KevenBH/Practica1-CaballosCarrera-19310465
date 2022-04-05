from NodoCab import NodoCab

class OrdenCab:
    def __init__(self, Vel, Nom):
        self.root = NodoCab(Vel, Nom)

    def __RecursiveAddition(self, Node, Vel, Nom):
        if Vel < Node.Vel:
            if Node.Back is None:
                Node.Back = NodoCab(Vel, Nom)
            else:
                self.__RecursiveAddition(Node.Back, Vel, Nom)
        else:
            if Node.Next is None:
                Node.Next = NodoCab(Vel, Nom)
            else:
                self.__RecursiveAddition(Node.Next, Vel, Nom)

    def __OrderRecursive(self, Node):
        if Node is not None:
            self.__OrderRecursive(Node.Next)
            print(Node.Nom, ": ", Node.Vel, "pts")
            self.__OrderRecursive(Node.Back)
    
    def __Busca(self, node, Vel):
        if node is None:
            return None
        if node.Vel == Vel:
            return node
        if Vel < node.Vel:
            return self.__Busca(node.Back, Vel)
        else:
            return self.__Busca(node.Next, )

    def Add(self, Vel, Nom):
        self.__RecursiveAddition(self.root, Vel, Nom)

    def OrderedPrint(self):
        print("Caballos Ordenados: ")
        self.__OrderRecursive(self.root)
        print("")

    def Busca(self, Vel):
        return self.__Busca(self.root, Vel)