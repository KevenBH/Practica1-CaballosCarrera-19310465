import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from OrdenCab import OrdenCab
from ListaT import ListaT


CC = np.zeros((5, 5))
for x in range(5):
    for y in range(5):
        CC[x, y] = random.randint(0,1000)
print("Grupos De Caballos :")
for x in range(5):
  print("Grupo ", x + 1, ":", CC[x])
print("")

#CARRERA 1-5
print("Ordenado Lento -> Rapido:")
for x in range(5):
  CC[x].sort() 
  print("Carrera ", x + 1, ":", CC[x]) 
print("")
  
#CARRERA 6
print("Los Mas Rapidos:")
print("                   |Race 6|")
R6 = CC[np.argsort(CC[:, -1])]
for x in range(5):
  print(R6[x]) 
print("")  
print("1° Caballo: ", int(R6[4,4]), "m/s\n")

#cARRERA 7
R7 = [R6[2, 4], R6[3, 4], R6[3, 3], R6[4, 3], R6[4, 2]]
R7.sort()
print("Carrara 7:", R7, "\n")
print ("2° Caballo: ", int(R7[4]), "m/s")

ConcatenatedArray = np.concatenate(R6)
ConcatenatedArray.sort()

OrdenCab = OrdenCab(int(R6[0, 0]), "Caballo 1")
OrdenCab.Add(int(R6[0, 1]), "C 2")
OrdenCab.Add(int(R6[0, 2]), "C 3")
OrdenCab.Add(int(R6[0, 3]), "C 4")
OrdenCab.Add(int(R6[0, 4]), "C 5")
OrdenCab.Add(int(R6[1, 0]), "C 6")
OrdenCab.Add(int(R6[1, 1]), "C 7")
OrdenCab.Add(int(R6[1, 2]), "C 8")
OrdenCab.Add(int(R6[1, 3]), "C 9")
OrdenCab.Add(int(R6[1, 4]), "C 10")
OrdenCab.Add(int(R6[2, 0]), "C 11")
OrdenCab.Add(int(R6[2, 1]), "C 12")
OrdenCab.Add(int(R6[2, 2]), "C 13")
OrdenCab.Add(int(R6[2, 3]), "C 14")
OrdenCab.Add(int(R6[2, 4]), "C 15")
OrdenCab.Add(int(R6[3, 0]), "C 16")
OrdenCab.Add(int(R6[3, 1]), "C 17")
OrdenCab.Add(int(R6[3, 2]), "C 18")
OrdenCab.Add(int(R6[3, 3]), "C 19")
OrdenCab.Add(int(R6[3, 4]), "C 20")
OrdenCab.Add(int(R6[4, 0]), "C 21")
OrdenCab.Add(int(R6[4, 1]), "C 22")
OrdenCab.Add(int(R6[4, 2]), "C 23")
OrdenCab.Add(int(R6[4, 3]), "C 24")
OrdenCab.Add(int(R6[4, 4]), "C 25")

"""x = 1
for x in range(5):
    for y in range(5):
        if R6[x, y] != R6[0, 0]:
            HorseTree.Add(int(R6[x, y]), "Horse " + string(x))
            x += 1
"""
OrdenCab.OrderedPrint()

Cabs = ["" for x in range(25)]
for x in range(25):
  Data = HorseTree.Search(ConcatenatedArray[x]) 
  Horses[x] = Data.Name

Graph = nx.Graph()

Vertex = [Cabs[24], Cabs[23], Cabs[22], Cabs[21], Cabs[20], Cabs[19], Cabs[18], 
              Cabs[17], Cabs[16], [15], Cabs[14], Cabs[13], Cabs[12], Cabs[11], 
              Cabs[10], Cabs[9], Cabs[8], Cabs[7], Cabs[6], Cabs[5], Cabs[4],
              Cabs[3], Cabs[2], Cabs[1], Cabs[0]]
Graph.add_nodes_from(Vertex)

Arista = [(Cabs[24], Cabs[23]), ([23], Cabs[22]), (Cabs[22], Cabs[21]), (Cabs[21], Cabs[20]),
             (Cabs[20], Cabs[19]), (Cabs[19], Cabs[18]), (Cabs[18], Cabs[17]), (Cabs[17], Cabs[16]),
             (Cabs[16], Cabs[15]), (Cabs[15], Cabs[14]), (Cabs[14], Cabs[13]), (Cabs[13], Cabs[12]),
             (Cabs[12], Cabs[11]), (Cabs[11], Cabs[10]), (Cabs[10], Cabs[9]), (Cabs[9], Cabs[8]), 
             (Cabs[8], Cabs[7]), (Cabs[7], Cabs[6]), (Cabs[6], Cabs[5]), (Cabs[5], Cabs[4]),
             (Cabs[4], Cabs[3]), (Cabs[3], Cabs[2]), (Cabs[2], Cabs[1]), (Cabs[1], Cabs[0])]
Graph.add_edges_from(Arista)

Position = {Horses[24]: (1, 26), Horses[23]: (2, 25), Horses[22]: (3, 24), Horses[21]: (4, 23), Horses[20]: (5, 22),
         Horses[19]: (6, 21), Horses[18]: (7, 20), Horses[17]: (8, 19), Horses[16]: (9, 18), Horses[15]: (10, 17), 
         Horses[14]: (11, 16), Horses[13]: (12, 15), Horses[12]: (13, 14), Horses[11]: (14, 13), Horses[10]: (15, 12),
         Horses[9]: (16, 11), Horses[8]: (17, 10), Horses[7]: (18, 9), Horses[6]: (19, 8), Horses[5]: (20, 7),
         Horses[4]: (21, 6), Horses[3]: (22, 5), Horses[2]: (23, 4), Horses[1]: (24, 3), Horses[0]: (25, 2)}
P1 = Tuple()
P1.x = Position[Horses[24]][0]
P1.y = Position[Horses[24]][1]
P2 = Tuple()
P2.x = Position[Horses[23]][0]
P2.y = Position[Horses[23]][1]
P3 = Tuple()
P3.x = Position[Horses[22]][0]
P3.y = Position[Horses[22]][1]
P4 = Tuple()
P4.x = Position[Horses[21]][0]
P4.y = Position[Horses[21]][1]
P5 = Tuple()
P5.x = Position[Horses[20]][0]
P5.y = Position[Horses[20]][1]
P6 = Tuple()
P6.x = Position[Horses[19]][0]
P6.y = Position[Horses[19]][1]
P7 = Tuple()
P7.x = Position[Horses[18]][0]
P7.y = Position[Horses[18]][1]
P8 = Tuple()
P8.x = Position[Horses[17]][0]
P8.y = Position[Horses[17]][1]
P9 = Tuple()
P9.x = Position[Horses[16]][0]
P9.y = Position[Horses[16]][1]
P10 = Tuple()
P10.x = Position[Horses[15]][0]
P10.y = Position[Horses[15]][1]
P11 = Tuple()
P11.x = Position[Horses[14]][0]
P11.y = Position[Horses[14]][1]
P12 = Tuple()
P12.x = Position[Horses[13]][0]
P12.y = Position[Horses[13]][1]
P13 = Tuple()
P13.x = Position[Horses[12]][0]
P13.y = Position[Horses[12]][1]
P14 = Tuple()
P14.x = Position[Horses[11]][0]
P14.y = Position[Horses[11]][1]
P15 = Tuple()
P15.x = Position[Horses[10]][0]
P15.y = Position[Horses[10]][1]
P16 = Tuple()
P16.x = Position[Horses[9]][0]
P16.y = Position[Horses[9]][1]
P17 = Tuple()
P17.x = Position[Horses[8]][0]
P17.y = Position[Horses[8]][1]
P18 = Tuple()
P18.x = Position[Horses[7]][0]
P18.y = Position[Horses[7]][1]
P19 = Tuple()
P19.x = Position[Horses[6]][0]
P19.y = Position[Horses[6]][1]
P20 = Tuple()
P20.x = Position[Horses[5]][0]
P20.y = Position[Horses[5]][1]
P21 = Tuple()
P21.x = Position[Horses[4]][0]
P21.y = Position[Horses[4]][1]
P22 = Tuple()
P22.x = Position[Horses[3]][0]
P22.y = Position[Horses[3]][1]
P23 = Tuple()
P23.x = Position[Horses[2]][0]
P23.y = Position[Horses[2]][1]
P24 = Tuple()
P24.x = Position[Horses[1]][0]
P24.y = Position[Horses[1]][1]
P25 = Tuple()
P25.x = Position[Horses[0]][0]
P25.y = Position[Horses[0]][1]

Nodes = {Horses[24]: P1, Horses[23]: P2, Horses[22]: P3, Horses[21]: P4, Horses[20]: P5, 
          Horses[19]: P6, Horses[18]: P7, Horses[17]: P8, Horses[16]: P9, Horses[15]: P10, 
          Horses[14]: P11, Horses[13]: P12, Horses[12]: P13, Horses[11]: P14, Horses[10]: P15, 
          Horses[9]: P16, Horses[8]: P17, Horses[7]: P18, Horses[6]: P19, Horses[5]: P20, 
          Horses[4]: P21, Horses[3]: P22, Horses[2]: P23, Horses[1]: P24, Horses[0]: P25}
          
nx.draw(Graph, pos = Position, node_color = 'blue', with_labels = True)
plt.show()