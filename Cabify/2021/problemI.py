import math

def calculate(point, polygon):
  total = 0
  for edge in polygon:
    if between(point, edge[0], edge[1]):
      return "on"

    total += angle(point, edge[0], edge[1])

  if near_zero(total):
    return "out"
  else:
    return "in"
  
def distance(p1, p2):
  return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def sign_of_rotation(p1, p2, p3):
  p1p2 = (p2[0]-p1[0], p2[1]-p1[1])
  p1p3 = (p3[0]-p1[0], p3[1]-p1[1])
  cross_product = p1p2[0]*p1p3[1] - p1p2[1]*p1p3[0]
  if cross_product > 0:
    return 1
  else:
    return -1

def angle(p1, p2, p3):
  p12 = distance(p1, p2)
  p13 = distance(p1, p3)
  p23 = distance(p2, p3)
  try:
    return math.acos((p12**2 + p13**2 - p23**2)/(2*p12*p13)) * sign_of_rotation(p1, p2, p3)
  except:
    return 0.0

def between(ip, p1, p2):
  if ip[0] == p1[0] and ip[1] == p1[1]:
    return True
  if ip[0] == p2[0] and ip[1] == p2[1]:
    return True

  # calculate unary vector from p1 to ip and from ip to p2
  p1ip = (ip[0]-p1[0], ip[1]-p1[1])
  ipp2 = (p2[0]-ip[0], p2[1]-ip[1])
  m1 = math.sqrt(p1ip[0]**2+p1ip[1]**2)
  m2 = math.sqrt(ipp2[0]**2+ipp2[1]**2)
  vu1 = (p1ip[0]/m1, p1ip[1]/m1)
  vu2 = (ipp2[0]/m2, ipp2[1]/m2)

  return str(vu1[0])[:15] == str(vu2[0])[:15] and str(vu1[1])[:15] == str(vu2[1])[:15]

def near_zero(n):
  r = n > 0.00000001 or n < -0.00000001
  return not r


p = int(input())
while p > 0:
  polygon_points = []

  for _ in range(p):
    polygon_points.append(tuple(int(x) for x in input().split()))
  
  polygon_edges = []
  for i in range(p):
    v1 = polygon_points[i-1]
    v2 = polygon_points[i]
    edge = [v1, v2]
    polygon_edges.append(edge)

  points = int(input())
  for _ in range(points):
    point = [int(x) for x in input().split()]
    print(calculate(point, polygon_edges))
  
  p = int(input())