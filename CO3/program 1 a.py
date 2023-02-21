import random
l=['ann','ben','ciril','raju']
print(random.choice(l))
print(random.choices(l,k=4))
print(random.sample(l,k=1))
random.shuffle(l)
print(l)
print(random.randrange(2,9,2))