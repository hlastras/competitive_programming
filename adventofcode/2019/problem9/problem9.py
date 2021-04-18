from processor import Processor
from pipeline_adapter import PipelineAdapter
# import itertools
# import time

# class Initializer():

#   def __init__(self, outputs):
#     self.outputs = outputs

#   def run(self, memory, modes):
#     self.a_finish = False

#     e = Processor('e', memory.copy(), self, self)
#     d_to_e = PipelineAdapter(e)
#     d = Processor('d', memory.copy(), d_to_e, self)
#     c_to_d = PipelineAdapter(d)
#     c = Processor('c', memory.copy(), c_to_d, self)
#     b_to_c = PipelineAdapter(c)
#     b = Processor('b', memory.copy(), b_to_c, self)
#     a_to_b = PipelineAdapter(b)
#     a = Processor('a', memory.copy(), a_to_b, self)

#     e.start()
#     d.start()
#     c.start()
#     b.start()
#     a.start()

#     mode_a, mode_b, mode_c, mode_d, mode_e = modes

#     a.send_data(mode_a)
#     b.send_data(mode_b)
#     c.send_data(mode_c)
#     d.send_data(mode_d)
#     e.send_data(mode_e)

#     self.a = a

#     a.send_data(0)


#   def output(self, data):
#     if self.a_finish:
#       self.outputs.append(data)
#       # print(data)
#     else:
#       self.a.send_data(data)

#   def end(self, id):
#     if id=='a':
#       self.a_finish = True


memory = [int(x) for x in input().split(',')]

outputer = PipelineAdapter(None)
a = Processor('a', memory.copy(), outputer, None)
a.start()
a.send_data(2)

# perms = list(itertools.permutations([5,6,7,8,9]))
# outputs = []
# for p in perms:
#   i = Initializer(outputs)
#   i.run(memory, list(p))
#   time.sleep(0.1)

# print("MAX:", max(outputs))

