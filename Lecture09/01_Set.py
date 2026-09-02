# Set Operation

s1={1,2,3,4,5}
s2={4,5,6,7,8}

# UNION
print(s1|s2)
# Intersection(&)
print(s1&s2)
# Difference(-)
print(s1-s2)
print(s2-s1)

# Symmetric Difference (^)
print(s1^s2)
# Membership Operator
print(1 not in s1)
for i in s1:
    print(i)

# len,sum,min,max,sorted

# Union/update

s1={1,2,3,4,5}
s2={4,5,6,7,8}
# print(s1.union(s2))
# print(s1)
print(s1.update(s2))
print(s1)
#intersection/intersection_update

#difference/difference_update

#symmetric/symmetric_update

#isdisjoint/issubset/issuperset


s1={1,2,3}
s2=s1
s1={4,5,6}
print(s2)
print(s1)