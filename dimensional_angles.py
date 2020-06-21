base = 3
steps = 10
first_dimension = ((steps-1) *  (steps-2)) * steps
second_dimension = (steps  + (steps - 1)) * (steps - 1)

result = second_dimension ** 2
for step in range(steps + 3, second_dimension):
    result = (step * (result))

# Forever loop (Large calculations)

base = 3
steps = base ** base
angles = ((steps-1) * (steps-2)) ** steps
while 1:
    angles = angles ** steps
    print(len(str(angles)))
