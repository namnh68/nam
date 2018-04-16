import random
import threading
import time
start = time.time()
results = []

def compute():
    results.append(sum(
        [random.randint(1, 100) for i in range(1000000)]))

for i in range(8):
    compute()
end = time.time()
print("Results: %s" % results)
print("Total time {}".format(end-start))

