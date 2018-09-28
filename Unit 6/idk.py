from random import random

def my_function(x):
  return (1-x[0])**2 + 100*(x[1] - x[0]**2)**2


def optimize(bounds, NFE, f):
  D = len(bounds) 
  best_f = 10 
  best_x = [None]*D

  for i in range(NFE):
    
    
    new_x = [bounds[d][0] + random()*(bounds[d][1] - bounds[d][0]) for d in range(D)]
    new_f = f(new_x)
    if new_f < best_f: 
      best_f = new_f
      best_x = new_x

  return {'best_x': best_x, 'best_f': best_f}



bounds = [[-1,5], [-1,5]]
result = optimize(bounds, 10000, my_function)
print (result)
