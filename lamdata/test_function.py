#from lamdata.ds_utility import myfunc

def myfunc(X):
  X = X.copy()
  y = X.isnull().sum()
  z = y.to_frame(name='missing')
  z['dtypes'] = X.dtypes
  return z

def enlarge(n):
  return n * 10