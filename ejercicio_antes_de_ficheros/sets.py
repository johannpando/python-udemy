s1 = {1, 2, 3}
s2 = {3, 4, 5}
# incorrect
# s3 = s1 + s2
s3 = s1.union(s2)
print(s3)

# add
s3.add(7)

print(s3)

# remove
s3.remove(7)

print(s3)

# no return error
s3.discard(90)

print(s3)

# pop eliminate a random value

s3.pop()

print(s3)