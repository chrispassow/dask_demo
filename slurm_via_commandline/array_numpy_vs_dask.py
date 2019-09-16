import numpy as np
import dask.array as da
import sys
from time import time

size_dim1 = int(sys.argv[1])
size_dim2 = int(sys.argv[2])

print('\n \n pure Numpy \n')

time_pre_gen = time()
x = np.random.rand(size_dim1, size_dim2)
time_post_gen = time()

print('Type:', type(x), 'Size', x.shape)
print('time to generate numpy array: %0.3f s' % (time_post_gen - time_pre_gen))

time_pre_calc = time()
res = np.sum(x)
time_post_calc = time()

print('Sum:',res)
print('time to calc sum: %0.3f s' % (time_post_calc - time_pre_calc))
print('total time  %0.3f s' % (time_post_calc - time_pre_gen))

print('\n \n with Dask \n')

time_pre_gen = time()
x = da.random.random((size_dim1, size_dim2), chunks=(1000,1000))
time_post_gen = time()

print('Type:', type(x), 'Size', x.shape)
print('time to generate dask array: %0.3f s' % (time_post_gen - time_pre_gen))

time_pre_calc = time()
res = da.sum(x).compute()
time_post_calc = time()

print('Sum:',res)
print('time to calc sum: %0.3f s' % (time_post_calc - time_pre_calc))
print('total time  %0.3f s \n \n' % (time_post_calc - time_pre_gen))
