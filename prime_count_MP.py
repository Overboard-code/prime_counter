from gmpy2 import is_prime
from datetime import timedelta
import sys,multiprocessing,time

#----------------------------------------------#
#  uses the 6k plus minus one rule to split a 
#  list of numbers into groups equal to number
#  of CPUs.  Then start a process on each range
#  to count all found primes. 
#----------------------------------------------#

def prime_range(ste): 
    # code requires ste[0] to be 6k-1 
    x = ste[1]
    y = ste[0]
    # Find number of primes from y to x
    count = 0
    if y < 5 and x >= 5:
        y = 5
        count = 2
    if (((y+1)//6)*6)-1 != y:
        print(f"{y:,} is not in form 6k-1") 
        raise Exception("Start is not 6k-1 number. Failing")
    for k6 in range(y,x,6):  # for each 6k-1 
        if is_prime(k6):    # 6k-1
            count += 1
        if is_prime(k6+2):   # 6k+1
            count += 1
    return count
    
sieve_size = 1000000
# simple sieve of primes to 1,000,000
p = bytearray([0] * sieve_size)
p[2] = 1
p[3] = 1 
for i in range(5,sieve_size+1,6): 
    if is_prime(i):   p[i] = 1
    if is_prime(i+2): p[i+2] = 1

n = int(input("Count primes to: >"))
CPUs = multiprocessing.cpu_count()  
chunk = n//(CPUs)   # one chunk per CPU thread
if n > sieve_size:
    nums = []
    end = n
    while end > chunk:
        strt = end-chunk
        strt = strt-strt%6-1  # Split at 6k-1 boundry 
        nums = [[strt,end]] + nums[:]
        end = strt-1  # Set new end one less than previous start
    nums = [[1,end]] + nums[:]  # last chunk 
    print(f"{nums=} ")  # Show the sets 
    start_time = time.time() 
    print(f"{CPUs=}  {chunk=} ") 
    pool =  multiprocessing.Pool(processes=(CPUs)) # get some threads for our pool
    results=pool.map(prime_range, nums) # one thread per chunk
    pool.close()
    pool.join()  # wait for them to finish
    print(f"results per thread: {results=}")
    c = sum(results)
else:
    start_time = time.time()
    c = sum(p[1:n+1])
    
print(f"From 1 to {n:,} there are {c:,}  primes") 

print(f" Search took {str(timedelta(seconds=time.time()-start_time))} ")
