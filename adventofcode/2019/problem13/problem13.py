from processor import Processor

class Initializer():

  def run(self, memory):
    self.blocks = 0
    self.phase = 0

    a = Processor('a', memory.copy(), self, self)
    a.start()

    self.a = a


  def output(self, data):
    if self.phase == 2:
      if data == 2:
        self.blocks += 1
      self.phase = 0
    else:
      self.phase += 1

  def end(self, id):
    print(self.blocks)



memory = [int(x) for x in input().split(',')]

ini = Initializer()
ini.run(memory)


