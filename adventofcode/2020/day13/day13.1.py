timestamp = int(input())
buses = input().split(",")

minor_time_waiting = -1
first_bus_id = -1
for b in buses:
  if b != "x":
    bus_id = int(b)
    wait_time = bus_id - (timestamp % bus_id)
    if wait_time < minor_time_waiting or minor_time_waiting == -1:
      minor_time_waiting = wait_time
      first_bus_id = bus_id

print(minor_time_waiting * first_bus_id)