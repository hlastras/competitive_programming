import threading
import time

class Processor(threading.Thread):
  def __init__(self,id, program, callback, ender):
    threading.Thread.__init__(self)
    self.id = id
    self.program = program
    self.callback = callback
    self.ender = ender
    self.input = []
    self.pointer = 0


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
        a = self.program[self.pointer+1] if mod_a=="1" else self.program[self.program[self.pointer+1]]
        b = self.program[self.pointer+2] if mod_b=="1" else self.program[self.program[self.pointer+2]]
        self.program[self.program[self.pointer+3]] = (a+b)
        # print("SUM:", a, b, mod_a, mod_b)
        self.pointer +=4
      elif opcode == "02": #mult
        a = self.program[self.pointer+1] if mod_a=="1" else self.program[self.program[self.pointer+1]]
        b = self.program[self.pointer+2] if mod_b=="1" else self.program[self.program[self.pointer+2]]
        self.program[self.program[self.pointer+3]] = (a*b)
        # print("MUL:", a, b, mod_a, mod_b)
        self.pointer +=4
      elif opcode == "03": #input
        self.program[self.program[self.pointer+1]] = self.read_data()
        self.pointer +=2
      elif opcode == "04": #output
        a = self.program[self.pointer+1] if mod_a=="1" else self.program[self.program[self.pointer+1]]
        # print("Output:", a)
        self.callback.output(a)
        self.pointer +=2
      elif opcode == "05": #jump if true
        a = self.program[self.pointer+1] if mod_a=="1" else self.program[self.program[self.pointer+1]]
        b = self.program[self.pointer+2] if mod_b=="1" else self.program[self.program[self.pointer+2]]
        if a != 0:
          self.pointer = b
        else:
          self.pointer += 3
      elif opcode == "06": #jump if false
        a = self.program[self.pointer+1] if mod_a=="1" else self.program[self.program[self.pointer+1]]
        b = self.program[self.pointer+2] if mod_b=="1" else self.program[self.program[self.pointer+2]]
        if a == 0:
          self.pointer = b
        else:
          self.pointer += 3
      elif opcode == "07": #less than
        a = self.program[self.pointer+1] if mod_a=="1" else self.program[self.program[self.pointer+1]]
        b = self.program[self.pointer+2] if mod_b=="1" else self.program[self.program[self.pointer+2]]
        if a<b:
          self.program[self.program[self.pointer+3]] = 1
        else:
          self.program[self.program[self.pointer+3]] = 0
        self.pointer +=4
      elif opcode == "08": #equal to
        a = self.program[self.pointer+1] if mod_a=="1" else self.program[self.program[self.pointer+1]]
        b = self.program[self.pointer+2] if mod_b=="1" else self.program[self.program[self.pointer+2]]
        if a==b:
          self.program[self.program[self.pointer+3]] = 1
        else:
          self.program[self.program[self.pointer+3]] = 0
        self.pointer +=4
    self.end_thread()

  def send_data(self, data):
    self.input.append(data)

  def read_data(self):
    while len(self.input) == 0:
      time.sleep(0.001)
    value = self.input[0]
    self.input = self.input[1:]
    return value

  def end_thread(self):
    self.ender.end(self.id)

