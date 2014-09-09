#The way we did it in class was more complicated than the one I did before.

def bin2dec(num):
  num = [1,0,1,0,1]
  result = 0
  for index in range (len(num)):
    digit = num[index]
    if digit == "1":
      result = result + pow(2, len(num) - index - 1)
  return result