tuple1 = (11, [22, 33], 44, 55)
modified_tuple = tuple1[0], [222] + list(tuple1[1][1:]), tuple1[2:]

print("tuple1:", tuple1)
print("modified_tuple:", modified_tuple)
