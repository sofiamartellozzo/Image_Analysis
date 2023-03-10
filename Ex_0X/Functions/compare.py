def compare(I1, I2):

  output = 0

  shape1 = I1.shape
  shape2 = I2.shape

  #first check if have the same shape
  if shape1 != shape2:
    return output

  nrows = I1.shape[0]
  ncols = I2.shape[1]

  for i in range(nrows):
    for j in range(ncols):
      if I1[i][j] != I2[i][j]:
        return output

  #the two images matches
  output = 1
  return output