# Complexity

# Find the big-$\Theta$ asymptotic complexity of the following function in terms of N, its input.
# Don't include constants and lower-order terms.

import numpy as np

def create_matrix(N):
  my_matrix = np.zeros((N,N)) # Hint: every item in the zeros matrix must be set to zero
  for i in range(0,N-2):
    for j in range(0,N):
      my_matrix[i][j] = 2
  return my_matrix

# Example
  create_matrix(5)

# Output
# array([[2., 2., 2., 2., 2.],
#        [2., 2., 2., 2., 2.],
#        [2., 2., 2., 2., 2.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]])

