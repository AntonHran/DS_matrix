import math

import numpy as np


# 1
def create_natural_vector(end: int, start: int = None, ) -> np.array:
    if not start:
        start = 1
    natural_numbers = [i for i in range(start, end+1)]
    return np.array(natural_numbers)


a_1 = create_natural_vector(10)
print(a_1)
a_1 = np.arange(1, 11)
print(a_1)
a_1 = np.linspace(1, 10, num=10)
print(a_1)

# 2
a_2 = np.zeros((3, 3), dtype=float)
print(a_2)

# 3
a_3 = np.random.randint(1, 10, size=(5, 5))
print(a_3)

# 4
a_4 = np.random.random((4, 4))
print(a_4)

# 5
a_5_1 = np.random.randint(1, 10, 5)
a_5_2 = np.random.randint(1, 10, 5)
print(a_5_1, a_5_2)
sum_v = a_5_1 + a_5_2
print(sum_v)
subtraction_v = a_5_1 - a_5_2
print(subtraction_v)
multiply_v = a_5_1 * a_5_2
print(multiply_v)
division_v = a_5_1 / a_5_2
print(division_v)

# 6
a_6_1 = np.random.randint(100, size=7)
a_6_2 = np.random.randint(100, size=7)
print(a_6_1)
print(a_6_2)
scalar_mult = np.dot(a_6_1, a_6_2)
print(scalar_mult)

# 7
m1 = np.random.randint(1, 10, (2, 2))
m2 = np.random.randint(1, 10, (2, 3))
mult = np.dot(m1, m2)
print(mult)

# 8
m1 = np.random.randint(1, 10, (3, 3))
print(m1)
m1_inv = np.linalg.inv(m1)
print(m1_inv)

# 9
m1 = np.random.random((4, 4))
print(m1)
m1_t = m1.T
print(m1_t)

# 10
m1 = np.random.randint(1, 10, (3, 4))
v1 = np.random.randint(1, 10, size=4)
mult = np.dot(m1, v1)
print(mult)

# 11
m1 = np.random.random((2, 3))
v1 = np.random.random(3)
mult = np.dot(m1, v1)
print(mult)

# 12
m1 = np.random.randint(1, 10, (2, 2))
m2 = np.random.randint(1, 10, (2, 2))
mult = m1 * m2
print(mult)

# 13
m1 = np.random.randint(1, 10, (2, 2))
m2 = np.random.randint(1, 10, (2, 2))
mult = np.dot(m1, m2)
print(mult)

# 14
m1 = np.random.randint(1, 100, (5, 5))
sum_el = m1.sum()
print(sum_el)

# 15
m1 = np.random.randint(1, 10, (4, 4))
m2 = np.random.randint(1, 10, (4, 4))
sub = m1 - m2
print(sub)

# 16
m1 = np.random.random((3, 3))
print(m1)
print(m1[0])
print(m1[0].sum())
print(m1[1])
print(m1[1].sum())
print(m1[0:, 1])
print(m1[0:, 1].sum())
print(np.shape(m1))
res = []
for i in range(np.shape(m1)[0]):
    res.append(m1[i].sum())
vector = np.array(res)
print(vector)
print(np.sum(m1, axis=1))

# 17
m1 = np.random.randint(100, size=(3, 4))
print(m1)
res = []
for i in range(np.shape(m1)[0]):
    res_i = []
    for j in m1[i]:
        res_i.append(math.pow(j, 2))
    res.append(res_i)
print(np.array(res))
print(np.square(m1))

# 18
v1 = np.random.randint(1, 50, size=4)
print(v1)
res = []
for el in v1:
    res.append(math.sqrt(el))
v_new = np.array(res)
print(v_new)
print(np.sqrt(v1))
