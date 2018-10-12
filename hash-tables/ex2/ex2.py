def reconstruct_trip(tickets):
  # create hash table
  ht = {}
  # declare initial route
  route = []

  # iterate through tickets list and set keys as start location and values as destinations
  for t in tickets:
    ht[t[0]] = t[1]

  # initialize current location as none
  try:
    # initialize current location as none
    current = ht[None]
    # begin building route with current location
    route.append(current)
    # initilize next location
    next = ht[None]

    # loop until next destination is none
    while (next != None):
      try:
        next = ht[next]
        if (next):
          route.append(next)
      except:
        return []

    return route
  
  except:
    return []



if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
#   tickets = [
#   ('PIT', 'ORD'),
#   ('XNA', 'CID'),
#   ('SFO', 'BHM'),
#   ('FLG', 'XNA'),
#   (None, 'LAX'), 
#   ('LAX', 'SFO'),
#   ('CID', 'SLC'),
#   ('ORD', None),
#   ('SLC', 'PIT'),
#   ('BHM', 'FLG'),
# ]
# print('Test')
# print(reconstruct_trip(tickets))
  pass
