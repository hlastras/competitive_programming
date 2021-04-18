from processor import Processor

class Initializer():

  def run(self, memory):
    self.is_color = True
    self.matrix = self.init_matrix()
    self.position = (100, 100)
    self.direction = 0
    self.painted = set()

    a = Processor('a', memory.copy(), self, self)
    a.start()

    self.a = a

    a.send_data(1)


  def output(self, data):
    if self.is_color:
      x = self.position[0]
      y = self.position[1]
      if data==1:
        self.matrix[x][y] = 1
      else:
        self.matrix[x][y] = 0

      if (x*5000+y) not in self.painted:
        self.painted.add(x*5000+y)

      self.is_color = False
    else:
      x = self.position[0]
      y = self.position[1]

      if data == 0: #izquierda
        if self.direction==0:
          y -= 1
          self.direction = 3
        elif self.direction==1:
          x -= 1
          self.direction = 0
        elif self.direction==2:
          y += 1
          self.direction = 1
        elif self.direction==3:
          x += 1
          self.direction = 2


      else: #derecha
        if self.direction==0:
          y += 1
          self.direction = 1
        elif self.direction==1:
          x += 1
          self.direction = 2
        elif self.direction==2:
          y -= 1
          self.direction = 3
        elif self.direction==3:
          x -= 1
          self.direction = 0

      self.position = (x, y)
      self.a.send_data(self.matrix[x][y])
      self.is_color = True

  def end(self, id):
    self.print_matrix()
    # print(len(self.painted))

  def init_matrix(self):
    matrix = []
    for _ in range(200):
      row = [1]*200
      matrix.append(row)
    return matrix
  
  def print_matrix(self):
    for row in self.matrix:
      tp = []
      for c in row:
        if c == 0:
          tp.append(" ")
        else:
          tp.append("#")
      print("".join(tp))


memory = [int(x) for x in input().split(',')]
ini = Initializer()
ini.run(memory)

