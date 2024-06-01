from datetime import timedelta
import sys,time,os
import numpy as np
    
def get_primes(x,start=0): 
    return [i+start for i in range(len(x)) if x[i]]
  
def isPrime(x,n): 
    if n > len(x): 
        print(f"{n:,} too large max is {len(p):,}") 
        return 
    return x[n] == 1
    
def make_sieve(size): 
    sieve_time = time.time() 
    print(f"Creating new sieve of {size:,} primes.")
    limit = int(1 + size**0.5)+2
    p = np.ones(size,dtype=np.int8)
    p[0] = p[1] = 0
    s = p[4::2]
    s[:] = 0   # clear 4,6,8,10
    s = p[9::3]
    s[:] = 0   # clear 9,12,15...
    for i in range(5,limit,6):
        if p[i]:
            s = p[3*i::2*i]  # Get a view 
            s[:] = 0         # Clear it
        if p[i+2]:
            h = i+2
            s = p[3*h::2*h]  # Get a view 
            s[:] = 0         # Clear it
    print(f" Make sieve for {len(p):,} took {str(timedelta(seconds=time.time()-sieve_time))} ")
    return p   
    
sieve_size = 100000000
p = make_sieve(sieve_size)
n = int(input("Count primes to: >"))
start_time = time.time() 
c=0
if n <= sieve_size:
    c =  np.sum(p[1:n+1])
else:
    p = None
    del p
    p = make_sieve(n)
    c =  np.sum(p[1:n+1])
         
print(f"From 1 to {n:,} there are {c:,}  primes") 

print(f" Search took {str(timedelta(seconds=time.time()-start_time))} ")
