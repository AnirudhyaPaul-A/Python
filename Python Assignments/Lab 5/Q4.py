# From the above sets A and B I. Join A and B II. Find A intersection B III. Is A subset of B IV. Are A and B disjoint sets V. Join A with B and B with A VI. What is the symmetric difference between A and B VII. Delete the sets completely

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# I. Join A and B
A_union_B = A.union(B)
print("A union B:", A_union_B)

# II. Find A intersection B
A_intersection_B = A.intersection(B)
print("A intersection B:", A_intersection_B)

# III. Is A subset of B
is_A_subset_of_B = A.issubset(B)
print("Is A a subset of B:", is_A_subset_of_B)

# IV. Are A and B disjoint sets
are_A_and_B_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets:", are_A_and_B_disjoint)

# V. Join A with B and B with A
A_union_B = A.union(B)
B_union_A = B.union(A)
print("A union B:", A_union_B)
print("B union A:", B_union_A)

# VI. What is the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_diff)

# VII. Delete the sets completely
del A
del B
print("Sets A and B are deleted.")