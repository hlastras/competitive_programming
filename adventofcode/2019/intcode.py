
def run(input, memory):
  output = None
  reader_pos = 0
  while True:
    init = "%05d" % (memory[reader_pos])
    opcode = init[3:]
    mod_a = init[2]
    mod_b = init[1]
    mod_c = init[0]

    # print(memory[reader_pos:reader_pos+4])
    if opcode == "99":
      break
    elif opcode == "01": #sum
      a = memory[reader_pos+1] if mod_a=="1" else memory[memory[reader_pos+1]]
      b = memory[reader_pos+2] if mod_b=="1" else memory[memory[reader_pos+2]]
      memory[memory[reader_pos+3]] = (a+b)
      reader_pos +=4
    elif opcode == "02": #mult
      a = memory[reader_pos+1] if mod_a=="1" else memory[memory[reader_pos+1]]
      b = memory[reader_pos+2] if mod_b=="1" else memory[memory[reader_pos+2]]
      memory[memory[reader_pos+3]] = (a*b)
      reader_pos +=4
    elif opcode == "03": #input
      memory[memory[reader_pos+1]] = input
      reader_pos +=2
    elif opcode == "04": #output
      a = memory[reader_pos+1] if mod_a=="1" else memory[memory[reader_pos+1]]
      output = a
      reader_pos +=2
    elif opcode == "05": #jump if true
      a = memory[reader_pos+1] if mod_a=="1" else memory[memory[reader_pos+1]]
      b = memory[reader_pos+2] if mod_b=="1" else memory[memory[reader_pos+2]]
      if a != 0:
        reader_pos = b
      else:
        reader_pos += 3
    elif opcode == "06": #jump if false
      a = memory[reader_pos+1] if mod_a=="1" else memory[memory[reader_pos+1]]
      b = memory[reader_pos+2] if mod_b=="1" else memory[memory[reader_pos+2]]
      if a == 0:
        reader_pos = b
      else:
        reader_pos += 3
    elif opcode == "07": #less than
      a = memory[reader_pos+1] if mod_a=="1" else memory[memory[reader_pos+1]]
      b = memory[reader_pos+2] if mod_b=="1" else memory[memory[reader_pos+2]]
      if a<b:
        memory[memory[reader_pos+3]] = 1
      else:
        memory[memory[reader_pos+3]] = 0
      reader_pos +=4
    elif opcode == "08": #equal to
      a = memory[reader_pos+1] if mod_a=="1" else memory[memory[reader_pos+1]]
      b = memory[reader_pos+2] if mod_b=="1" else memory[memory[reader_pos+2]]
      if a==b:
        memory[memory[reader_pos+3]] = 1
      else:
        memory[memory[reader_pos+3]] = 0
      reader_pos +=4


  return output






memory = [int(x) for x in input().split(',')]
print(run(5, memory))