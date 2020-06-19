# Time synchronization
bases = 4
dimensions = 3
steps = (bases * dimensions)

b = ['(' for step in range(81)]
c = [' ** steps)' for step in range(81)]
d =  ''.join(b) + 'steps' +''.join(c)
print(d)
e = eval(d)
