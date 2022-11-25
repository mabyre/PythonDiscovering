#
# https://numpy.org/doc/stable/user/quickstart.html
#
import numpy

b = numpy.arange(12).reshape(3, 4)

print(b)
print('--------')

c = b.sum(axis=0)     # sum of each column

print(c)
print('--------')

c = b.min(axis=1)     # min of each row

print(c)
print('--------')

c = b.cumsum(axis=1)  # cumulative sum along each row

print(c)

print('--------')

c1 = b[0:3, 1]  # equiv b[:,1] all lignes form columns 1

print(c1)

# [[0  1  2  3]
#  [4  5  6  7]
#  [8  9 10 11]]
# --------
# [12 15 18 21]
# --------
# [0 4 8]
# --------
# [[0  1  3  6]
#  [4  9 15 22]
#  [8 17 27 38]]
# --------
# [1 5 9]


print('-------- Convolution --------')

conv = numpy.convolve([1, 2, 3], [0, 1, 0.5])
print(conv)

conv = numpy.convolve([1, 2, 3], [0, 1, 0.5], 'same')
print(conv)

conv = numpy.convolve([1, 2, 3], [0, 1, 0.5], 'valid')
print(conv)

conv = numpy.convolve([1, 2, 3], [0, 0.5], 'valid')
print(conv)
