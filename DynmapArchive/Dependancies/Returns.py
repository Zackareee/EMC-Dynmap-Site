import numpy as np
import time

def MinimumReturn(List):
  return int(min([List[i][j] for i in range(len(List)) for j in range(len(List[i]))]))

def MaximumReturn(List):
  return int(max([List[i][j] for i in range(len(List)) for j in range(len(List[i]))]))

def ThreeDMaximumReturn(List):
  return max(list(map(max,map(max,List))))

def ThreeDMinimumReturn(List):
  return min(list(map(min,map(min,List))))

