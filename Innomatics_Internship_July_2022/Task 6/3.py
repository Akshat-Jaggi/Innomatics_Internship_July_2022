import numpy

n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)

print(array.T)
print(array.flatten())
