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
    if x <=1000:
        count = sum(p[y:x+1])
        return count
    count = 0
    if y < 5:
        count = 2
        y = 5
    for i in range(y,x,6):
        if is_prime(i):
            count += 1
        if is_prime(i+2):
            count += 1
    return count

# simple sieve primes to 1000
p = [1 if is_prime(i) else 0 for i in range(1,1001) ]

n = int(input("Count primes to: >"))
cpus = multiprocessing.cpu_count() 
thrd = cpus - 1
if n > 1000*thrd:
    a = n//cpus + 1
    nums = []
    k = n
    while k - a > 1:
        s = k-a
        s = s-s%6-1  # Split at 6k-1 boundry 
        if s<a: s =1
        nums.append([s,k])
        k = s-1
    print(f"{nums=} ")  # Show the sets 
    start_time = time.time() 
    p =  multiprocessing.Pool(processes=(thrd)) # get some threads for our pool
    results=p.map(prime_range, nums) # one thread per arctan(1/xxxx)
    p.close()
    p.join()  # wait for them to finish
    print(f"{results=}")
    c = sum(results)
else:
    start_time = time.time()
    c = prime_range([1,n])
print(f"From 1 to {n:,} there are {c:,}  primes") 

print(f" Search took {str(timedelta(seconds=time.time()-start_time))} ")
