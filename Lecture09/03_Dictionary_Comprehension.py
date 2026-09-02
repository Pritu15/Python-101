print({i:i**2 for i in range(1,11)})

distances={'dhaka':1000,'chattogram':500,'sylhet':600}
print(distances.items())
print({key:value*0.62 for (key,value) in distances.items()})

print( {key:distances[key]*0.62 for key in distances})

days=["Sunday","Monday","Tuesday"]
temp_c=[30.5,40.5,31]

s={i:j for (i,j) in zip(days,temp_c)}
print(s)