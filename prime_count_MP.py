from gmpy2 import is_prime
from datetime import timedelta
import sys,multiprocessing,time

#----------------------------------------------#
#  uses the 6k plus minus one rule to split a 
#  list of numbers into groups equal to number
#  of CPUs minus 1.  Then start a task on each range
#   to count all found primes. 
#----------------------------------------------#

def prime_range(ste): 
    x = ste[1]
    y = ste[0]
    # Find number of primes from 1 to x
    count = 0
    if y < 5:
        y = 5
        count = 2
    for i in range(y,x,6):
        if is_prime(i):
            count += 1
        if is_prime(i+2):
            count += 1
    return count

# simple sieve primes to 10000
p = [1 if is_prime(i) else 0 for i in range(10001) ]

n = int(input("Count primes to: >"))
thrds = multiprocessing.cpu_count() - 1
chunk = n//(thrds+1)   # one chunk per thread
if n > len(p):
    nums = []
    end = n
    while end - chunk > 1:
        strt = end-chunk
        strt = strt-strt%6-1  # Split at 6k-1 boundry else range fails
        if strt < chunk: strt = 1  # set bottom to all that's left
        nums = [[strt,end]] + nums[:]
        end = strt-1  # Set new end one less than this start
    print(f"{nums=} ")  # Show the sets 
    start_time = time.time() 
    p =  multiprocessing.Pool(processes=(thrds)) # get some threads for our pool
    results=p.map(prime_range, nums) # one thread per chunk
    p.close()
    p.join()  # wait for them to finish
    print(f"{results=}")
    c = sum(results)
else:
    start_time = time.time()
    c = sum(p[1:n+1])
    
print(f"From 1 to {n:,} there are {c:,}  primes") 

print(f" Search took {str(timedelta(seconds=time.time()-start_time))} ")
