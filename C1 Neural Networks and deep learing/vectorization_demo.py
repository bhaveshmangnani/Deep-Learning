import numpy as np
a = np.random.rand(1000000)
b = np.random.rand(1000000)

import time
start = time.time()
c = np.dot(a,b)
end=time.time()
print(c)
print("Vectorized-->"+str(1000*(end-start))+"ms")
c=0
start=time.time()
for i in range(1000000):
    c+=a[i]*b[i]
end=time.time()
print(c)
print("For loop-->"+str(1000*(end-start))+"ms")
