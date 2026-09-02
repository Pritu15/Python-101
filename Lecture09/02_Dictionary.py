# empty dictionary

d={}
print(d)
# 1D
d1={
    'name':'Arian',
    'gender':'male',
}
print(d1)

#Mixed key
d2={
    (1,2,3):1,
    'hello':"world"

}
print(d2)
print(d2[(1,2,3)])

# 2D dictionary-JSON
s={
    'name':'Pritu',
    'sem':7,
    'subjects':{
        'DSA':50,
        'Maths':70,
        'English':10

    }
}
print(s['subjects']['DSA'])

# using sequence and dict function
d4=dict([('name','pritu'),('age',32),(3,3)])
print(d4)
#duplicate keys
d5={
    'name':'Arian',
    'name':'male',
}
print(d5)

# Access items

#Adding key-value pair
d1['weight']=90
print(d1)
s['subjects']['chemistry']=90
print(s)

#Remove key-value pair
d={'name':'Pritu','age':24,3:34}
#pop
# d.pop(3)
# print(d)
# popitem
d.popitem()
print(d)
# del
del d['name']
print(d)
# clear
d.clear()
print(d)
# Editing
s['subjects']['chemistry']=85
print(s)

# Membership operator
print('name' in s)
d={
    'name':'pritu',
    'gender':'Male',
    'age':24
}

for i in d:
    print(i,d[i])