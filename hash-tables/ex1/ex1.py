def get_indices_of_item_weights(weights, limit):
  # create hash table
  ht = {}

  # return empty tuple if only one package
  if len(weights) == 1:
    return ()

  # compare values right away if only two packages
  if len(weights) == 2:
    # return indices if values equal limit
    if (weights[0] + weights[1] == limit):
      return (1, 0)
    #return empty tuple if values do not match limit
    else:
      return ()

  # set hash table with weights as keys and values as indices
  for i, weights in enumerate(weights):
    ht[weights] = i

  # iterate through hash table and check for weights that meet the limit
  for key in ht:
    try:
      keyTest = ht[limit-key]
      if (keyTest):
        return (ht[limit-key], ht[key])
    except KeyError:
      print('key error, moving on')

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print('Test 1')
  print(get_indices_of_item_weights([2, 2], 4))
  print('Test 2')
  print(get_indices_of_item_weights([6, 3, 8, 4], 7))
  print('Test 3')
  print(get_indices_of_item_weights([1, 16, 7, 5], 17))
  print('Test 4')
  print(get_indices_of_item_weights([22, 33, 44], 11))
  print('Test 5')
  print(get_indices_of_item_weights([2, 2], 3))
