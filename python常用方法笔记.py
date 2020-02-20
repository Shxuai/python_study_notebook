# np.array多维数组降维
a = np.array([[1], [2]])
b = np.squeeze(a)
print(a, b)

# np.array多维数组迭代遍历所有元素
# 可通过order控制遍历优先顺序
# for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
# for x in np.nditer(a.T, order='C'):C order，即是行序优先；
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
print('原始数组的转置是：')
b = a.T
print(b)
print('\n')
print('以 C 风格顺序排序：')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=", ")
print('\n')
print('以 F 风格顺序排序：')
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print(x, end=", ")


# 将给定十进制int变量i编码为位数为num_digits的二进制数组,不足的位数补0
def binary_encode(i, num_digits):
    return np.array([i >> d & 1 for d in range(num_digits)][::-1])
