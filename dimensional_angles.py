base = 3
steps = 10
first_dimension = ((steps-1) *  (steps-2)) * steps
second_dimension = (steps  + (steps - 1)) * (steps - 1)

result = second_dimension ** 2
for step in range(steps + 3, second_dimension):
    result = (step * (result))

print(result)


'''
waves = sound_files[0]
frequencies = [0, 1]

frequency = 1hz  
clock_speed = frequency/3
calculation = clock_speed

'''
