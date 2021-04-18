s = "%d needs %d steps, %d needs %d steps, they meet at %d"
results = []

a, b = [int(x) for x in input().split()]
while a != 0 and b != 0:
  last_term_seq_a = a
  last_term_seq_b = b
  seen_seq_a = {}
  seen_seq_b = {}

  step = 0
  while True:

    #Add element of sequence to hashmap if element not in it yet
    if last_term_seq_a not in seen_seq_a:
      seen_seq_a[last_term_seq_a] = step
    if last_term_seq_b not in seen_seq_b:
      seen_seq_b[last_term_seq_b] = step

    #Check if we reach the result
    if last_term_seq_a in seen_seq_b:
      results.append(s % (a, seen_seq_a[last_term_seq_a], b, seen_seq_b[last_term_seq_a], last_term_seq_a))
      break
    elif last_term_seq_b in seen_seq_a:
      results.append(s % (a, seen_seq_a[last_term_seq_b], b, seen_seq_b[last_term_seq_b], last_term_seq_b))
      break

    #Calculate next term of the sequence if it is not ended
    if last_term_seq_a != 1:
      if last_term_seq_a%2 == 0:
        last_term_seq_a = last_term_seq_a//2
      else:
        last_term_seq_a = 3*last_term_seq_a + 1

    if last_term_seq_b != 1:
      if last_term_seq_b%2 == 0:
        last_term_seq_b = last_term_seq_b//2
      else:
        last_term_seq_b = 3*last_term_seq_b + 1

    step += 1

  a, b = [int(x) for x in input().split(" ")]

print("\n".join(results))