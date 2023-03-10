'''Find the next triangle number that is also pentagonal and hexagonal.'''

def tria_generator(n=285):
    while True:
        yield int(n * (n + 1) / 2)
        n += 1

def penta_generator(n=165):
    while True:
        yield int(n * (3 * n - 1) / 2)
        n += 1

def hexa_generator(n=143):   
    while True:
        yield n * (2 * n - 1)
        n += 1

tria = iter(tria_generator())
penta = iter(penta_generator())
hexa = iter(hexa_generator())

next(tria)
t, p, h = next(tria), next(penta), next(hexa)
while t != p or t != h:
    if min(t, p, h) == t:
        t = next(tria)
    elif min(t, p, h) == p:
        p = next(penta)
    else:
        h = next(hexa)

print(t)