import time

start_time = time.perf_counter()

time.sleep(1)

end_time = time.perf_counter()

time = end_time - start_time
print(time)