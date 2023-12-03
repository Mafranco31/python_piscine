from vector import Vector

v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
#print(v[0][1])
v2 = Vector([[5.0], [4.0], [2.0], [3.0]])
#print(v2[1][0])
#v2 = Vector(3)
print(v1)
print("v1 = ", v1.values, v1.shape)
print("v2 = ", v2.values, v2.shape)
v3 = Vector(4)
print("v3 = ", v3.values, v3.shape)  

v4 = Vector((5, 9))
print("v4 = ", v4.values, v4.shape)
v5 = Vector((0, 4))
print("v5 = ", v5.values, v5.shape)
print()
v10 = v1.dot(v3.T())
print("v1 * v3.T() = ", v10)
print("v4 * v5 = ", v4.dot(v5))
print("\ninverse de v1 = ", v1.T())
print("inverse de v2 = ", v2.T())
v69 = v1 - v4.T()
print("v1 - v4.T() = ", v69)
print("v1 / 2 =", v1 / 2)
print("v1 * 2 =", v1 * 2)
print(v1)
v1
# print(v2.shape)
# Expected output:
# (1,4)
#print(v2.T())
# Expected output:
#v1 = Vector(3)
#print(v2.values)
#print(v1.dot(v2))
#print(v2.T().shape)
# Expected
# (4,1)