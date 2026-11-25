import numpy as np
a1 = np.arange(9)
# print(a1)
# for i in a1:
    # print(i)
a2 = np.arange(9).reshape(3,3)
# print(a2)
# print(a2[0,:])
# print(a2[1,1:])
# print(a2[::2,1])
# for i in a2 :
    # print(i)
a3 = np.arange(27).reshape(3,3,3)
# print(a3)
# print(a3[1,1,2])
#for i in a3:
    # print(i)
for i in np.nditer(a3):
    print(i)