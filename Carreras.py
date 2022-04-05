import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from OrdenCab import OrdenCab

class Lista:
    def _init_(self, x, y):
        self.x = x
        self.y = y

CC = np.zeros((5, 5))
for x in range(5):
    for y in range(5):
        CC[x, y] = random.randint(0,100)
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

OrdenCab = OrdenCab(int(R6[0, 0]), "C 1")
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


OrdenCab.OrderedPrint()

Cabs = ["" for x in range(25)]
for x in range(25):
  Data = OrdenCab.Busca(ConcatenatedArray[x]) 
  Cabs[x] = Data.Nom

G = nx.Graph()

Vert = [Cabs[24], Cabs[23], Cabs[22], Cabs[21], Cabs[20], Cabs[19], Cabs[18], 
              Cabs[17], Cabs[16], Cabs[15], Cabs[14], Cabs[13], Cabs[12], Cabs[11], 
              Cabs[10], Cabs[9], Cabs[8], Cabs[7], Cabs[6], Cabs[5], Cabs[4],
              Cabs[3], Cabs[2], Cabs[1], Cabs[0]]
G.add_nodes_from(Vert)

Arista = [(Cabs[24], Cabs[23]), (Cabs[23], Cabs[22]), (Cabs[22], Cabs[21]), (Cabs[21], Cabs[20]),
             (Cabs[20], Cabs[19]), (Cabs[19], Cabs[18]), (Cabs[18], Cabs[17]), (Cabs[17], Cabs[16]),
             (Cabs[16], Cabs[15]), (Cabs[15], Cabs[14]), (Cabs[14], Cabs[13]), (Cabs[13], Cabs[12]),
             (Cabs[12], Cabs[11]), (Cabs[11], Cabs[10]), (Cabs[10], Cabs[9]), (Cabs[9], Cabs[8]), 
             (Cabs[8], Cabs[7]), (Cabs[7], Cabs[6]), (Cabs[6], Cabs[5]), (Cabs[5], Cabs[4]),
             (Cabs[4], Cabs[3]), (Cabs[3], Cabs[2]), (Cabs[2], Cabs[1]), (Cabs[1], Cabs[0])]
G.add_edges_from(Arista)

Position = {Cabs[24]: (1, 26), Cabs[23]: (2, 25), Cabs[22]: (3, 24), Cabs[21]: (4, 23), Cabs[20]: (5, 22),
         Cabs[19]: (6, 21), Cabs[18]: (7, 20), Cabs[17]: (8, 19), Cabs[16]: (9, 18), Cabs[15]: (10, 17), 
         Cabs[14]: (11, 16), Cabs[13]: (12, 15), Cabs[12]: (13, 14), Cabs[11]: (14, 13), Cabs[10]: (15, 12),
         Cabs[9]: (16, 11), Cabs[8]: (17, 10), Cabs[7]: (18, 9), Cabs[6]: (19, 8), Cabs[5]: (20, 7),
         Cabs[4]: (21, 6), Cabs[3]: (22, 5), Cabs[2]: (23, 4), Cabs[1]: (24, 3), Cabs[0]: (25, 2)}

P1 = Lista()
P1.x = Position[Cabs[24]][0]
P1.y = Position[Cabs[24]][1]
P2 = Lista()
P2.x = Position[Cabs[23]][0]
P2.y = Position[Cabs[23]][1]
P3 = Lista()
P3.x = Position[Cabs[22]][0]
P3.y = Position[Cabs[22]][1]
P4 = Lista()
P4.x = Position[Cabs[21]][0]
P4.y = Position[Cabs[21]][1]
P5 = Lista()
P5.x = Position[Cabs[20]][0]
P5.y = Position[Cabs[20]][1]
P6 = Lista()
P6.x = Position[Cabs[19]][0]
P6.y = Position[Cabs[19]][1]
P7 = Lista()
P7.x = Position[Cabs[18]][0]
P7.y = Position[Cabs[18]][1]
P8 = Lista()
P8.x = Position[Cabs[17]][0]
P8.y = Position[Cabs[17]][1]
P9 = Lista()
P9.x = Position[Cabs[16]][0]
P9.y = Position[Cabs[16]][1]
P10 = Lista()
P10.x = Position[Cabs[15]][0]
P10.y = Position[Cabs[15]][1]
P11 = Lista()
P11.x = Position[Cabs[14]][0]
P11.y = Position[Cabs[14]][1]
P12 = Lista()
P12.x = Position[Cabs[13]][0]
P12.y = Position[Cabs[13]][1]
P13 = Lista()
P13.x = Position[Cabs[12]][0]
P13.y = Position[Cabs[12]][1]
P14 = Lista()
P14.x = Position[Cabs[11]][0]
P14.y = Position[Cabs[11]][1]
P15 = Lista()
P15.x = Position[Cabs[10]][0]
P15.y = Position[Cabs[10]][1]
P16 = Lista()
P16.x = Position[Cabs[9]][0]
P16.y = Position[Cabs[9]][1]
P17 = Lista()
P17.x = Position[Cabs[8]][0]
P17.y = Position[Cabs[8]][1]
P18 = Lista()
P18.x = Position[Cabs[7]][0]
P18.y = Position[Cabs[7]][1]
P19 = Lista()
P19.x = Position[Cabs[6]][0]
P19.y = Position[Cabs[6]][1]
P20 = Lista()
P20.x = Position[Cabs[5]][0]
P20.y = Position[Cabs[5]][1]
P21 = Lista()
P21.x = Position[Cabs[4]][0]
P21.y = Position[Cabs[4]][1]
P22 = Lista()
P22.x = Position[Cabs[3]][0]
P22.y = Position[Cabs[3]][1]
P23 = Lista()
P23.x = Position[Cabs[2]][0]
P23.y = Position[Cabs[2]][1]
P24 = Lista()
P24.x = Position[Cabs[1]][0]
P24.y = Position[Cabs[1]][1]
P25 = Lista()
P25.x = Position[Cabs[0]][0]
P25.y = Position[Cabs[0]][1]

Nodes = {Cabs[24]: P1, Cabs[23]: P2, Cabs[22]: P3, Cabs[21]: P4, Cabs[20]: P5, 
          Cabs[19]: P6, Cabs[18]: P7, Cabs[17]: P8, Cabs[16]: P9, Cabs[15]: P10, 
          Cabs[14]: P11, Cabs[13]: P12, Cabs[12]: P13, Cabs[11]: P14, Cabs[10]: P15, 
          Cabs[9]: P16, Cabs[8]: P17, Cabs[7]: P18, Cabs[6]: P19, Cabs[5]: P20, 
          Cabs[4]: P21,Cabs[3]: P22, Cabs[2]: P23, Cabs[1]: P24, Cabs[0]: P25}
          
nx.draw(G, pos = Position, node_color = 'green', with_labels = True)
plt.show()