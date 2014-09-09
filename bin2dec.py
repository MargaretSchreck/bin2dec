def bin2dec():
  num = [1,0,1,0,1]
  result = 0
  for index in range (5):
    result = result + num [index]*pow(2,4 - index)
  print result