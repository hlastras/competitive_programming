import threading
import time

class Processor(threading.Thread):
  def __init__(self,id, program, callback, ender):
    threading.Thread.__init__(self)
    self.id = id
    self.program = [0]*100000
    for i, x in enumerate(program):
      self.program[i] = x
    self.callback = callback
    self.ender = ender
    self.input = []
    self.pointer = 0
    self.relative_base = 0

  def read_param(self, position, mode):
    if mode == "0":
      return self.program[self.program[self.pointer+position]]
    elif mode == "1":
      return self.program[self.pointer+position]
    elif mode == "2":
      return self.program[self.relative_base + self.program[self.pointer+position]]

    return None

  def write_memory(self, position, mode, value):
    if mode == "0":
      self.program[self.program[self.pointer+position]] = value
    elif mode == "2":
      self.program[self.relative_base + self.program[self.pointer+position]] = value


  def run(self):
    while True:
      init = "%05d" % (self.program[self.pointer])
      opcode = init[3:]
      mod_a = init[2]
      mod_b = init[1]
      mod_c = init[0]

      # print(self.program[self.pointer:self.pointer+4])
      if opcode == "99":
        break
      elif opcode == "01": #sum
        a = self.read_param(1, mod_a)
        b = self.read_param(2, mod_b)
        self.write_memory(3, mod_c, (a+b))
        # print("SUM:", a, b, mod_a, mod_b)
        self.pointer +=4
      elif opcode == "02": #mult
        a = self.read_param(1, mod_a)
        b = self.read_param(2, mod_b)
        self.write_memory(3, mod_c, (a*b))
        # print("MUL:", a, b, mod_a, mod_b)
        self.pointer +=4
      elif opcode == "03": #input
        value = self.read_data()
        self.write_memory(1, mod_a, value)
        self.pointer +=2
      elif opcode == "04": #output
        a = self.read_param(1, mod_a)
        # print("Output:", a)
        self.callback.output(a)
        self.pointer +=2
      elif opcode == "05": #jump if true
        a = self.read_param(1, mod_a)
        b = self.read_param(2, mod_b)
        if a != 0:
          self.pointer = b
        else:
          self.pointer += 3
      elif opcode == "06": #jump if false
        a = self.read_param(1, mod_a)
        b = self.read_param(2, mod_b)
        if a == 0:
          self.pointer = b
        else:
          self.pointer += 3
      elif opcode == "07": #less than
        a = self.read_param(1, mod_a)
        b = self.read_param(2, mod_b)
        if a<b:
          self.write_memory(3, mod_c, 1)
        else:
          self.write_memory(3, mod_c, 0)
        self.pointer +=4
      elif opcode == "08": #equal to
        a = self.read_param(1, mod_a)
        b = self.read_param(2, mod_b)
        if a==b:
          self.write_memory(3, mod_c, 1)
        else:
          self.write_memory(3, mod_c, 0)
        self.pointer +=4
      elif opcode == "09": #adjusts the relative base
        a = self.read_param(1, mod_a)
        self.relative_base += a
        self.pointer +=2
    self.end_thread()

  def send_data(self, data):
    print(self.input)
    self.input.append(data)

  def read_data(self):
    while len(self.input) == 0:
      time.sleep(0.001)
    value = self.input[0]
    self.input = self.input[1:]
    return value

  def end_thread(self):
    if self.ender:
      self.ender.end(self.id)

