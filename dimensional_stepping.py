bases_step = 10
bases = 3
count = 1


all_steps = []
all_bases = range(bases, bases_step)
for base in all_bases:
    all_steps.append(((base * base) * (bases_step)))

for step in all_steps:
    step = (step ** step)
    print(step)
    count += 1
