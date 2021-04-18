from processor import Processor

class Initializer():

  def run(self, memory):
    self.blocks = 0
    self.col = 0
    self.row = 0
    self.phase = 1
    self.matrix = self.init_matrix()
    self.filled = False

    self.ballf = False
    self.barf = False
    self.ballx = 0
    self.bally = 0
    self.barx = -1
    self.bary = -1
    self.balld = 0


    a = Processor('a', memory.copy(), self, self)
    self.a = a
    a.start()



  def output(self, data):

    # if self.phase >= 2398:
    #   # print(data)
    #   z = 1
    # else:
    if self.phase%3 == 1: # col
      self.col = data
    if self.phase%3 == 2: # row
      self.row = data
    if self.phase%3 == 0:
      if data == 3:
        print("barra")
        self.barf = True
        self.barx = self.col
        self.bary = self.row
      if data == 4:
        print("bola")
        self.ballf = True
        if self.ballx < self.col:
          self.balld = 1
        elif self.ballx > self.col:
          self.balld = -1
        else:
          print("NEVER")
        self.ballx = self.col
        self.bally = self.row

      if self.col == -1: #points
        print("Points:", data)
        self.print_matrix()
      else:
        self.matrix[self.row][self.col] = data
    self.phase += 1
    
    if self.ballf and self.barf:
      self.ballf = False
      self.barf = False
      self.print_matrix()

      diffy = self.bary - self.bally
      diff = self.barx - self.ballx
      if diffy == 1 and diff == 0:
        self.barf = True
        self.a.send_data(0)
      else:
        if self.balld == 1 and diff >= 0:
          if abs(diff)<1:
            print("derecha1")
            self.a.send_data(1)
          else:
            print("igual1")
            self.barf = True
            self.a.send_data(0)
          

        elif self.balld == -1 and diff <= 0:
          if abs(diff)<1:
            print("izquierda2")
            self.a.send_data(-1)
          else:
            print("igual2")
            self.barf = True
            self.a.send_data(0)

        else:
          if diff < 0:
            print("derecha3")
            self.a.send_data(1)
          elif diff > 0:
            print("izquierda3")
            self.a.send_data(-1)
          else:
            print("igual3")
            self.barf = True
            self.a.send_data(0)

    

  def end(self, id):
    self.print_matrix()
    print(self.blocks)

  def init_matrix(self):
    matrix = []
    for _ in range(21):
      row = [-1]*38
      matrix.append(row)
    return matrix

  def print_matrix(self):
    print("\n\n")
    for row in self.matrix:
      tp = []
      for c in row:
        tp.append(str(c))
      print("".join(tp))



memory = [int(x) for x in input().split(',')]
memory[0] = 2

ini = Initializer()
ini.run(memory)


