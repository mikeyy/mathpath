# Looking for dimensional memory

import time

base_step = 10
bases = 3
steps = ((bases * bases) * (base_step)) / (base_step * base_step)
while 1:
    steps = ((steps ** 2) ** steps) / (base_step * 2)
    print(steps)
    time.sleep(1)
