from processor import Processor
import random

class Initializer():

  def run(self, memory):
    self.matrix = []
    self.actual_line = []

    a = Processor('a', memory.copy(), self, self)
    a.start()

    self.a = a


  def output(self, data):
    if data == 35:
      self.actual_line.append("#")
    elif data == 46:
      self.actual_line.append(".")
    elif data == 10:
      self.matrix.append(self.actual_line)
      self.actual_line = []
    else:
      self.actual_line.append("X")



  def end(self, id):
    self.matrix.append(self.actual_line)
    self.actual_line = []
    self.print_matrix()
    self.resolve()
    self.print_matrix()
    print("END")


  def resolve(self):
    total = 0
    r = 0
    c = 0
    for row in self.matrix[1:-3]:
      r += 1
      c = 0
      for col in row[1:-3]:
        c += 1
        if self.matrix[r][c] == "#" and \
          self.matrix[r-1][c] == "#" and \
          self.matrix[r+1][c] == "#" and \
          self.matrix[r][c-1] == "#" and \
          self.matrix[r][c+1] == "#":
          total += (r*c)

    print("TOTAL:",total)



  def print_matrix(self):
    for row in self.matrix:
      print("".join(row))



memory = [int(x) for x in input().split(',')]

ini = Initializer()
ini.run(memory)


