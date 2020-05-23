import time
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = time.time()
input("Press enter to stop")
end_time = time.time()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print(f"Your reaction time was {end_time - start_time} seconds")