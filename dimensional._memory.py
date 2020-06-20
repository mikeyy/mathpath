# Looking for dimensional memory (memory in math)

import time

base_step = 10
bases = 3
steps = ((bases * bases) * (base_step)) / (base_step * base_step)
count = 1
while 1:
    steps = ((steps ** 2) ** steps) / (base_step * 2)
    print(steps, count)
    count += 1
    time.sleep(1)
