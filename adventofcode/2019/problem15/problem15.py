from processor import Processor
import random

class Initializer():

  def run(self, memory):
    self.matrix = self.init_matrix()
    self.x = 2500
    self.y = 2500
    self.maxx = 2500
    self.maxy = 2500
    self.minx = 2500
    self.miny = 2500
    self.d = 1

    a = Processor('a', memory.copy(), self, self)
    a.start()
    a.send_data(1)

    self.a = a


  def output(self, data):
    print(data)
    if data == 1:
      if self.d == 1:
        self.x -= 1
      elif self.d == 2:
        self.y += 1
      elif self.d == 3:
        self.x += 1
      elif self.d == 4:
        self.y -= 1
      print(self.x, self.y)
      self.matrix[self.x][self.y] = data
      self.d = int((random.random() * 4)//1)+1
      self.a.send_data(self.d)

    elif data == 0:
      x = self.x
      y = self.y
      if self.d == 1:
        x -= 1
      elif self.d == 2:
        y += 1
      elif self.d == 3:
        x += 1
      elif self.d == 4:
        y -= 1
      self.matrix[x][y] = data
      self.d = self.d - 1
      if self.d == 0:
        self.d = 4
      self.a.send_data(self.d)


    else:
      print("FIN: ",data)
    # self.print_matrix()
    self.print_matrix()
    self.minx = min(self.x, self.minx)
    self.miny = min(self.y, self.miny)
    self.maxx = max(self.x, self.maxx)
    self.maxy = max(self.y, self.maxy)


  def end(self, id):
    # self.print_matrix()
    print("END")

  def init_matrix(self):
    matrix = []
    for _ in range(5000):
      row = [-1]*5000
      matrix.append(row)
    return matrix

  def print_matrix(self):
    print("\n\n")
    for row in self.matrix[self.minx:self.maxx]:
      tp = []
      for c in row[self.miny:self.maxy]:
        if c == -1:
          tp.append(" ")
        elif c == 0:
          tp.append("#")
        elif c == 1:
          tp.append(".")
        else:
          tp.append("o")

      print("".join(tp))



memory = [int(x) for x in input().split(',')]

ini = Initializer()
ini.run(memory)


